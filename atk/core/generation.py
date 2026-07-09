from atk.core.llm import ask
from atk.languages import LANGUAGES
from pathlib import Path
import re
import tempfile

MAX_ATTEMPTS = 4


def build_prompt(topic: str, difficulty: str, language: dict) -> str:
    return f"""
        You are an expert {language["name"]} teacher writing a practice
        challenge for a self-taught learner - this repository is their
        autodidact's toolkit. The learner can program, but may have gaps in
        math, in domain jargon, and in {language["name"]}-specific idioms -
        never assume outside knowledge.

        Create a single {language["name"]} coding challenge based on:

        Topic:
        {topic}

        Difficulty:
        {difficulty}

        What a great challenge looks like:
        - A small, concrete scenario (a shopkeeper, a library, a ferry, a
          wizard's workshop) with data that matters and rules to enforce -
          not an abstract puzzle.
        - The topic is load-bearing: solving the challenge must REQUIRE the
          topic, not merely permit it.
        - It has verifiable acceptance criteria the learner's work must
          satisfy exactly.
        - Keep the test data SMALL (3-5 items) so expected values are easy
          to compute correctly.
        - {language["edge_rule"]}

        Difficulty guide:
        {language["difficulty_guide"]}

        The challenge description MUST contain these sections, in this order:

        STORY
            2-5 sentences setting the scenario.
        YOUR TASK
            Numbered requirements: the exact names of the things to write,
            their inputs and outputs, and the rules they must enforce.
        {language["acceptance_title"]}
            {language["acceptance_spec"]}
        BACKGROUND
            The most important section. Explain every concept the task
            relies on, assuming zero prior exposure: any math (e.g. what a
            perfect square is and how you would recognize one), any domain
            jargon, and any {language["name"]} behavior that might surprise
            a newcomer. Explain the IDEAS and name useful building blocks,
            but NEVER assemble them into the solution.
        HINTS
            2-4 nudges that point at where to think, not what to type.
            No code.

        Formatting rules:
        - Do not put solution or implementation code in the challenge
          (acceptance criteria and tiny illustrative one-liners in
          BACKGROUND are allowed).
        - Each section must appear EXACTLY ONCE, in the order given.
        - The entire challenge must be {language["challenge_wrapper"]}.
        - Use plain ASCII characters only (write * for multiplication,
          never the times sign).
        {language["extra_rules"]}

        Exercise Rules:
        - Generate a creative snake_case exercise.
        - The exercise should be 2 words.
        - Do not describe the challenge directly.
        - Do NOT reuse the example names below - invent a fresh one.
        - Use names similar to:
        - golden_sun
        - crimson_forest
        - silent_mountain

        Reference solution rules:
        - After the challenge, provide a complete reference solution proving
          the challenge is correct and solvable. A machine runs it to verify
          the challenge; the learner never sees it.
        - {language["solution_spec"]}
        - The solution must be BARE runnable code: never wrapped in a
          comment, never in markdown fences.

        Final check before you answer (do this silently, fix what fails):
        1. Recompute the expected value of EVERY acceptance check from the
           test data, applying the rules in YOUR TASK literally. If a check
           and a rule disagree, fix whichever is wrong.
        2. Confirm BACKGROUND would let someone who has never met the
           topic's underlying concepts (math, jargon) solve the task.
        3. Confirm no section of the challenge contains the assembled
           solution.

        Return ONLY this format:

        EXERCISE:
        <exercise>

        CONTENT:
        <the challenge, wrapped as described above>

        SOLUTION:
        <the runnable reference solution>
    """


def build_repair_prompt(response: str, failure: str) -> str:
    return f"""
        You wrote the coding challenge and reference solution below, but the
        reference solution FAILED when executed. Diagnose the failure and fix
        it: correct the solution, and if an acceptance check itself is wrong
        (a miscomputed expected value), fix the challenge too so the checks
        and the rules agree.

        Return the COMPLETE corrected output in the exact same format
        (EXERCISE: / CONTENT: / SOLUTION:), nothing else. Keep the same
        exercise name.

        FAILURE OUTPUT:
        {failure}

        YOUR PREVIOUS OUTPUT:
        {response}
    """


def strip_fences(text: str) -> str:
    """Drop markdown code fences if the model wrapped a section in them."""
    lines = text.strip().splitlines()

    if lines and lines[0].startswith("```"):
        lines = lines[1:]
    if lines and lines[-1].startswith("```"):
        lines = lines[:-1]

    return "\n".join(lines).strip()


def parse(response: str) -> tuple[str, str, str]:
    # Split on the section headers, tolerating trailing whitespace after the
    # colon (models frequently emit "EXERCISE:  \n").
    parts = re.split(r"^(EXERCISE|CONTENT|SOLUTION):[ \t]*\n", response, flags=re.MULTILINE)
    sections = {parts[i]: parts[i + 1] for i in range(1, len(parts) - 1, 2)}

    exercise = sections["EXERCISE"].strip()

    return exercise, strip_fences(sections["CONTENT"]), strip_fences(sections["SOLUTION"])


def verify(solution: str, language: dict) -> tuple[bool | None, str]:
    """Run the reference solution; if its own checks fail, the challenge is broken.

    Returns (True, output) on success, (False, output) on failure, and
    (None, reason) when the solution could not be executed at all.
    """
    with tempfile.NamedTemporaryFile(
        "w", suffix=language["solution_suffix"], delete=False, encoding="utf-8"
    ) as handle:
        handle.write(solution)
        path = Path(handle.name)

    try:
        return language["run_solution"](path)
    finally:
        path.unlink()


def unique_directory(base: str, exercise: str) -> Path:
    """Never overwrite an existing exercise; add a numeric suffix instead."""
    directory = Path(f"{base}/{exercise}")
    suffix = 2

    while directory.exists():
        directory = Path(f"{base}/{exercise}_{suffix}")
        suffix += 1

    return directory


def generate(topic: str, difficulty: str, language_key: str):
    language = LANGUAGES[language_key]
    prompt = build_prompt(topic, difficulty, language)

    response = None
    failure = None
    repaired = False

    for attempt in range(1, MAX_ATTEMPTS + 1):
        # A failed verification gets ONE repair pass (the model sees its own
        # error output). If the repair also fails, start fresh - asking the
        # model to re-repair just anchors it to its own broken output.
        if failure is not None and not repaired:
            response = ask(build_repair_prompt(response, failure))
            repaired = True
        else:
            response = ask(prompt)
            repaired = False

        failure = None

        try:
            exercise, content, solution = parse(response)
        except (ValueError, IndexError, KeyError):
            print(f"\nAttempt {attempt}: response drifted from the EXERCISE/CONTENT/SOLUTION format, retrying...")
            continue

        ran_ok, output = verify(solution, language)

        if ran_ok:
            break

        if ran_ok is None:
            print(f"\nWARNING: saving UNVERIFIED challenge - {output}")
            break

        failure = output
        print(f"\nAttempt {attempt}: the reference solution failed its checks, asking the model to repair it...")
        print(output)
    else:
        raise RuntimeError(f"No verified challenge after {MAX_ATTEMPTS} attempts - try re-running.")

    directory = unique_directory(language["directory"], exercise)
    directory.mkdir(parents=True)

    file = directory / language["challenge_file"]
    file.write_text(content, encoding="utf-8")

    print(f"\nSaved challenge to {file}")

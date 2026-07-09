from atk.core.llm import ask
from atk.languages import by_path
from pathlib import Path
from datetime import datetime


def execution_status(ran_ok: bool | None) -> str:
    if ran_ok is None:
        return "NOT RUN - judge correctness by reading the code carefully"
    if ran_ok:
        return "PASSED - exited cleanly"
    return "FAILED - did not exit cleanly"


def review(code_file: Path) -> None:
    """Review the solution at code_file against the challenge that lives
    beside it. The file's extension determines the language."""
    language_key, language = by_path(code_file)

    directory = code_file.parent
    exercise = directory.name

    challenge = (directory / language["challenge_file"]).read_text(encoding="utf-8")
    solution = code_file.read_text(encoding="utf-8")

    ran_ok, run_output = language["run_code"](code_file)

    prompt = f"""
        You are a {language["reviewer"]} reviewing a student's solution to a
        coding challenge. The student is a self-taught developer building
        breadth across languages - this repository is their autodidact's
        toolkit. They are strongest in JavaScript, so compare to JS defaults
        where it genuinely helps (skip the comparison where it doesn't).

        THE CHALLENGE:
        {challenge}

        THE STUDENT'S SOLUTION:
        {solution}

        EXECUTION RESULT:
        Status: {execution_status(ran_ok)}
        Output:
        {run_output}

        Write a code review as Markdown.

        Begin your output with EXACTLY one line, then a blank line:
        VERDICT: PASS
        or
        VERDICT: FAIL

        PASS requires BOTH of these to be true:
        - The solution is correct - if the EXECUTION RESULT above is FAILED,
          the verdict MUST be FAIL, and your Blocking bugs section must be
          based on the actual error output, not speculation. If the code was
          NOT RUN, judge correctness by careful reading against the
          challenge's acceptance criteria.
        - The target feature was genuinely practiced, not dodged.

        After the verdict line, follow this exact structure:

        # {exercise} - Code Review Notes

        A one-paragraph summary. If there is a single recurring theme across
        the issues, name it here.

        ## Blocking bugs (can't run correctly)
        Anything that crashes, fails to compile, or prevents a correct run.
        Empty is fine - say so.

        ## Logic bugs (runs, but wrong behavior)
        Wrong results, off-by-one, mishandled edge cases.

        ## Design / idiom
        Non-idiomatic {language["name"]}, awkward structure, better
        standard-tool choices.

        ## Did the solution practice the target feature?
        The whole point of this exercise is to practice a specific feature or
        concept. Identify which one the challenge was built around, then state
        plainly whether the solution actually used it - or dodged it with a
        workaround. This is the most important section.

        ## Checks you should add
        {language["checks_spec"]}

        ## Reference version
        One clean, idiomatic implementation in a {language["name"]} code block.

        ## Quick reference
        A Markdown table of the concepts that came up, one row each, with a
        short JS comparison where it clarifies.

        Rules:
        - Order issues most-severe first within each section.
        - Quote the student's own code when pointing at a problem.
        - Be direct and specific; no vague praise.
        - Output ONLY the Markdown review, nothing before or after it.
    """

    response = ask(prompt, options={"temperature": 0, "seed": 42}).strip()

    # Objective correctness gate: a solution that ran and failed cannot pass,
    # whatever the model concluded. Force the verdict to FAIL. (A solution
    # that could not be run at all is left to the model's judgement.)
    if ran_ok is False:
        lines = response.splitlines()

        if lines and lines[0].upper().startswith("VERDICT:"):
            lines[0] = "VERDICT: FAIL"
            response = "\n".join(lines)
        else:
            response = "VERDICT: FAIL\n\n" + response

    file = directory / "review.md"

    # Keep history: archive the current review (if any) before overwriting it,
    # stamped with when it was written, so review.md always holds the latest.
    if file.exists():
        history = directory / "reviews"
        history.mkdir(exist_ok=True)
        stamp = datetime.fromtimestamp(file.stat().st_mtime).strftime("%Y%m%d-%H%M%S")
        file.rename(history / f"review-{stamp}.md")

    file.write_text(response, encoding="utf-8")

    verdict = response.splitlines()[0] if response else "VERDICT: UNKNOWN"
    print(f"\n{'=' * 40}\n{verdict}\n{'=' * 40}")

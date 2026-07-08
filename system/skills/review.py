from system.llm import ask
from pathlib import Path
from datetime import datetime
import subprocess
import argparse
import sys

def run_solution(path: Path) -> tuple[bool, str]:
    """Run the solution and report whether it exited cleanly, plus its output."""
    try:
        result = subprocess.run(
            [sys.executable, str(path)],
            capture_output=True,
            text=True,
            timeout=30,
        )
    except subprocess.TimeoutExpired:
        return False, "Timed out after 30s (possible infinite loop)."

    ran_ok = result.returncode == 0
    output = (result.stdout + result.stderr).strip() or "(no output)"
    return ran_ok, output

def review(exercise: str) -> None:
    directory = Path(f"python/{exercise}")

    challenge = (directory / "challenge.py").read_text(encoding="utf-8")
    solution = (directory / "code.py").read_text(encoding="utf-8")

    ran_ok, run_output = run_solution(directory / "code.py")

    prompt = f"""
        You are a senior Python engineer reviewing a student's solution to a
        coding challenge. The student is strong in JavaScript and is learning
        Python, so compare to JS defaults where it genuinely helps.

        THE CHALLENGE:
        {challenge}

        THE STUDENT'S SOLUTION:
        {solution}

        EXECUTION RESULT (the solution was actually run):
        Status: {"PASSED — exited cleanly" if ran_ok else "FAILED — did not exit cleanly"}
        Output:
        {run_output}

        Write a code review as Markdown.

        Begin your output with EXACTLY one line, then a blank line:
        VERDICT: PASS
        or
        VERDICT: FAIL

        PASS requires BOTH of these to be true:
        - The program runs correctly — the EXECUTION RESULT above is PASSED.
        - The target language feature was genuinely practiced, not dodged.
        If the execution FAILED, the verdict MUST be FAIL — base your Blocking
        bugs section on the actual error output above, not on speculation.

        After the verdict line, follow this exact structure:

        # {exercise} — Code Review Notes

        A one-paragraph summary. If there is a single recurring theme across
        the issues, name it here.

        ## Blocking bugs (program can't run correctly)
        Anything that crashes or prevents a correct run. Empty is fine — say so.

        ## Logic bugs (runs, but wrong behavior)
        Wrong results, off-by-one, mishandled edge cases.

        ## Design / idiom
        Non-idiomatic Python, awkward structure, better standard-library tools.

        ## Did the solution practice the target feature?
        The whole point of this exercise is to practice a specific language
        feature. Identify which feature the challenge was built around, then
        state plainly whether the solution actually used it — or dodged it with
        a workaround. This is the most important section.

        ## Asserts you should add
        List 3–5 concrete test cases the student should add to their own main()
        to prove the solution. Give each as an input and the exact expected
        result (assert lines are ideal). Include at least one edge case, and —
        if the challenge implies an error path — one assert that proves the
        error is raised. These must be actionable, so the student can paste
        them in and re-run.

        ## Reference version
        One clean, idiomatic implementation in a Python code block.

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

    # Objective correctness gate: a solution that didn't run cleanly cannot
    # pass, whatever the model concluded. Force the verdict to FAIL.
    if not ran_ok:
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

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--exercise", required=True)

    arguments = parser.parse_args()

    review(arguments.exercise)


main()

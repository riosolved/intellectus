"""Python - the reference language definition.

This module is the pattern to copy when adding a language: one LANGUAGE
dict declaring everything the pipelines need. See documentation/adding-a-language.md
for the authoring checklist.
"""

from atk.runtime.runners.python import run_python, run_python_with_requirements

LANGUAGE = {
    "name": "Python",
    "directory": "interests/python/challenges",
    "extensions": [".py"],
    "challenge_file": "challenge.py",
    "code_file": "code.py",
    "reviewer": "senior Python engineer",

    # challenge generation
    "challenge_wrapper": "a single triple-quoted docstring so it saves directly as a valid `.py` file",
    "difficulty_guide": (
        "- beginner: one or two short functions, no classes, 2-4 asserts.\n"
        "- medium: several functions or 2-3 small classes that interact, 4-6 asserts.\n"
        "- hard: a multi-part design with edge cases, error handling, and asserts that probe them."
    ),
    "edge_rule": (
        "It includes at least one failure path (invalid input, a limit "
        "being hit, an error that must be raised), not just the happy path."
    ),
    "acceptance_title": "ASSERTS",
    "acceptance_spec": (
        "A code block of assert statements the learner's main() must make "
        "pass, using the exact names from YOUR TASK. (Asserts are "
        "acceptance criteria, not solution code - they are required.) "
        "The block must be SELF-CONTAINED: define any starting data it "
        "uses (initial dicts, lists, objects) at the top of the block - "
        "the learner cannot see data that only exists in your head."
    ),
    "extra_rules": "",
    "solution_spec": (
        "Plain runnable Python: the implementations named in YOUR TASK, "
        "followed by the assert statements from ASSERTS, copied EXACTLY. "
        "No markdown fences, no docstring wrapper, no explanations."
    ),
    "solution_suffix": ".py",
    # Generated reference solutions are stdlib-only, so they run with no
    # network; YOUR code may declare a requirements.txt beside it.
    "run_solution": run_python,
    "run_code": run_python_with_requirements,

    # review
    "checks_spec": (
        "List 3-5 concrete test cases the student should add to their own "
        "main() to prove the solution. Give each as an input and the exact "
        "expected result (assert lines are ideal). Include at least one "
        "edge case, and - if the challenge implies an error path - one "
        "assert that proves the error is raised. These must be actionable, "
        "so the student can paste them in and re-run."
    ),
}

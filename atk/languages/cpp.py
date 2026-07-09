"""C++ language definition. python.py is the annotated reference pattern."""

from atk.runtime.runners.cpp import run_cpp

LANGUAGE = {
    "name": "C++",
    "directory": "interests/c++/challenges",
    "extensions": [".cpp", ".cc"],
    "challenge_file": "challenge.cpp",
    "code_file": "code.cpp",
    "reviewer": "senior C++ engineer",

    "challenge_wrapper": "a single /* ... */ block comment so it saves directly as a valid `.cpp` file",
    "difficulty_guide": (
        "- beginner: one or two short functions, 2-4 asserts.\n"
        "- medium: several functions or a small class/struct that interact, 4-6 asserts.\n"
        "- hard: a multi-part design with edge cases, error handling, and asserts that probe them."
    ),
    "edge_rule": (
        "It includes at least one failure path (invalid input, a limit "
        "being hit, an error that must be handled), not just the happy path."
    ),
    "acceptance_title": "ASSERTS",
    "acceptance_spec": (
        "A code block of assert(...) calls (from <cassert>) the learner's "
        "main() must make pass, using the exact names from YOUR TASK. "
        "(Asserts are acceptance criteria, not solution code - they are "
        "required.) The block must be SELF-CONTAINED: define any starting "
        "data it uses (vectors, structs, values) at the top of the block - "
        "the learner cannot see data that only exists in your head."
    ),
    "extra_rules": "- Target C++17 and the standard library only - no external dependencies.",
    "solution_spec": (
        "A complete compilable C++17 program: all #includes, the "
        "implementations named in YOUR TASK, and a main() containing the "
        "assert statements from ASSERTS, copied EXACTLY, that returns 0. "
        "Standard library only. No markdown fences, no explanations."
    ),
    "solution_suffix": ".cpp",
    "run_solution": run_cpp,
    "run_code": run_cpp,

    "checks_spec": (
        "List 3-5 concrete test cases the student should add to their own "
        "main() to prove the solution. Give each as an input and the exact "
        "expected result (assert(...) lines are ideal). Include at least "
        "one edge case. These must be actionable, so the student can paste "
        "them in and re-run."
    ),
}

"""SQL language definition. python.py is the annotated reference pattern.

SQL is the odd one out: challenges are verified by a PYTHON reference
script (stdlib sqlite3) running in the python container, and student
queries are reviewed statically - there is no engine to execute a bare
.sql file against.
"""

from atk.runtime.runners.python import run_python
from atk.runtime.runners.sql import skip_run

LANGUAGE = {
    "name": "SQL",
    "directory": "interests/sql/challenges",
    "extensions": [".sql"],
    "challenge_file": "challenge.sql",
    "code_file": "code.sql",
    "reviewer": "senior SQL engineer",

    "challenge_wrapper": "a single /* ... */ block comment so it saves directly as a valid `.sql` file",
    "difficulty_guide": (
        "- beginner: a single-table SELECT with WHERE and ORDER BY.\n"
        "- medium: a join or GROUP BY with an aggregate across 2-3 small tables.\n"
        "- hard: subqueries, HAVING, window functions, or multi-step logic."
    ),
    "edge_rule": (
        "It includes at least one trap in the data: a row that a sloppy "
        "query (wrong join type, missing filter, missing GROUP BY) would "
        "wrongly include or drop."
    ),
    "acceptance_title": "DATA AND EXPECTED RESULT",
    "acceptance_spec": (
        "The complete setup and expected output: the CREATE TABLE "
        "statements, the INSERT statements (3-5 rows per table, explicit "
        "ids), and the EXACT rows the learner's query must return, drawn "
        "as a small text table. YOUR TASK must require a deterministic "
        "ORDER BY so exactly one output is correct."
    ),
    "extra_rules": (
        "- Use portable SQL that runs identically on SQLite and MySQL: "
        "INTEGER PRIMARY KEY instead of AUTO_INCREMENT, explicit ids in "
        "every INSERT, no vendor-specific functions.\n"
        "        - The task must be solvable with a single query."
    ),
    "solution_spec": (
        "A plain runnable PYTHON script (not SQL) using only the "
        "standard-library sqlite3 module: create the schema, insert the "
        "data, run the reference query, fetch the rows, and assert they "
        "equal the expected result EXACTLY. No markdown fences, no "
        "explanations."
    ),
    "solution_suffix": ".py",
    "run_solution": run_python,
    "run_code": skip_run,

    "checks_spec": (
        "List 3-5 extra data rows or scenarios that would expose a wrong "
        "query (e.g. a parent row with no children for a join challenge, "
        "a tie that tests the ORDER BY), each with the result the correct "
        "query must then return."
    ),
}

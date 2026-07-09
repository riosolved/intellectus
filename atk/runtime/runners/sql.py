"""How SQL "executes": it doesn't - and that is the whole module.

A bare .sql file has no engine to run against, so student queries are
reviewed statically. (Challenge VERIFICATION is different: the model's
reference solution for SQL is a Python sqlite3 script, executed by
runners.python.run_python - see atk/languages/sql.py wiring both.)
"""


def skip_run(path) -> tuple[None, str]:
    return None, "SQL files are not executed automatically - the review is static."

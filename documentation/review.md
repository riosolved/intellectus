# review - Grade your solution

Reads a challenge and your solution, executes your code in a container,
then asks the local model for a tiered code review and a `PASS` / `FAIL`
verdict.

## Command

The `atk review <file>` command is in progress (see the guided TODO in
`atk/cli/review.py`). The pipeline itself is complete and callable:

```bash
.venv/Scripts/python.exe -c "from pathlib import Path; from atk.core.review import review; review(Path('interests/python/challenges/magic_numbers/code.py'))"
```

You point at your **code file**; its extension determines the language and
its parent folder is the exercise. The review is written to `review.md`
beside it.

## Execution before review

Your solution is executed first, per language:

| Language | Execution |
|----------|-----------|
| Python | Runs in the `atk-python` container; a `requirements.txt` beside your code is baked into a cached derived image (rebuilt only when it changes) |
| C++ | Compiled and run in the `atk-cpp` container |
| SQL | Not executed - reviewed statically |

## The verdict

Every review begins with a machine-readable first line, reprinted as a
banner when the run finishes:

```
========================================
VERDICT: PASS
========================================
```

**PASS requires both:**

1. The solution is correct.
2. The target feature was genuinely practiced, not dodged.

The first condition is gated **objectively** where possible: if your code
ran and did not exit cleanly (a crash, a failed assert, a compile error),
the verdict is forced to `FAIL` regardless of what the model thinks, and
the real error output is fed into the review. Code that could not be
executed at all (SQL, engine down) is judged by careful reading instead.

The second condition is the model's judgment, and it is the whole point:
you can get the right answer with the wrong technique - solving a
generator exercise with a plain loop - and a normal test wouldn't notice.
The review does, and fails you for it.

Reviews are **reproducible**: the model runs at `temperature: 0` with a
fixed seed, so the same code yields the same verdict.

## Re-reviewing keeps history

`review.md` always holds the **latest** review. Each re-run archives the
previous one into a `reviews/` subfolder, stamped with when it was written:

```
interests/<language>/challenges/<name>/
|-- review.md                        <- latest
`-- reviews/
    |-- review-20260707-142310.md    <- older, kept
    `-- review-20260707-160845.md
```

## What's in the review

| Section | Covers |
|---------|--------|
| Blocking bugs | Crashes, compile errors, anything preventing a correct run |
| Logic bugs | Runs, but wrong results or mishandled edge cases |
| Design / idiom | Non-idiomatic code, awkward structure, better tools |
| Target feature | Whether you actually practiced the intended feature |
| Checks you should add | Concrete test cases to paste in and re-run |
| Reference version | One clean, idiomatic implementation |
| Quick reference | Concept table, with JS comparisons where they help |

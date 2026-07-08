# review — Grade your solution

Reads a challenge and your solution, then asks the local model for a tiered
code review and a `PASS` / `FAIL` verdict. This is step 3 of the loop; see
[../README.md](../README.md) for the full picture.

## Command

Run from the **repo root** (`intellectus/`):

```bash
.venv/Scripts/python.exe -m system.skills.review --exercise magic_numbers
```

| Flag | Meaning | Example |
|------|---------|---------|
| `--exercise` | The folder name under `python/` to review | `magic_numbers` |

It reads `python/<exercise>/challenge.py` and `python/<exercise>/code.py`, and
writes the review to `python/<exercise>/review.md`.

## Re-reviewing keeps history

`review.md` always holds the **latest** review. Each time you re-run, the
previous `review.md` is archived first — moved into a `reviews/` subfolder and
stamped with when it was written:

```
python/<exercise>/
├── review.md                        ← latest
└── reviews/
    ├── review-20260707-142310.md    ← older, kept
    └── review-20260707-160845.md
```

So you can re-review after each fix and watch the verdict progress from `FAIL`
to `PASS` over time, without losing any earlier feedback.

## The verdict

Every review begins with a machine-readable first line, reprinted as a banner
when the run finishes:

```
========================================
VERDICT: PASS
========================================
```

**`PASS` requires both:**

1. The program runs correctly.
2. The target language feature was genuinely practiced, not dodged.

The first condition is checked **objectively**: before reviewing, the skill
actually runs your `code.py` in a subprocess. If it doesn't exit cleanly
(a crash, or a failed `assert`), the verdict is forced to `FAIL` regardless of
what the model thinks — and the real error output is fed into the review so the
Blocking bugs section describes the actual failure, not a guess.

The second condition is the model's judgment. It's the whole point of the
exercise: you can get the right answer with the wrong technique — solving a
generator exercise with a plain loop — and a normal test wouldn't notice. The
review does, and fails you for it.

Reviews are **reproducible**: the model runs at `temperature: 0` with a fixed
seed, so the same code yields the same verdict instead of drifting between runs.

## What's in the review

The saved `review.md` follows a fixed structure, most-severe first:

| Section | Covers |
|---------|--------|
| Blocking bugs | Crashes or anything preventing a correct run |
| Logic bugs | Runs, but wrong results or mishandled edge cases |
| Design / idiom | Non-idiomatic Python, awkward structure, better tools |
| Target feature | Whether you actually practiced the intended feature |
| Asserts you should add | Concrete test cases to paste into your `main()` |
| Reference version | One clean, idiomatic implementation |
| Quick reference | Concept table, with JS comparisons where they help |

The **Asserts you should add** section is what makes the fix → re-review loop
productive: a `FAIL` tells you exactly which cases to cover, you add them, and
run the review again.

## Possible upgrades

- **Exit code** — `sys.exit(0)` on `PASS`, `sys.exit(1)` on `FAIL`, so the
  verdict is scriptable (shell chains, git hooks, CI).

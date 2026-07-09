# challenge - Generate a machine-verified challenge

Asks the local model to invent a coding challenge for a topic, difficulty,
and language, verifies it actually works, then saves it ready to solve.

## Command

```bash
.venv/Scripts/atk.exe challenge --topic "joins and grouping" --difficulty medium --language sql
```

| Flag | Meaning | Values |
|------|---------|--------|
| `--topic` | The feature or theme to drill (required) | `generators`, `joins`, `vectors and iteration` |
| `--difficulty` | How hard it should be | `beginner`, `medium` (default), `hard` |
| `--language` | Which language | `python` (default), `c++`, `sql` |

The model invents a whimsical two-word name and writes the challenge to
`interests/<language>/challenges/<name>/challenge.*`. Existing exercises are never
overwritten - a name collision gets a `_2` suffix.

## What a challenge contains

Every challenge has five sections, in order:

| Section | Purpose |
|---------|---------|
| STORY | A small concrete scenario |
| YOUR TASK | Numbered requirements with exact names, inputs, outputs, rules |
| ASSERTS (or DATA AND EXPECTED RESULT for SQL) | Self-contained acceptance criteria your solution must pass |
| BACKGROUND | Every concept explained from zero prior exposure - math, jargon, surprising language behavior - without revealing the solution |
| HINTS | Nudges that point at where to think, not what to type |

## How verification works

The model must also produce a hidden reference solution ending in the same
acceptance checks the challenge gives you. The pipeline executes it in a
container (see [containers.md](containers.md)):

1. If the checks pass, the challenge is saved. The reference solution is
   discarded - it exists only as proof the challenge is correct and
   solvable.
2. If they fail (local models miscompute expected values surprisingly
   often), the failure output goes back to the model for ONE repair pass.
3. If the repair also fails, generation starts fresh - re-repairing
   anchors the model to its own broken output. Up to 4 attempts total.
4. If no container engine is available, the challenge saves with a loud
   `UNVERIFIED` warning instead.

Format drift (the model breaking the EXERCISE/CONTENT/SOLUTION reply
format) also counts as a failed attempt and retries automatically; after
4 failed attempts the run errors out - just re-run it.

## Good to know

- **The name is the model's choice** - watch the streamed output for the
  `EXERCISE:` line to learn the folder name.
- **Topic phrasing matters.** A precise topic (`"generators and yield"`)
  produces a more focused challenge than a vague one (`"something fun"`).
- SQL challenges demand portable SQL (SQLite + MySQL compatible) and are
  verified through Python's stdlib `sqlite3` in the python container.

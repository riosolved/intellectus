# Adding a language

Adding a language is a deliberate, manual act - you author its definition
and integration yourself. This is the checklist that makes it repeatable.

## The shape: three seams plus a registry line

A supported language is exactly one file at each of three seams, plus one
registry line:

| Seam | File | Answers |
|------|------|---------|
| Definition | `atk/languages/<name>.py` | What to generate and how to review it |
| Execution | `atk/runtime/runners/<name>.py` | Which image, which command |
| Environment | `atk/runtime/containerfiles/<name>.Containerfile` | What the container needs installed |
| Registry | one line in `atk/languages/__init__.py` | Makes the CLI aware of it |

Adding Go someday means creating exactly one file at each seam plus that
registry line - and each existing file is small enough to hold in your
head while you copy its pattern (`runners/cpp.py` is ~20 lines). The
steps below walk the seams in order.

## 1. Author the language module

Copy `atk/languages/python.py` (the annotated reference) to
`atk/languages/<name>.py` and fill in **every** field:

| Field | What it controls |
|-------|------------------|
| `name` | Display name used in prompts ("Python", "C++") |
| `directory` | Where exercises live: `interests/<lang>/challenges` |
| `extensions` | File suffixes that resolve to this language (`atk run file.ext`) |
| `challenge_file` / `code_file` | File names inside an exercise folder |
| `reviewer` | The review persona ("senior X engineer") |
| `challenge_wrapper` | How the challenge text stays a valid source file (docstring, block comment) |
| `difficulty_guide` | What beginner/medium/hard mean for this language |
| `edge_rule` | What a "failure path" looks like here |
| `acceptance_title` / `acceptance_spec` | The acceptance-criteria section (asserts, expected rows...) |
| `extra_rules` | Language-specific generation rules (dialect, std version) |
| `solution_spec` / `solution_suffix` | What the hidden reference solution is and what file type verifies it |
| `run_solution` | How to execute the reference solution (verification) |
| `run_code` | How to execute the student's solution (run/review) |
| `checks_spec` | What "checks you should add" means in a review |

## 2. Register its container

See [containers.md](containers.md) for the full rules. In short:

1. Write `atk/runtime/containerfiles/<name>.Containerfile` - alpine base
   (mandatory), declaring exactly the dependencies the language needs.
2. Add `atk/runtime/runners/<name>.py` following `runners/cpp.py` as
   the pattern; image tag `atk-<name>`.
3. The image builds automatically the first time it is needed.

A language that cannot be executed directly (see SQL) can verify through
another language's runner and use `skip_run` for student code.

## 3. Register the module

In `atk/languages/__init__.py`: import your module, add one entry to
`LANGUAGES`. The CLI's `--language` choices and extension resolution pick
it up from there.

## 4. Create its home

```
interests/<lang>/
`-- challenges/        <- generated exercises land here
```

## 5. Prove the loop

```
atk challenge --language <name> --topic "something small" --difficulty beginner
atk run interests/<lang>/challenges/<generated>/<code file>
atk review interests/<lang>/challenges/<generated>/<code file>
```

The generation must end in `Saved challenge to ...` **without** an
UNVERIFIED warning - if verification can't run, fix the runtime before
calling the language supported.

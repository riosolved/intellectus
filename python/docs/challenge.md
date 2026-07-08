# challenge — Generate a coding challenge

Asks the local model to invent a Python coding challenge for a given topic and
difficulty, then saves it as a ready-to-open `.py` file. This is step 1 of the
loop; see [../README.md](../README.md) for the full picture.

## Command

Run from the **repo root** (`intellectus/`):

```bash
.venv/Scripts/python.exe -m system.skills.challenge --topic "generators" --difficulty "medium"
```

Both flags are required:

| Flag | Meaning | Example values |
|------|---------|----------------|
| `--topic` | The language feature or theme to drill | `generators`, `decorators`, `dunder methods`, `recursion` |
| `--difficulty` | How hard it should be | `beginner`, `medium`, `hard` |

## Output

The model invents a whimsical two-word name and writes the challenge to:

```
python/<generated_name>/challenge.py
```

The challenge is saved as Python comments, so the file opens cleanly and you
can start writing your solution right below it — though by convention your
solution goes in a sibling `code.py`.

## How it works

1. Builds a prompt embedding your `--topic` and `--difficulty`.
2. Sends it to Ollama via `ask()` (`system/llm.py`), streaming the reply to
   your terminal so you can watch it generate.
3. Splits the reply into its `EXERCISE:` (the name) and `CONTENT:` (the task)
   sections.
4. Creates `python/<name>/` and writes `challenge.py` as UTF-8.

## Good to know

- **The name is the model's choice**, not yours — you won't know the folder
  name until it finishes. Watch the streamed output for the `EXERCISE:` line.
- **Format sensitivity:** parsing relies on the model returning the exact
  `EXERCISE:` / `CONTENT:` headers. If a run ever errors on unpacking, the
  model drifted from the format — just re-run it.
- **Topic phrasing matters.** A precise topic (`"generators and yield"`)
  produces a more focused challenge than a vague one (`"something fun"`).

## Next step

Once you've solved it in `python/<name>/code.py`, run the
[review](review.md) skill to get feedback and a `PASS` / `FAIL`.

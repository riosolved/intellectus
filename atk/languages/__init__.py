"""The language registry - one module per supported language.

Adding a language is a deliberate, manual act:
1. Copy python.py (the annotated reference) to <name>.py and fill in
   every field.
2. Add a runner module at runtime/runners/<name>.py if the language needs a new
   container image.
3. Import the module below and add its LANGUAGE to the registry.
4. Follow the full checklist in documentation/adding-a-language.md.
"""

from pathlib import Path

from atk.languages import cpp, python, sql

LANGUAGES = {
    "python": python.LANGUAGE,
    "c++": cpp.LANGUAGE,
    "sql": sql.LANGUAGE,
}


def by_path(path: Path) -> tuple[str, dict]:
    """Resolve which language owns a file from its extension."""
    for key, language in LANGUAGES.items():
        if path.suffix in language["extensions"]:
            return key, language

    supported = sorted(ext for lang in LANGUAGES.values() for ext in lang["extensions"])
    raise ValueError(f"No supported language uses '{path.suffix}' files (known: {', '.join(supported)})")

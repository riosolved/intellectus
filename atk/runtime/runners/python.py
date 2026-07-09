"""How Python code executes: the atk-python image, `python3 <file>`.

Python is also the runtime's workhorse: SQL challenges verify through
run_python (a sqlite3 script), and per-exercise dependencies bake into
images derived from IMAGE.
"""

from atk.runtime.engine import ENGINE
from atk.runtime.images import ensure_requirements_image
from atk.runtime.sandbox import run_in_container

IMAGE = "atk-python"


def run_python(path) -> tuple[bool | None, str]:
    return run_in_container(IMAGE, ["python3", f"/work/{path.name}"], path)


def run_python_with_requirements(path) -> tuple[bool | None, str]:
    """Run a Python file; if a requirements.txt sits beside it, the
    dependencies are baked into a derived image first (once per
    requirements change, not once per run), so the run stays
    network-free."""
    requirements = path.parent / "requirements.txt"

    if not requirements.exists() or ENGINE is None:
        return run_python(path)

    image, error = ensure_requirements_image(requirements, IMAGE)

    if error is not None:
        return None, error + " Code was not executed."

    return run_in_container(image, ["python3", f"/work/{path.name}"], path)

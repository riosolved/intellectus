"""Layer 2 - images: frozen filesystems built from recipes.

An image is the result of executing a Containerfile once: a snapshot
holding one language's toolchain and nothing else. Containers are then
disposable instances of that snapshot - the image never changes at run
time, which is what makes every run start from the same known state.

Two kinds of image exist here:

1. Registered images (atk-python, atk-cpp) - one Containerfile per
   language in containerfiles/, exactly `FROM alpine:<version>` plus the
   language's toolchain via apk. Built automatically on first use.

2. Derived dependency images (atk-python-deps-<hash>) - when an exercise
   declares a requirements.txt, its packages are baked into an image
   layered on top of atk-python. The tag is a hash of the file's
   contents, so the bake happens once per requirements change, never
   once per run - and the run itself can stay network-free.
"""

import hashlib
import shutil
import tempfile
from pathlib import Path

from atk.runtime.engine import ENGINE, run_command

CONTAINERFILES = Path(__file__).resolve().parent / "containerfiles"

_present: set[str] = set()  # images confirmed present this process


def ensure_image(image: str) -> str | None:
    """Build a registered image from its Containerfile if it is missing.
    Returns None when the image is ready, or an error message."""
    if ENGINE is None:
        return "nerdctl (containerd) not found on PATH."

    if image in _present:
        return None

    exists_ok, existing = run_command([ENGINE, "images", "-q", image])

    if exists_ok and existing not in ("", "(no output)"):
        _present.add(image)
        return None

    containerfile = CONTAINERFILES / f"{image.removeprefix('atk-')}.Containerfile"

    if not containerfile.exists():
        return f"No Containerfile registered for {image} (expected {containerfile})."

    print(f"Building {image} from {containerfile.name} (first use)...")

    built_ok, build_output = run_command(
        [ENGINE, "build", "-t", image, "-f", str(containerfile), str(CONTAINERFILES)],
        timeout=600,
    )

    if not built_ok:
        return f"Failed to build {image}:\n{build_output}"

    _present.add(image)
    return None


def ensure_requirements_image(requirements: Path, base_image: str) -> tuple[str | None, str | None]:
    """Bake an exercise's requirements.txt into an image derived from
    base_image, tagged with the file's content hash so it is built once
    and reused until the requirements change.
    Returns (image, None) on success or (None, error)."""
    digest = hashlib.sha256(requirements.read_bytes()).hexdigest()[:12]
    image = f"{base_image}-deps-{digest}"

    if image in _present:
        return image, None

    exists_ok, existing = run_command([ENGINE, "images", "-q", image])

    if exists_ok and existing not in ("", "(no output)"):
        _present.add(image)
        return image, None

    base_error = ensure_image(base_image)

    if base_error is not None:
        return None, base_error

    print(f"Baking requirements.txt into {image} (built once per requirements change)...")

    with tempfile.TemporaryDirectory() as context:
        shutil.copy(requirements, Path(context) / "requirements.txt")

        containerfile = Path(context) / "Containerfile"
        containerfile.write_text(
            f"FROM {base_image}\n"
            "COPY requirements.txt /tmp/requirements.txt\n"
            "RUN pip install --no-cache-dir --break-system-packages -r /tmp/requirements.txt\n",
            encoding="utf-8",
        )

        built_ok, build_output = run_command(
            [ENGINE, "build", "-t", image, "-f", str(containerfile), context],
            timeout=600,
        )

    if not built_ok:
        return None, f"Failed to build {image}:\n{build_output}"

    _present.add(image)
    return image, None

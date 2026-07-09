"""Layer 3 - the sandbox: the cage every run lives in.

One function runs one file inside one throwaway container. The rules are
few and absolute:

- The file's folder is mounted READ-ONLY at /work: the code can see
  itself and its neighbors, but cannot modify anything on the host.
- --network none by default: the code cannot reach the internet, the
  host, or the LLM. (The only exception is image builds, which happen in
  images.py, not here.)
- --rm: the container is deleted the moment the process exits. Nothing
  a run does survives into the next run - which is why runs are
  reproducible.

The only channels back out are the exit code and stdout/stderr - the
same discipline CI systems enforce.
"""

from atk.runtime.engine import ENGINE, run_command
from atk.runtime.images import ensure_image


def run_in_container(image: str, command: list[str], path, timeout: int = 120, network: bool = False) -> tuple[bool | None, str]:
    """Execute `command` in a fresh container of `image`, with `path`'s
    folder mounted read-only at /work. Returns (ran_ok, output) where
    ran_ok is None when execution was impossible (no engine, build
    failure, engine stopped)."""
    if ENGINE is None:
        return None, "nerdctl (containerd) not found on PATH - code was not executed."

    build_error = ensure_image(image)

    if build_error is not None:
        return None, build_error + " Code was not executed."

    ran_ok, output = run_command(
        [
            ENGINE, "run", "--rm",
            *([] if network else ["--network", "none"]),
            "-v", f"{path.resolve().parent}:/work:ro",
            image,
            *command,
        ],
        timeout=timeout,
    )

    if ran_ok is False and ("error during connect" in output or "Cannot connect" in output or "cannot connect" in output):
        return None, f"The {ENGINE} engine is not running - code was not executed."

    return ran_ok, output

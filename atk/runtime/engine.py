"""Layer 1 - the engine: how the toolkit talks to containerd.

There is no SDK in play. The toolkit shells out to nerdctl (containerd's
docker-compatible CLI) exactly as you would in a terminal, and reads back
the two things any process gives you: an exit code and its output. Every
other module in the runtime is built on that single primitive.

The engine is containerd via nerdctl, and nothing else is auto-detected.
The one escape hatch is the user explicitly setting ATK_CONTAINER_ENGINE
to another CLI that accepts the same build/run flags (docker, podman).
ENGINE is None when no engine is available - callers treat that as
"code cannot be executed", never as an error to hide.
"""

import os
import shutil
import subprocess

ENGINE = os.environ.get("ATK_CONTAINER_ENGINE") or ("nerdctl" if shutil.which("nerdctl") else None)


def run_command(command: list[str], timeout: int = 30) -> tuple[bool, str]:
    """Run one CLI command; return (ran_ok, combined output)."""
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
    except subprocess.TimeoutExpired:
        return False, f"Timed out after {timeout}s (possible infinite loop)."

    ran_ok = result.returncode == 0
    output = (result.stdout + result.stderr).strip() or "(no output)"
    return ran_ok, output

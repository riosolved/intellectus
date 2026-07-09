"""How C++ code executes: the atk-cpp image, compile then run.

Two steps in one container: g++ compiles the mounted file, and the
binary runs immediately. /work is read-only, so the binary goes to the
container's /tmp and dies with it.
"""

from atk.runtime.sandbox import run_in_container

IMAGE = "atk-cpp"


def run_cpp(path) -> tuple[bool | None, str]:
    return run_in_container(
        IMAGE,
        ["sh", "-c", f"g++ -std=c++17 /work/{path.name} -o /tmp/app && /tmp/app"],
        path,
    )

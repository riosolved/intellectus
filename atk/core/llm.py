import requests
import json

OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
MODEL = "qwen3-coder:30b"

def ask(prompt: str, options: dict | None = None) -> str:
    """
    Send a prompt to the Ollama API and return the response.

    Args:
        prompt (str): The prompt to send to the model.
        options (dict): Optional Ollama generation options, e.g.
            {"temperature": 0, "seed": 42} for a reproducible answer.
    """
    response = requests.post(
        OLLAMA_ENDPOINT,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False,
            "options": options or {},
        }
    )

    response.raise_for_status()

    chunks = []

    for line in response.iter_lines():
        if not line:
            continue

        chunk = json.loads(line)["response"]

        print(chunk, end="", flush=True) # live print to console

        chunks.append(chunk)

    print() # print a newline after the response is complete

    return "".join(chunks)

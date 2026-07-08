from system.llm import ask
from pathlib import Path
import argparse

def generate(topic: str, difficulty: str) -> str:
    prompt = f"""
        You are an expert Python programming teacher responsible for creating coding challenges.

        Create a single Python coding challenge based on:

        Topic:
        {topic}

        Difficulty:
        {difficulty}

        Rules:
        - Do not provide the solution.
        - Do not include implementation code.
        - The challenge should be clear, concise, and engaging.
        - The challenge should be appropriate for the specified difficulty.
        - The challenge should be written as Python comments so the output can be saved directly as a `.py` file.

        Exercise Rules:
        - Generate a creative snake_case exercise.
        - The exercise should be 2 words.
        - Do not describe the challenge directly.
        - Use names similar to:
        - golden_sun
        - salty_walrus
        - crimson_forest
        - silent_mountain

        Return ONLY this format:

        EXERCISE:
        <exercise>

        CONTENT:
        <python comments containing the challenge description>
    """

    response = ask(prompt)

    section_for_exercise, section_for_content = response.split("CONTENT:\n", 1)

    exercise = section_for_exercise.split("EXERCISE:\n", 1)[1].strip()
    content = section_for_content.strip()

    directory = Path(f"python/{exercise}")
    directory.mkdir(parents=True, exist_ok=True)

    file = directory / "challenge.py"
    file.write_text(content, encoding="utf-8")

def main():
    parsers = {
        "arguments": argparse.ArgumentParser()
    }

    parsers["arguments"].add_argument("--topic", required=True)
    parsers["arguments"].add_argument("--difficulty", required=True)

    arguments = parsers["arguments"].parse_args()

    generate(
        arguments.topic,
        arguments.difficulty
    )


main()

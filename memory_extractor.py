from memory import remember


def extract_memory(command: str):
    command = command.lower().strip()

    if command.startswith("my name is "):
        name = command.replace("my name is", "").strip()
        remember("my name", name)

    elif command.startswith("i live in "):
        city = command.replace("i live in", "").strip()
        remember("city", city)

    elif command.startswith("my favorite language is "):
        language = command.replace(
            "my favorite language is", ""
        ).strip()
        remember("favorite language", language)
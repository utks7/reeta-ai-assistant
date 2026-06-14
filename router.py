def detect_tool(command: str):

    command = command.lower()

    if "time" in command:
        return "tell_time"

    if "joke" in command:
        return "tell_joke"

    if "youtube" in command:
        return "open_youtube"

    if "search" in command:
        return "search_google"

    if command.startswith("open "):
        return "open_application"

    return "chat"
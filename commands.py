from memory_extractor import extract_memory

from brain import ask_ai
from memory import (
    remember,
    recall,
    get_all_memories,
    forget
)
from voice import speak

from actions.utility_actions import (
    tell_time,
    tell_joke,
    tell_date
)

from actions.web_actions import (
    open_youtube,
    search_google
)

from actions.knowledge_actions import (
    tell_about
)

from actions.app_actions import (
    open_application
)


def recall_information(command):

    try:

        key = command.replace(
            "what is",
            ""
        ).strip()

        value = recall(key)

        if value:

            speak(
                f"{key} is {value}"
            )

        else:

            speak(
                f"I don't remember {key}"
            )

    except Exception:

        speak(
            "Sorry Boss"
        )


def who_am_i():

    name = recall("my name")

    if name:

        speak(
            f"Your name is {name}"
        )

    else:

        speak(
            "I don't know your name yet."
        )


def show_memories():

    memories = get_all_memories()

    if not memories:

        speak(
            "I don't remember anything yet."
        )

        return

    memory_text = []

    for key, value in memories.items():

        memory_text.append(
            f"{key} is {value}"
        )

    speak(
        ". ".join(memory_text)
    )


def forget_information(command):

    key = command.replace(
        "forget",
        ""
    ).strip()

    success = forget(key)

    if success:

        speak(
            f"I forgot {key}"
        )

    else:

        speak(
            f"I don't remember {key}"
        )


def remember_information(command):

    try:

        text = command.replace(
            "remember",
            ""
        ).strip()

        key, value = text.split(" is ", 1)

        key = key.strip()
        value = value.strip()

        remember(key, value)

        speak(
            f"I will remember that {key} is {value}"
        )

    except Exception:

        speak(
            "Please say it like: remember favorite language is Python"
        )


def split_commands(command: str):

    separators = [
        " and ",
        " then ",
        ","
    ]

    commands = [command]

    for sep in separators:

        temp = []

        for cmd in commands:

            temp.extend(
                cmd.split(sep)
            )

        commands = temp

    return [

        cmd.strip()

        for cmd in commands

        if cmd.strip()

    ]


def handle_command(command):
    extract_memory(command)
    command = command.lower().strip()

    command_list = split_commands(command)
    # Auto remember user's name
    if command.startswith("my name is "):
        name = command.replace("my name is", "").strip()
        remember("my name", name)
        speak(f"Nice to meet you, {name}. I'll remember your name.")
        return
    
    if command.startswith("my favorite language is "):
        lang = command.replace("my favorite language is", "").strip()
        remember("favorite language", lang)
        speak(f"Got it Boss. I'll remember that your favorite language is {lang}.")
        return
    
    if command.startswith("i live in "):
        city = command.replace("i live in", "").strip()
        remember("city", city)
        speak(f"Okay Boss. I'll remember that you live in {city}.")
        return
    for cmd in command_list:

        if "time" in cmd:

            tell_time()

        elif "open youtube" in cmd or "youtube" in cmd:

            open_youtube()

        elif "joke" in cmd:

            tell_joke()

        elif "tell me about" in cmd:

            tell_about(cmd)

        elif "search" in cmd:

            search_google(cmd)

        elif cmd.startswith("open "):

            open_application(cmd)

        elif cmd.startswith("remember"):

            remember_information(cmd)

        elif cmd.startswith("what is"):

            recall_information(cmd)

        elif "who am i" in cmd:

            who_am_i()

        elif "what do you remember about me" in cmd:

            show_memories()

        elif cmd.startswith("forget"):

            forget_information(cmd)

        elif "date" in cmd or "today" in cmd:
            
            speak(tell_date())

        elif any(word in cmd for word in ["hello", "hi", "good morning", "good evening"]):
            speak("Hello Boss, how can I help you today?")


        elif cmd == "help" or "what can you do" in cmd:

            speak(
                "Boss, I can tell time and date, tell jokes, "
                "search Google, open YouTube, open applications, "
                "remember information, forget memories, recall saved facts, "
                "answer questions using AI, and handle multiple commands."
            )


        elif "version" in cmd:

            speak(
                "I am Reeta Version 1.0, your personal AI voice assistant created by Utkarsh."
            )

        elif cmd == "ping":
            speak("I'm online and ready to help, Boss.")


        elif cmd in ["exit", "quit", "shutdown reeta"]:

            speak("Goodbye Boss. See you soon.")
            raise SystemExit

        else:

            response = ask_ai(cmd)

            speak(response)
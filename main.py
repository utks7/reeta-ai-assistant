from datetime import datetime

from voice import speak, listen
from commands import handle_command

from config import (
    WAKE_WORDS,
    SLEEP_WORDS,
    ASSISTANT_NAME
)


def get_greeting():
    hour = datetime.now().hour

    if hour < 12:
        return "Good morning"
    elif hour < 17:
        return "Good afternoon"
    else:
        return "Good evening"


startup_message = (
    f"{get_greeting()}, Boss. "
    f"{ASSISTANT_NAME} is online and ready to assist you."
)

speak(startup_message)

active_mode = False

while True:

    if not active_mode:

        wake_command = listen()

        if not wake_command:
            continue

        if any(word in wake_command for word in WAKE_WORDS):

            speak("Yes Boss")
            active_mode = True

    else:

        command = listen()

        if not command:
            continue

        if any(word in command for word in SLEEP_WORDS):

            speak("Going to sleep Boss")
            active_mode = False
            continue

        handle_command(command)
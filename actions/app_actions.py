from voice import speak

import os


def open_application(command):

    app_name = command.replace(
        "open",
        ""
    ).strip()

    if not app_name:
        speak(
            "Which application should I open?"
        )

        return

    speak(f"Opening {app_name}")

    os.system(f"start {app_name}")
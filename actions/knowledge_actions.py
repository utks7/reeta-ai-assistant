from voice import speak

import wikipedia


def tell_about(command):

    topic = command.replace(
        "tell me about",
        ""
    ).strip()

    if not topic:
        speak("What would you like to know about?")
        return

    try:

        summary = wikipedia.summary(
            topic,
            sentences=2
        )

        speak(summary)

    except wikipedia.exceptions.PageError:

        speak(
            "Sorry Boss, I could not find information about that."
        )

    except Exception:

        speak(
            "Sorry Boss, something went wrong."
        )
from voice import speak

import webbrowser
import pywhatkit as kit


def open_youtube():

    speak("Opening YouTube")

    webbrowser.open("https://youtube.com")


def search_google(command):

    query = command.replace("search", "").strip()

    if not query:
        speak("What would you like me to search?")
        return

    speak(f"Searching for {query}")

    kit.search(query)
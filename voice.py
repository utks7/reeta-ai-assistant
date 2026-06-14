
import speech_recognition as sr
import re
import asyncio
import edge_tts
import os
from playsound import playsound

from logger import log_message

# ---------------------------------
# Voice Configuration
# ---------------------------------

VOICE_NAME = "en-US-AriaNeural"
TEMP_AUDIO_FILE = "temp_voice.mp3"

# Track speaking state
is_speaking = False


# ---------------------------------
# Text Cleaning
# ---------------------------------

def clean_for_speech(text: str) -> str:
    """
    Clean AI output before speaking.
    """

    # Remove markdown
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = re.sub(r"\*(.*?)\*", r"\1", text)
    text = re.sub(r"`(.*?)`", r"\1", text)
    text = re.sub(r"#+\s*", "", text)

    # Remove bullets
    text = text.replace("- ", "")
    text = text.replace("* ", "")

    # Replace newlines with pauses
    text = text.replace("\n", ". ")

    # Remove URLs
    text = re.sub(r"http\S+", "", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    return text.strip()


# ---------------------------------
# Edge TTS
# ---------------------------------

async def edge_speak(text: str):
    communicate = edge_tts.Communicate(
        text=text,
        voice=VOICE_NAME
    )

    await communicate.save(TEMP_AUDIO_FILE)


def stop_speaking():
    """
    Future-ready stop function.
    Currently removes pending audio if possible.
    """
    global is_speaking

    is_speaking = False

    try:
        if os.path.exists(TEMP_AUDIO_FILE):
            os.remove(TEMP_AUDIO_FILE)
    except Exception:
        pass


def speak(text: str):
    """
    Speak text using Microsoft Edge TTS.
    """

    global is_speaking

    try:

        is_speaking = True

        clean_text = clean_for_speech(text)

        print(f"Reeta: {clean_text}")

        log_message("Reeta", clean_text)

        asyncio.run(edge_speak(clean_text))

        if os.path.exists(TEMP_AUDIO_FILE):
            playsound(TEMP_AUDIO_FILE)

    except Exception as e:

        print(f"Speech Error: {e}")

    finally:

        is_speaking = False

        try:
            if os.path.exists(TEMP_AUDIO_FILE):
                os.remove(TEMP_AUDIO_FILE)
        except Exception:
            pass


# ---------------------------------
# Speech Recognition
# ---------------------------------

def listen():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("🎤 Listening...")

        recognizer.adjust_for_ambient_noise(
            source,
            duration=1
        )

        recognizer.pause_threshold = 0.8
        recognizer.energy_threshold = 200

        try:

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

        except sr.WaitTimeoutError:

            return ""

    try:

        command = recognizer.recognize_google(
            audio,
            language="en-IN"
        ).lower().strip()

        print(f"You said: {command}")

        log_message("User", command)

        return command

    except sr.UnknownValueError:

        return ""

    except sr.RequestError:

        print("Speech recognition service unavailable.")
        return ""

    except Exception as e:

        print(f"Recognition Error: {e}")
        return ""

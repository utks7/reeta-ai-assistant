import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env from project root (one level above src)
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)

ASSISTANT_NAME = "Reeta"
MAX_HISTORY = 20
AI_MODEL = "gemini-2.5-flash"

VOICE_RATE = 200

WAKE_WORDS = [
    "hey reeta",
    "hey rita",
    "hi reeta",
    "herita",
    "hi rita"
]

SLEEP_WORDS = [
    "sleep",
    "go to sleep",
    "stop listening",
    "stand by"
]

MEMORY_FILE = "memory.json"

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

print("API Loaded:", bool(GEMINI_API_KEY))
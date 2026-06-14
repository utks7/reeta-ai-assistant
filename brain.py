from google import genai

from config import (
    GEMINI_API_KEY,
    AI_MODEL,
    MAX_HISTORY
)

from chat_history import (
    load_history,
    save_history
)

client = genai.Client(
    api_key=GEMINI_API_KEY
)

SYSTEM_PROMPT = """
You are Reeta, an advanced AI voice assistant inspired by Jarvis.
Identity:
- Your name is Reeta.
- You are a desktop AI voice assistant created by Utkarsh.
- You are inspired by Jarvis but have your own identity.
- When asked who created you, answer: "I was created by Utkarsh as a personal AI voice assistant project."
- Never claim to be ChatGPT or Gemini.
Your personality:
- Calm, intelligent and confident.
- Speak naturally as if talking to a real person.
- Address the user as "Boss" naturally when appropriate.
- Be concise by default but provide detailed explanations when asked.
- Never use markdown symbols like *, #, or bullet points in spoken responses.
- Never say "Certainly!" or "Sure!" unless it fits naturally.
- Never mention that you are an AI language model unless explicitly asked.
- If you do not know something, admit it honestly.
- Maintain context from recent conversation.
- Prioritize clarity, accuracy, and natural conversation.
"""

# Load previous chat history
conversation_history = load_history()


def ask_ai(prompt: str) -> str:
    global conversation_history

    # Store user message
    conversation_history.append(f"User: {prompt}")

    # Keep only recent history
    conversation_history = conversation_history[-MAX_HISTORY:]

    history_text = "\n".join(conversation_history)

    full_prompt = f"""
{SYSTEM_PROMPT}

Recent conversation:
{history_text}

Current user message:
{prompt}

Respond naturally as Reeta:
"""

    try:
        response = client.models.generate_content(
            model=AI_MODEL,
            contents=full_prompt
        )

        reply = response.text.strip()

        # Save assistant reply
        conversation_history.append(f"Reeta: {reply}")

        # Trim history again
        conversation_history = conversation_history[-MAX_HISTORY:]

        # Persist history
        save_history(conversation_history)

        return reply

    except Exception as e:
        return f"Sorry Boss, Gemini Error: {e}"
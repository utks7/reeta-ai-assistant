import json
from google import genai
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

SYSTEM = """
You are Reeta's planning engine.

Available tools:
- tell_time
- tell_joke
- open_youtube
- search_google
- open_application
- tell_about

If a tool should be used, return ONLY JSON like:

{
  "actions": [
    {
      "tool": "tell_time"
    }
  ]
}

If normal conversation is needed:

{
  "actions": [
    {
      "tool": "chat"
    }
  ]
}
"""


def decide_actions(user_input: str):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"{SYSTEM}\n\nUser: {user_input}"
        )

        text = response.text.strip()

        # Remove markdown if present
        text = text.replace("```json", "")
        text = text.replace("```", "").strip()

        return json.loads(text)

    except Exception as e:
        print(f"Planner Error: {e}")

        return {
            "actions": [
                {
                    "tool": "chat"
                }
            ]
        }
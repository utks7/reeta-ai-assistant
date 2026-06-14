import asyncio
import edge_tts
from playsound import playsound
import os

TEXT = "Hello Boss. I am Reeta. My voice is now much more natural. i want to tell u about how lucky u are for having sister like riddhi , i must say you are very lucky to have her in your life"

async def generate():
    await edge_tts.Communicate(
        TEXT,
        voice="en-US-AriaNeural"
    ).save("temp.mp3")

asyncio.run(generate())

playsound("temp.mp3")

os.remove("temp.mp3")
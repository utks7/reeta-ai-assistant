from voice import speak
import datetime
import random
from datetime import datetime
def tell_date():
    today = datetime.now()
    return f"Today is {today.strftime('%A, %d %B %Y')}."
def tell_time():

    current_time = datetime.datetime.now().strftime("%H:%M")

    speak(f"The time is {current_time}")


def tell_joke():

    jokes = [
        "Why don't skeletons fight each other? They don't have the guts.",
        "Why did the scarecrow win an award? Because he was outstanding in his field."
    ]

    speak(random.choice(jokes))




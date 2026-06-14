import json
import os

from config import MEMORY_FILE


def load_memory():

    if not os.path.exists(MEMORY_FILE):
        return {}

    with open(MEMORY_FILE, "r") as file:
        return json.load(file)


def save_memory(memory):

    with open(MEMORY_FILE, "w") as file:
        json.dump(memory, file, indent=4)


def remember(key, value):

    memory = load_memory()

    memory[key] = value

    save_memory(memory)


def recall(key):

    memory = load_memory()

    return memory.get(key)


def get_all_memories():

    return load_memory()


def forget(key):

    memory = load_memory()

    if key in memory:

        del memory[key]

        save_memory(memory)

        return True

    return False
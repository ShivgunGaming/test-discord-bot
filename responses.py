import random

def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == "hello":
        return "Hello There"

    if p_message == "Hello There":
        return "General Kenobi"

    if p_message == "roll":
        return str(random.randInt(1, 6))


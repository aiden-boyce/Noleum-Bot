import random


def get_response(user_input: str) -> str:
    lower_input = user_input.lower()

    if lower_input == "hello":
        return "Hi!!!"

    if lower_input == "roll":
        return str(random.randint(1, 6))

    if lower_input == "help":
        return "`This is a help message you can modify.`"

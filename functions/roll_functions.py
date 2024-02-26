import random
import os


def read_lines(path: str):
    if not os.path.isfile(path):
        return None  # Return None if the file doesn't exist

    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        if not lines:
            return None  # Return None if the file is empty

        return lines


def roll() -> str:
    links = read_lines("functions/img_links.txt")
    img = random.choice(links)
    print(img)
    return img


def main():
    print(roll())


if __name__ == "__main__":
    main()

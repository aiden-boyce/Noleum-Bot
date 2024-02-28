import random
import os


def get_rand_photocard(path: str) -> list[str]:
    if not os.path.isfile(path):
        return None

    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()[1:]
        if not lines:
            return None

        # Grab valid Photo Card
        photocard = []
        while len(photocard) != 4:
            line = random.choice(lines)
            photocard = line.split(", ")

        return photocard


def roll_photocard() -> dict:
    photocard = get_rand_photocard("photocards/photocards_list.txt")
    photocard_info = {
        "id": photocard[0],
        "category": photocard[1],
        "name": photocard[2],
        "link": photocard[3].strip(),
    }
    return photocard_info


def main():
    print(roll_photocard())


if __name__ == "__main__":
    main()

from random import choice, randint
from math import ceil

PIXEL = "█"


def get_representation(sprite: list[list[str]]) -> str:
    res = ""
    for row in sprite:
        res += "".join(row) + "\n"
    return res


def get_vertical_sprite(size: int) -> list[list[str]]:
    res = []
    mid = ceil(size / 2)
    for _ in range(size):
        pixels_number = randint(0, mid)
        free_indexes = [i for i in range(mid)]
        sprite_row = [" " for _ in range(size)]
        for t in range(pixels_number - 1, -1, -1):
            fill_i = choice(free_indexes)
            sprite_row[fill_i] = PIXEL
            sprite_row[-fill_i - 1] = PIXEL
        res.append(sprite_row)
    return res


def get_horizontal_sprite(size: int) -> list[list[str]]:
    vertical = get_vertical_sprite(size)
    return [[vertical[j][i] for j in range(size)] for i in range(size)]


def get_mixed_sprite(size: int) -> list[list[str]]:
    vertical = get_vertical_sprite(size)
    res = vertical
    for i in range(size):
        for j in range(size):
            if vertical[i][j] == PIXEL:
                res[-i - 1][j] = PIXEL
    return res


def random_generation(size: int) -> list[list[str]]:
    random_choice = randint(0, 2)
    if random_choice == 0:
        return get_vertical_sprite(size)
    if random_choice == 1:
        return get_horizontal_sprite(size)
    return get_mixed_sprite(size)


def main():
    user_size = input("Enter sprite size: ")
    try:
        user_size = int(user_size)
    except ValueError:
        print("Size must be integer.")
        return
    if not (0 < user_size <= 1000):
        print("Size must be positive, max size is 1000")
        return
    user_stop = "1"
    while user_stop == "1":
        print(get_representation(random_generation(user_size)))
        user_stop = input("Enter 1 to continue, any other symbol to stop: ")


if __name__ == "__main__":
    main()

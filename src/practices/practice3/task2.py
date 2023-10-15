from random import sample


def get_bulls_and_cows_current_res(current_guess, answer):
    bulls, cows = 0, 0
    for i in range(len(answer)):
        if current_guess[i] == answer[i]:
            bulls += 1
        elif current_guess[i] in answer:
            cows += 1
    return bulls, cows


def is_contains_duplicates(string):
    for symbol in string:
        if string.count(symbol) > 1:
            return True
    return False


def get_digits_count():
    digits_number = input("Введите количество загаданных цифр: ")
    while digits_number not in (str(n) for n in range(1, 10 + 1)):
        digits_number = input("Введите количество загаданных цифр (число от 1 до 10): ")
    return int(digits_number)


def generate_random_value(digits_number):
    random_val = "".join(sample("1234567890", digits_number))
    return random_val if random_val[0] != "0" else random_val[::-1]


def is_guess_valid(cur_guess, digits_number):
    return (
        cur_guess.isdigit()
        and len(cur_guess) == digits_number
        and not is_contains_duplicates(cur_guess)
    )


def game(answer_len):
    print('Чтобы закончить игру напишите "стоп"')
    random_value = generate_random_value(answer_len)
    current_guess_num = 1
    while True:
        guess = input(f"{current_guess_num}. Введите ваше предположение: ")
        if guess == "стоп":
            print(f"Вы проиграли, загаданное значение: {random_value}")
            break
        if not is_guess_valid(guess, answer_len):
            print(
                f"Введите {answer_len}-значное число, не содержащее повторяющихся цифр"
            )
            continue
        current_bulls, current_cows = get_bulls_and_cows_current_res(
            guess, random_value
        )
        if current_bulls == answer_len:
            print("Вы победили!")
            break
        print(f"Быков: {current_bulls}, коров: {current_cows}")
        current_guess_num += 1


if __name__ == "__main__":
    digits_count = get_digits_count()
    game(digits_count)

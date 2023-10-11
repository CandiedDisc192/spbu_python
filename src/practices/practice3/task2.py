from random import sample


def get_bulls_and_cows_current_res(current_guess, answer):
    bulls, cows = 0, 0
    for i in range(len(answer)):
        if current_guess[i] == answer[i]:
            bulls += 1
        elif current_guess[i] in answer:
            cows += 1
    return bulls, cows


if __name__ == "__main__":
    digits_count = int(input("Введите количество загаданных цифр (число от 1 до 10): "))
    print('Чтобы закончить игру напишите "стоп"')
    random_value = "".join(sample("1234567890", digits_count))
    current_guess_num = 1
    while True:
        guess = input(f"{current_guess_num}. Введите ваше предположение: ")
        if guess == "стоп":
            print(f"Вы проиграли, загаданное значение: {random_value}")
            break
        if not guess.isdigit() or len(guess) != digits_count:
            print(f"Введите {digits_count}-значное число")
            continue
        current_bulls, current_cows = get_bulls_and_cows_current_res(
            guess, random_value
        )
        if current_bulls == digits_count:
            print("Вы победили!")
            break
        else:
            print(f"Быков: {current_bulls}, коров: {current_cows}")
            current_guess_num += 1

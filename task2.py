from random import sample


def get_bulls_and_cows_current_res(current_guess, answer):
    bulls_cows = [0, 0]
    for i in range(len(answer)):
        if current_guess[i] == answer[i]:
            bulls_cows[0] += 1
        elif current_guess[i] in answer:
            bulls_cows[1] += 1
    return bulls_cows


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
        current_res = get_bulls_and_cows_current_res(guess, random_value)
        current_bulls = current_res[0]
        current_cows = current_res[1]
        if current_bulls == digits_count:
            print("Вы победили!")
            break
        else:
            print(f"Быков: {current_bulls}, коров: {current_cows}")
            current_guess_num += 1
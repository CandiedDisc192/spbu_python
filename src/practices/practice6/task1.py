from math import sqrt


def is_float_number(number: str):
    number = number[1:] if number[0] == "-" else number
    return number.replace(".", "", 1).isdigit()


def is_input_valid(arguments):
    return len(arguments) == 3 and all(map(is_float_number, arguments))


def solve_quadratic_equation(a, b, c):
    if a == 0:
        raise ValueError("Lending coefficient must be non-zero")
    discriminant = b**2 - 4 * a * c
    if discriminant < 0:
        raise ArithmeticError("To find real roots discriminant must be non-negative")
    x1 = (-b + sqrt(discriminant)) / (2 * a)
    x2 = (-b - sqrt(discriminant)) / (2 * a)
    return (x1, x2) if x1 != x2 else (x1,)


def solve_linear_equation(k, b):
    if k == 0:
        raise ValueError("Slope coefficient must be non-zero")
    return -b / k


def get_solved_equation(arg1, arg2, arg3):
    if arg1 == arg2 == 0:
        raise ArithmeticError("Equation is not linear or quadratic")
    if arg1 == 0:
        return (solve_linear_equation(arg2, arg3),)
    return solve_quadratic_equation(arg1, arg2, arg3)


def main():
    raw_numbers = input("Enter three numbers separated by spaces: ").split()
    if not is_input_valid(raw_numbers):
        print('Incorrect input(follow instructions; use "." not ",").')
        return
    argument1, argument2, argument3 = (float(n) for n in raw_numbers)
    try:
        results = get_solved_equation(argument1, argument2, argument3)
    except ArithmeticError as error:
        print(f"Error during calculations: {error}")
        return
    print("Found solutions to the equation:", *results)


if __name__ == "__main__":
    main()

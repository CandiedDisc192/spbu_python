def expression(variable):
    square_of_variable = variable * variable
    return (square_of_variable + 1) * (square_of_variable + variable) + 1


if __name__ == "__main__":
    try:
        x = int(input("Calculating x^4 + x^3 + x^2 + x + 1, enter x: "))
        calculated_result = expression(x)
        print(f"{x}^4 + {x}^3 + {x}^2 + {x} + 1 = {calculated_result}")
    except ValueError:
        print("Incorrect input.")

def expression(variable):
    variable = int(variable) if int(variable) == variable else variable
    square_of_variable = variable * variable
    return (square_of_variable + 1) * (square_of_variable + variable) + 1


if __name__ == "__main__":
    try:
        x = float(input("Calculating x^4 + x^3 + x^2 + x + 1, enter x: "))
        print("{arg}^4 + {arg}^3 + {arg}^2 + {arg} + 1 = {ans}".format(arg=int(x) if int(x) == x else x,
                                                                       ans=expression(x)))
    except ValueError:
        print("Incorrect input.")

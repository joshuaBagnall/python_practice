OPERATORS = {
    "*": lambda lhs, rhs: print(lhs * rhs),
    "/": lambda lhs, rhs: print(lhs / rhs),
    "+": lambda lhs, rhs: print(lhs + rhs),
    "-": lambda lhs, rhs: print(lhs - rhs),
}


def parse_number(value):
    try:
        return float(value)
    except ValueError:
        print("Invalid Number")
    return None


def main():
    num_1 = parse_number(input("Enter first number: "))

    if num_1 is None:
        return

    operator = input("Enter operator: ")
    if operator not in OPERATORS:
        print("Invalid Operator")
        return

    num_2 = parse_number(input("Enter second number: "))

    if num_2 is None:
        return

    OPERATORS[operator](num_1, num_2)


if __name__ == "__main__":
    main()



     # if operator == "*":
    #     print(num_1 * num_2)
    #
    # elif operator == "/":
    #     print(num_1 / num_2)
    #
    # elif operator == "+":
    #     print(num_1 + num_2)
    #
    # elif operator == "-":
    #     print(num_1 - num_2)
    #
    # else:
    #     print("Invalid Operator")

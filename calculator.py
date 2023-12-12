from art import logo
from replit import clear


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


calcuations = {'+': add, '-': subtract, '*': multiply, '/': divide}


def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))
    for key in calcuations:
        print(key)

    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the second number?: "))
        calculation_function = calcuations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(
                f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: "
        ) == "y":
            num1 = answer
        else:
            should_continue = False
        clear()
        calculator()


calculator()

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


calcuations = {'+': add, '-': subtract, '*': multiply, '/': divide}


def calculator():
    print(logo)

    num1 = int(input("What's the first number?: "))
    for key in calcuations:
        print(key)

    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the second number?: "))
        calculation_function = calcuations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(
                f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: "
        ) == "y":
            num1 = answer
        else:
            should_continue = False
            clear()
            calculator()


calculator()

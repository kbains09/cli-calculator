import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def square_root(x):
    if x < 0:
        return "Error: Imaginary number"
    return math.sqrt(x)

def exponentiate(x, y):
    return x ** y

def factorial(x):
    if x < 0:
        return "Error: Factorial is not defined for negative numbers"
    if x == 0:
        return 1
    return math.factorial(x)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

while True:
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'sqrt' for square root")
    print("Enter 'exp' for exponentiation")
    print("Enter 'factorial' for factorial")
    print("Enter 'sine' for sine")
    print("Enter 'cosine' for cosine")
    print("Enter 'tangent' for tangent")
    print("Enter 'quit' to end the program")

    user_input = input(": ")

    if user_input == "quit":
        break
    elif user_input in ("add", "subtract", "multiply", "divide", "sqrt", "exp", "factorial", "sine", "cosine", "tangent"):
        if user_input in ("sqrt", "factorial", "sine", "cosine", "tangent"):
            num = float(input("Enter a number: "))
            if user_input == "sqrt":
                print("Result:", square_root(num))
            elif user_input == "factorial":
                print("Result:", factorial(num))
            elif user_input == "sine":
                print("Result:", sine(num))
            elif user_input == "cosine":
                print("Result:", cosine(num))
            elif user_input == "tangent":
                print("Result:", tangent(num))
        else:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if user_input == "add":
                print("Result:", add(num1, num2))
            elif user_input == "subtract":
                print("Result:", subtract(num1, num2))
            elif user_input == "multiply":
                print("Result:", multiply(num1, num2))
            elif user_input == "divide":
                print("Result:", divide(num1, num2))
            elif user_input == "exp":
                print("Result:", exponentiate(num1, num2))
    else:
        print("Invalid input")

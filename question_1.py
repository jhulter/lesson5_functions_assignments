# Task 1
# Task 2
# Task 3
num1 = int(input("Please enter a number: "))
action = str(input("Please enter the action you want to perform (+, -, x, /): "))
num2 = int(input("Please enter another number: "))

def add(*args):
    return num1 + num2
def subtract(*args):
    return num1 - num2
def multiply(*args):
    return num1 * num2
def divide(*args):
    return num1 / num2 if num2 else "Can't do that"

if action == "+":
    print(add(num1, num2))
elif action == "-":
    print(subtract(num1, num2))
elif action == "x":
    print(multiply(num1, num2))
elif action == "/":
    print(divide(num1, num2))



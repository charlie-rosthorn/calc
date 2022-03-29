def add():
    first_number = int(input("First number:\n"))
    second_number = int(input("Second number \n"))
    return first_number + second_number


def sub():
    first_number = int(input("First number:\n"))
    second_number = int(input("Second number \n"))
    return first_number - second_number


def mult():
    first_number = int(input("First number:\n"))
    second_number = int(input("Second number \n"))
    return first_number * second_number


def div():
    first_number = int(input("First number:\n"))
    second_number = int(input("Second number \n"))
    return first_number / second_number


def calculator():
    correct = 0
    question = input("Would you like to add, subtract, multiply, or divide two numbers?\n").strip()
    while correct == 0:
        if question == "add":
            print("Result: \n" + str(add()))
            correct += 1
        elif question == "sub":
            print("Result: \n" + str(sub()))
            correct += 1
        elif question == "div":
            print("Result: \n" + str(div()))
            correct += 1
        elif question == "mult":
            print("Result: \n" + str(mult()))
            correct += 1
        else:
            question = input("Sorry, please try again:\n").strip()

calculator()
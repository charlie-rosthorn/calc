from tkinter import *
import functools


window = Tk()

# Display

window.title("Calculator")
calculator = PhotoImage(file="calculator.png")
window.iconphoto(True, calculator)

number_input = []
number_bank = []
operator_bank = []
total = 0

# Definitions


def point():
    if "." not in number_input:
        number_input.append(".")
        display = Entry(window)
        display.insert(0, number_input)
        display.grid(row=0, column=0, columnspan=30)
    else:
        print("Cannot use two '.' in the same number input")


def plus_minus():
    if (len(number_input) == 0) or ("-" in number_input[0]):
        if "-" in number_input:
            number_input.remove("-")
            display = Entry(window)
            display.insert(0, number_input)
            display.grid(row=0, column=0, columnspan=30)
        else:
            number_input.append("-")
            display = Entry(window)
            display.insert(0, number_input)
            display.grid(row=0, column=0, columnspan=30)
    else:
        print("Please input negative indicator at start of number input")


def ce():
    number_input.pop()
    display = Entry(window)
    display.delete(0, END)
    display.grid(row=0, column=0, columnspan=30)


def c():
    number_input.clear()
    number_bank.clear()
    operator_bank.clear()
    display = Entry(window)
    display.delete(0, END)
    display.grid(row=0, column=0, columnspan=30)


def number(x):
    number_input.append(x)
    display = Entry(window)
    display.insert(0, number_input)
    display.grid(row=0, column=0, columnspan=30)


def times():
    if len(number_input) != 0:
        Entry(window).grid(row=0, column=0, columnspan=30)
        number_input_str = functools.reduce(lambda a, b: a+b, number_input)
        number_input_int = float(number_input_str)
        number_bank.append(number_input_int)
        operator_bank.append("*")
        if len(operator_bank) > 1:
            if "+" in operator_bank[0]:
                number1 = number_bank[0]
                number2 = number_bank[1]
                total = (number1 + number2)
            elif "-" in operator_bank[0]:
                number1 = number_bank[0]
                number2 = number_bank[1]
                total = (number1 - number2)
            elif "/" in operator_bank[0]:
                number1 = number_bank[0]
                number2 = number_bank[1]
                total = (number1 / number2)
            elif "*" in operator_bank[0]:
                number1 = number_bank[0]
                number2 = number_bank[1]
                total = (number1 * number2)
            number_input.clear()
            number_bank.clear()
            number_bank.append(total)
            operator_bank.pop(0)
        else:
            print(number_input_int)
            number_input.clear()
    else:
        print("Please enter a number before inputting an operation.")


def minus():
    if len(number_input) != 0:
        Entry(window).grid(row=0, column=0, columnspan=30)
        number_input_str = functools.reduce(lambda a, b: a + b, number_input)
        number_input_int = float(number_input_str)
        number_bank.append(number_input_int)
        operator_bank.append("-")
        if len(operator_bank) > 1:
            if "+" in operator_bank[0]:
                number1 = number_bank[0]
                number2 = number_bank[1]
                total = (number1 + number2)
            elif "-" in operator_bank[0]:
                number1 = number_bank[0]
                number2 = number_bank[1]
                total = (number1 - number2)
            elif "/" in operator_bank[0]:
                number1 = number_bank[0]
                number2 = number_bank[1]
                total = (number1 / number2)
            elif "*" in operator_bank[0]:
                number1 = number_bank[0]
                number2 = number_bank[1]
                total = (number1 * number2)
            number_input.clear()
            number_bank.clear()
            number_bank.append(total)
            operator_bank.pop(0)
        else:
            print(number_input_int)
            number_input.clear()
    else:
        print("Please enter a number before inputting an operation.")


def div():
    if len(number_input) != 0:
        Entry(window).grid(row=0, column=0, columnspan=30)
        number_input_str = functools.reduce(lambda a, b: a + b, number_input)
        number_input_int = float(number_input_str)
        number_bank.append(number_input_int)
        operator_bank.append("/")
        if len(operator_bank) > 1:
            if "+" in operator_bank[0]:
                number1 = number_bank[0]
                number2 = number_bank[1]
                total = (number1 + number2)
            elif "-" in operator_bank[0]:
                number1 = number_bank[0]
                number2 = number_bank[1]
                total = (number1 - number2)
            elif "/" in operator_bank[0]:
                number1 = number_bank[0]
                number2 = number_bank[1]
                total = (number1 / number2)
            elif "*" in operator_bank[0]:
                number1 = number_bank[0]
                number2 = number_bank[1]
                total = (number1 * number2)
            number_input.clear()
            number_bank.clear()
            number_bank.append(total)
            operator_bank.pop(0)
        else:
            print(number_input_int)
            number_input.clear()
    else:
        print("Please enter a number before inputting an operation.")


def plus():
    if len(number_input) != 0:
        Entry(window).grid(row=0, column=0, columnspan=30)
        number_input_str = functools.reduce(lambda a, b: a + b, number_input)
        number_input_int = float(number_input_str)
        number_bank.append(number_input_int)
        operator_bank.append("+")
        if len(operator_bank) > 1:
            if "+" in operator_bank[0]:
                number1 = number_bank[0]
                number2 = number_bank[1]
                total = (number1 + number2)
            elif "-" in operator_bank[0]:
                number1 = number_bank[0]
                number2 = number_bank[1]
                total = (number1 - number2)
            elif "/" in operator_bank[0]:
                number1 = number_bank[0]
                number2 = number_bank[1]
                total = (number1 / number2)
            elif "*" in operator_bank[0]:
                number1 = number_bank[0]
                number2 = number_bank[1]
                total = (number1 * number2)
            number_input.clear()
            number_bank.clear()
            number_bank.append(total)
            operator_bank.pop(0)
        else:
            print(number_input_int)
            number_input.clear()
    else:
        print("Please enter a number before inputting an operation.")


def equals():
    Entry(window).grid(row=0, column=0, columnspan=30)
    number_input_str = functools.reduce(lambda a, b: a + b, number_input)
    number_input_int = float(number_input_str)
    print(number_input_int)
    number_bank.append(number_input_int)
    number_input.clear()
    if "+" in operator_bank[0]:
        number1 = number_bank[0]
        number2 = number_bank[1]
        total = (number1 + number2)
    elif "-" in operator_bank[0]:
        number1 = number_bank[0]
        number2 = number_bank[1]
        total = (number1 - number2)
    elif "/" in operator_bank[0]:
        number1 = number_bank[0]
        number2 = number_bank[1]
        total = (number1 / number2)
    elif "*" in operator_bank[0]:
        number1 = number_bank[0]
        number2 = number_bank[1]
        total = (number1 * number2)
    display = Entry(window)
    display.insert(0, str(total))
    display.grid(row=0, column=0, columnspan=30)
    number_input.clear()
    number_bank.clear()
    operator_bank.clear()
    number_input.append(total)

# Widgets


display = Entry(window)
display.grid(row=0, column=0, columnspan=30)

zero_button = Button(window, text="0", command=lambda: number("0"))
zero_button.grid(row=6, column=0)
one_button = Button(window,text="1", command= lambda: number("1"))
one_button.grid(row=5, column=0)
two_button = Button(window,text="2", command= lambda: number("2"))
two_button.grid(row=5, column=1)
three_button = Button(window,text="3", command= lambda: number("3"))
three_button.grid(row=5, column=2)
four_button = Button(window,text="4", command= lambda: number("4"))
four_button.grid(row=4, column=0)
five_button = Button(window,text="5", command= lambda: number("5"))
five_button.grid(row=4, column=1)
six_button = Button(window,text="6", command= lambda: number("6"))
six_button.grid(row=4, column=2)
seven_button = Button(window,text="7", command= lambda: number("7"))
seven_button.grid(row=3, column=0)
eight_button = Button(window,text="8", command= lambda: number("8"))
eight_button.grid(row=3, column=1)
nine_button = Button(window, text="9", command= lambda: number("9"))
nine_button.grid(row=3, column=2)

point_button = Button(window,text=".", command=point)
point_button.grid(row=2, column=1)
plus_button = Button(window,text="+", command=plus)
plus_button.grid(row=6, column=1)
minus_button = Button(window,text="-", command=minus)
minus_button.grid(row=6, column=2)
times_button = Button(window,text="x", command=times)
times_button.grid(row=3, column=3)
divide_button = Button(window,text="/", command=div)
divide_button.grid(row=4, column=3)
plus_minus_button = Button(window,text="+/-", command=plus_minus)
plus_minus_button.grid(row=2, column=0)

delete_button = Button(window,text="CE", command=ce)
delete_button.grid(row=2, column=2)
restart_button = Button(window,text="C", command=c)
restart_button.grid(row=2, column=3)
enter_button = Button(window,text="=", command=equals, height=2)
enter_button.grid(row=5, column=3, rowspan=2)

window.resizable(False, False)
window.mainloop()
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
    number_input.append(".")
    display = Entry(window)
    display.insert(0, number_input)
    display.grid(row=0, column=0, columnspan=30)

def plus_minus():
    if "-" in number_input:
        number_input.pop()
        display = Entry(window)
        display.insert(0, number_input)
        display.grid(row=0, column=0, columnspan=30)
    else:
        number_input.append("-")
        display = Entry(window)
        display.insert(0, number_input)
        display.grid(row=0, column=0, columnspan=30)


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
    Entry(window).grid(row=0, column=0, columnspan=30)
    number_input_str = functools.reduce(lambda a, b: a+b, number_input)
    number_input_int = float(number_input_str)
    print(number_input_int)
    number_bank.append(number_input_int)
    number_input.clear()
    operator_bank.insert(0, "*")


def minus():
    Entry(window).grid(row=0, column=0, columnspan=30)
    number_input_str = functools.reduce(lambda a, b: a + b, number_input)
    number_input_int = float(number_input_str)
    print(number_input_int)
    number_bank.append(number_input_int)
    number_input.clear()
    operator_bank.insert(0, "-")

def div():
    Entry(window).grid(row=0, column=0, columnspan=30)
    number_input_str = functools.reduce(lambda a, b: a + b, number_input)
    number_input_int = float(number_input_str)
    print(number_input_int)
    number_bank.append(number_input_int)
    number_input.clear()
    operator_bank.insert(0, "/")


def plus():
    Entry(window).grid(row=0, column=0, columnspan=30)
    number_input_str = functools.reduce(lambda a, b: a + b, number_input)
    number_input_int = float(number_input_str)
    print(number_input_int)
    number_bank.append(number_input_int)
    number_input.clear()
    operator_bank.insert(0, "+")


def equals():
    Entry(window).grid(row=0, column=0, columnspan=30)
    number_input_str = functools.reduce(lambda a, b: a + b, number_input)
    number_input_int = float(number_input_str)
    print(number_input_int)
    number_bank.append(number_input_int)
    number_input.clear()
   # if "+" in operator_bank:
     #   minus1 = number_bank[0]
      #  minus2 = number_bank[1]
     #   total = (minus1 + minus2)
  #  elif "-" in operator_bank:
  #  minus1 = number_bank[0]    minus2 = number_bank[1]
    #    total = (minus1 - minus2)
  #  elif "/" in operator_bank:
   #     minus1 = number_bank[0]
   #     minus2 = number_bank[1]
   #     total = (minus1 / minus2)
  #  elif "*" in operator_bank:
  #      minus1 = number_bank[0]
  #      minus2 = number_bank[1]
  #      total = (minus1 * minus2)






    display = Entry(window)
    display.insert(0, str(total))
    display.grid(row=0, column=0, columnspan=30)
    number_input.clear()
    number_bank.clear()
    operator_bank.clear()
    number_input.append(total)

# Widgets

display = Entry(window).grid(row=0, column=0, columnspan=30)

zero_button = Button(window, text="0", command=lambda:number("0")).grid(row=6, column=0)
one_button = Button(window,text="1", command= lambda: number("1")).grid(row=5, column=0)
two_button = Button(window,text="2", command= lambda: number("2")).grid(row=5, column=1)
three_button = Button(window,text="3", command= lambda: number("3")).grid(row=5, column=2)
four_button = Button(window,text="4", command= lambda: number("4")).grid(row=4, column=0)
five_button = Button(window,text="5", command= lambda: number("5")).grid(row=4, column=1)
six_button = Button(window,text="6", command= lambda: number("6")).grid(row=4, column=2)
seven_button = Button(window,text="7", command= lambda: number("7")).grid(row=3, column=0)
eight_button = Button(window,text="8", command= lambda: number("8")).grid(row=3, column=1)
nine_button = Button(window, text="9", command= lambda: number("9")).grid(row=3, column=2)

point_button = Button(window,text=".", command=point).grid(row=2, column=1)
plus_button = Button(window,text="+", command=plus).grid(row=6, column=1)
minus_button = Button(window,text="-", command=minus).grid(row=6, column=2)
times_button = Button(window,text="x", command=times).grid(row=3, column=3)
divide_button = Button(window,text="/", command=div).grid(row=4, column=3)
plus_minus_button = Button(window,text="+/-", command=plus_minus).grid(row=2, column=0)

delete_button = Button(window,text="CE", command=ce).grid(row=2, column=2)
restart_button = Button(window,text="C", command=c).grid(row=2, column=3)
enter_button = Button(window,text="=", command=equals, height=2).grid(row=5, column=3, rowspan=2)

window.resizable(False, False)
window.mainloop()
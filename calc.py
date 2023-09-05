from tkinter import *

def btn_click(item):
    global expression
    if item == "/" and expression.endswith("0"):
        input_text.set("Cannot divide by zero")
        expression = ""
    elif item == "=" and expression.endswith("0.0"):
        input_text.set("math error!")
        expression= "math error!"
    elif item == "/" and expression.endswith("/0"):
        input_text.set("math error!")
        expression= "math error!"
    else:
        expression = expression + str(item)
        input_text.set(expression)



    


def btn_clear():
    global expression
    expression = ""
    input_text.set("")

def btn_equal():
    global expression
    try:
        result = str(eval(expression))
        if isinstance(result, str):
            input_text.set(result)
        else:
            input_text.set(result)
        expression = ""
    except ZeroDivisionError:
        input_text.set("math error!")
        expression = "math error!"


def clear_last_char():
    global expression
    expression = expression[:-1]
    input_text.set(expression)

def divide(num1, num2):
    if num2 == 0:
        result = "Cannot divide by zero"
    else:
        result = num1 / num2
    return result
def divide_by_zero(num1, num2):
    try:
      print  (num1 /0)
    except ZeroDivisionError:
       print ("error")




window = Tk()
window.title("Calculator")

window.configure(bg="black")

window.geometry("295x345")

expression = ""

input_text = StringVar()

input_field = Entry(window, textvariable=input_text)
input_field.place(height=150)

input_field.grid(columnspan=4, ipadx=85, ipady=20)

input_text.set("")

button_1 = Button(window, text="7",fg="orange", bg="grey", activebackground="white", height = 3, width = 9, command=lambda: btn_click(7))
button_1.grid(row=3, column=0)

button_2 = Button(window, text="8",fg="orange", bg="grey", activebackground="white", height = 3, width = 9, command=lambda: btn_click(8))
button_2.grid(row=3, column=1)

button_3 = Button(window, text="9",fg="orange", bg="grey", activebackground="white", height = 3, width = 9, command=lambda: btn_click(9))
button_3.grid(row=3, column=2)

button_4 = Button(window, text="4",fg="orange", bg="grey", activebackground="white", height = 3, width = 9, command=lambda: btn_click(4))
button_4.grid(row=4, column=0)

button_5 = Button(window, text="5",fg="orange", bg="grey", activebackground="white", height = 3, width = 9, command=lambda: btn_click(5))
button_5.grid(row=4, column=1)

button_6 = Button(window, text="6",fg="orange", bg="grey", activebackground="white", height = 3, width = 9, command=lambda: btn_click(6))
button_6.grid(row=4, column=2)

button_7 = Button(window, text="1",fg="orange", bg="grey", activebackground="white", height = 3, width = 9, command=lambda: btn_click(1))
button_7.grid(row=5, column=0)

button_8 = Button(window, text="2",fg="orange", bg="grey", activebackground="white", height = 3, width = 9, command=lambda: btn_click(2))
button_8.grid(row=5, column=1)

button_9 = Button(window, text="3",fg="orange", bg="grey", activebackground="white", height = 3, width = 9, command=lambda: btn_click(3))
button_9.grid(row=5, column=2)

dot_button = Button(window, text="." ,fg="orange", bg="grey", activebackground="white", height = 3, width = 9, command=lambda: btn_click("."))
dot_button.grid(row=6, column=0)

button_0 = Button(window, text="0",fg="orange", bg="grey", activebackground="white", height = 3, width = 9, command=lambda: btn_click(0))
button_0.grid(row=6, column=1)

clear_button = Button(window, text="Clear",fg="red", bg="grey", activebackground="white", height = 3, width=9, command=btn_clear)
clear_button.grid(row=2, column=0)

plus_button = Button(window, text="+",fg="orange", bg="grey", activebackground="white", height=3, width=9, command=lambda: btn_click("+"))
plus_button.grid(row=3, column=3)

minus_button = Button(window, text="-",fg="orange", bg="grey", activebackground="white", height=3, width=9, command=lambda: btn_click("-"))
minus_button.grid(row=4, column=3)

double_zero_button = Button(window, text="00",fg="orange", bg="grey", activebackground="white", height=3, width=9, command=lambda:btn_click("00"))
double_zero_button.grid(row=6, column=2)

equal_button = Button(window, text="=", fg="white", bg="blue", activebackground="black",height=7, width=9, command=btn_equal)
equal_button.grid(row=5, column=3, rowspan =2)

multiply_button = Button(window, text="*",fg="orange", bg="grey", activebackground="white", height=3, width=9, command=lambda: btn_click("*"))
multiply_button.grid(row=2, column=1)

divide_button = Button(window, text="/",fg="orange", bg="grey", activebackground="white", height=3, width=9, command=lambda: btn_click("/"))
divide_button.grid(row=2, column=2)

Del_button = Button(window, text="DEL" ,fg="red", bg="grey", activebackground="white",height=3, width=9, command=clear_last_char)
Del_button.grid(row=2, column=3)

window.mainloop()
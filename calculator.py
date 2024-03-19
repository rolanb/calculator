#Programmer: Rolan Belgrave
#Purpose: Simple calculator able to compute arithmetic
#Importing tkinter library for GUI development
from tkinter import *
from tkinter import ttk 

root = Tk()
root.title("Calculator")


e = Entry(root, width=40, borderwidth=4)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number): #Places clicked number on entry bar
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():  #Clears the entry bar
    e.delete(0, END)

def button_add(): #adding function
    a = e.get()
    global f_num #saves first number to operate with, to a global variable
    global math_op
    math_op = "addition"
    f_num = float(a)
    e.delete(0, END) #clears entry tab, in order to add second number to be added

def button_substract():
    a = e.get()
    global f_num #saves first number to operate with to a global variable
    global math_op
    math_op = "substract"
    f_num = float(a)
    e.delete(0, END) #clears entry tab, in order to add second number to be added

def button_multiply():
    a = e.get()
    global f_num #saves first number to operate with to a global variable
    global math_op
    math_op = "multiply"
    f_num = float(a)
    e.delete(0, END) #clears entry tab, in order to add second number to be added

def button_divide():
    a = e.get()
    global f_num #saves first number to operate with to a global variable
    global math_op
    math_op = "divide"
    f_num = float(a)
    e.delete(0, END) #clears entry tab, in order to add second number to be added

def button_equal():
    b = e.get() 
    e.delete(0, END)
    s_num = float(b) 

    if math_op == "addition":
        e.insert(0, f_num + s_num) 
    elif math_op == "substraction":
        e.insert(0, f_num - s_num)
    elif math_op == "multiply":
        e.insert(0, f_num * s_num)
    else:
        e.insert(0, f_num / s_num)

#Definitions of buttons
button_1 = Button(root, text="1", padx=40, pady=10, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=10, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=10, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=10, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=10, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=10, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=10, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=10, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=10, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=10, command=lambda: button_click(0))
button_add = Button(root, text="+", padx=39, pady=10, command= button_add)
button_equal = Button(root, text="=", padx=91, pady=10, command= button_equal)
button_clear = Button(root, text="Clear", padx=81, pady=10, command= button_clear)

button_substract = Button(root, text="-", padx=41, pady=10, command= button_substract)
button_multiply = Button(root, text="*", padx=40, pady=10, command= button_multiply)
button_divide = Button(root, text="/", padx=40, pady=10, command= button_divide)

#display buttons on screen
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_add.grid(row=5,column=0)
button_equal.grid(row=5,column=1, columnspan=2)
button_clear.grid(row=4,column=1, columnspan=2)

button_substract.grid(row=6,column=0)
button_multiply.grid(row=6,column=1)
button_divide.grid(row=6,column=2)

root.mainloop() #Executes loop that continues to display buttons and text bar after cliked.

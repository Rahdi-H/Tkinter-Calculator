from ast import Delete, operator
from tkinter import *

root = Tk()
root.title('Calculator')
root.iconbitmap('icon.png')

e = Entry(root, width=60)
e.grid(row=0, column=0, columnspan=3)

def button_click(x):
    current = str(e.get())
    e.delete(0, END)
    e.insert(0, current + x)

def operator_click(i):
    global first_number 
    first_number = e.get()
    global operatr
    operatr = i
    e.delete(0, END)

def clear_click():
    e.delete(0, END)

def equal_click():
    second_number = e.get()
    e.delete(0, END)
    global answerr
    answerr = 0
    if operatr == 'add':
        answerr = float(first_number) + float(second_number)
    if operatr == 'sub':
        answerr = float(first_number) - float(second_number)
    if operatr == 'div':
        answerr = float(first_number) / float(second_number)
    if operatr == 'mul':
        answerr = float(first_number) * float(second_number)
    e.insert(0, answerr)

button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_click('1'))
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_click('2'))
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_click('3'))
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_click('4'))
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_click('5'))
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_click('6'))
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_click('7'))
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_click('8'))
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_click('9'))
button_0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_click('0'))

button_addition = Button(root, text='+', padx=40, pady=20, command=lambda: operator_click('add'))
button_subtraction = Button(root, text="-", padx=40, pady=20, command=lambda: operator_click('sub'))
button_multiplication = Button(root,text='*', padx=40, pady=20, command=lambda: operator_click('mul'))
button_division = Button(root, text='/', padx=40, pady=20, command=lambda: operator_click('div'))
button_clear = Button(root, text='AC', padx=40, pady=20, command=clear_click)
button_equal = Button(root, text='=', padx=40, pady=20, command=equal_click)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_0.grid(row=6, columnspan=3)

button_addition.grid(row=4, column=0, columnspan=1)
button_subtraction.grid(row=4, column=1, columnspan=1)
button_multiplication.grid(row=4, column=2, columnspan=1)

button_division.grid(row=5, column=0, columnspan=1)
button_clear.grid(row=5, column=1, columnspan=1)
button_equal.grid(row=5, column=2, columnspan=1)


root.mainloop()
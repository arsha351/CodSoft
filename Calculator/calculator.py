from tkinter import *

root = Tk()
root.title("Python Calculator")
root.configure(bg='#2d2d2d')

e = Entry(root, width=16, borderwidth=5, font=('Arial', 24), bg='#2d2d2d', fg='white', justify='right')
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    elif math == "subtraction":
        e.insert(0, f_num - int(second_number))
    elif math == "multiplication":
        e.insert(0, f_num * int(second_number))
    elif math == "division":
        e.insert(0, f_num / int(second_number))
    else:
        e.insert(0, "Error")

button_config = {
    'font': ('Arial', 18),
    'width': 5,
    'height': 2,
    'bg': '#2d2d2d',
    'fg': 'white',
    'bd': 0,
}


button_special_config = button_config.copy()
button_special_config.update(bg='white', fg='black')

button_ce_config = button_config.copy()
button_ce_config.update(bg='#f28c38', fg='white')

button_1 = Button(root, text="1", command=lambda: button_click(1), **button_config)
button_2 = Button(root, text="2", command=lambda: button_click(2), **button_config)
button_3 = Button(root, text="3", command=lambda: button_click(3), **button_config)
button_4 = Button(root, text="4", command=lambda: button_click(4), **button_config)
button_5 = Button(root, text="5", command=lambda: button_click(5), **button_config)
button_6 = Button(root, text="6", command=lambda: button_click(6), **button_config)
button_7 = Button(root, text="7", command=lambda: button_click(7), **button_config)
button_8 = Button(root, text="8", command=lambda: button_click(8), **button_config)
button_9 = Button(root, text="9", command=lambda: button_click(9), **button_config)
button_0 = Button(root, text="0", command=lambda: button_click(0), **button_config)

button_add = Button(root, text="+", command=button_add, **button_special_config)
button_subtract = Button(root, text="-", command=button_subtract, **button_special_config)
button_multiply = Button(root, text="*", command=button_multiply, **button_special_config)
button_divide = Button(root, text="/", command=button_divide, **button_special_config)

button_equal = Button(root, text="=", command=button_equal, **button_special_config)
button_clear = Button(root, text="CE", command=button_clear, **button_ce_config)

# Grid layout
button_7.grid(row=1, column=0, padx=1, pady=1)
button_8.grid(row=1, column=1, padx=1, pady=1)
button_9.grid(row=1, column=2, padx=1, pady=1)
button_divide.grid(row=1, column=3, padx=1, pady=1)

button_4.grid(row=2, column=0, padx=1, pady=1)
button_5.grid(row=2, column=1, padx=1, pady=1)
button_6.grid(row=2, column=2, padx=1, pady=1)
button_multiply.grid(row=2, column=3, padx=1, pady=1)

button_1.grid(row=3, column=0, padx=1, pady=1)
button_2.grid(row=3, column=1, padx=1, pady=1)
button_3.grid(row=3, column=2, padx=1, pady=1)
button_subtract.grid(row=3, column=3, padx=1, pady=1)

button_0.grid(row=4, column=0, padx=1, pady=1)
button_clear.grid(row=4, column=1, padx=1, pady=1)
button_equal.grid(row=4, column=2, padx=1, pady=1)
button_add.grid(row=4, column=3, padx=1, pady=1)

root.mainloop()
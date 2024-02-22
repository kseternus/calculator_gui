import tkinter as tk


def update_expression(num):
    global expression
    expression += str(num)
    equation.set(expression)


def calculate():
    try:
        global expression
        result = str(eval(expression))
        equation.set(result)
        expression = ''
    except ZeroDivisionError:
        equation.set('division by zero')
        expression = ''
    except SyntaxError:
        equation.set('Error')
        expression = ''


def clear():
    global expression
    expression = ''
    equation.set('')


expression = ''

root = tk.Tk()
root.title('Calculator')
root.geometry('434x600')
root.resizable(False, False)
root.config(background='#66545e')

equation = tk.StringVar()
screen = tk.Entry(root, font='Futura 48', foreground='#ffffff', readonlybackground='#827475', justify='right',
                  borderwidth=0, textvariable=equation, state='readonly', width=12)
screen.grid(columnspan=4)

# first row of buttons 7-9 & *
button_7 = tk.Button(root, font='Futura 22', text='7', command=lambda: update_expression(7), width=5, height=2,
                     background='#827475', activebackground='#827475', foreground='#ffffff')
button_7.grid(row=1, column=0, pady=(20, 10))

button_8 = tk.Button(root, font='Futura 22', text='8', command=lambda: update_expression(8), width=5, height=2,
                     background='#827475', activebackground='#827475', foreground='#ffffff')
button_8.grid(row=1, column=1, pady=(20, 10))

button_9 = tk.Button(root, font='Futura 22', text='9', command=lambda: update_expression(9), width=5, height=2,
                     background='#827475', activebackground='#827475', foreground='#ffffff')
button_9.grid(row=1, column=2, pady=(20, 10))

button_multiplication = tk.Button(root, font='Futura 22', text='*', command=lambda: update_expression('*'), width=5,
                                  height=2, background='#a39193', activebackground='#a39193', foreground='#ffffff')
button_multiplication.grid(row=1, column=3, pady=(20, 10))

# second row 4-6 & /
button_4 = tk.Button(root, font='Futura 22', text='4', command=lambda: update_expression(4), width=5, height=2,
                     background='#827475', activebackground='#827475', foreground='#ffffff')
button_4.grid(row=2, column=0, pady=(0, 10))

button_5 = tk.Button(root, font='Futura 22', text='5', command=lambda: update_expression(5), width=5, height=2,
                     background='#827475', activebackground='#827475', foreground='#ffffff')
button_5.grid(row=2, column=1, pady=(0, 10))

button_6 = tk.Button(root, font='Futura 22', text='6', command=lambda: update_expression(6), width=5, height=2,
                     background='#827475', activebackground='#827475', foreground='#ffffff')
button_6.grid(row=2, column=2, pady=(0, 10))

button_division = tk.Button(root, font='Futura 22', text='/', command=lambda: update_expression('/'), width=5, height=2,
                            background='#a39193', activebackground='#a39193', foreground='#ffffff')
button_division.grid(row=2, column=3, pady=(0, 10))

# third row 1-3 & CE
button_1 = tk.Button(root, font='Futura 22', text='1', command=lambda: update_expression(1), width=5, height=2,
                     background='#827475', activebackground='#827475', foreground='#ffffff')
button_1.grid(row=3, column=0, pady=(0, 10))

button_2 = tk.Button(root, font='Futura 22', text='2', command=lambda: update_expression(2), width=5, height=2,
                     background='#827475', activebackground='#827475', foreground='#ffffff')
button_2.grid(row=3, column=1, pady=(0, 10))

button_3 = tk.Button(root, font='Futura 22', text='3', command=lambda: update_expression(3), width=5, height=2,
                     background='#827475', activebackground='#827475', foreground='#ffffff')
button_3.grid(row=3, column=2, pady=(0, 10))

button_subtract = tk.Button(root, font='Futura 22', text='-', command=lambda: update_expression('-'), width=5, height=2,
                            background='#a39193', activebackground='#a39193', foreground='#ffffff')
button_subtract.grid(row=3, column=3, pady=(0, 10))

# fourth row . 0 clear and -
button_decimal = tk.Button(root, font='Futura 22', text='.', command=lambda: update_expression('.'), width=5, height=2,
                           background='#a39193', activebackground='#a39193', foreground='#ffffff')
button_decimal.grid(row=4, column=0, pady=(0, 10))

button_0 = tk.Button(root, font='Futura 22', text='0', command=lambda: update_expression(0), width=5, height=2,
                     background='#827475', activebackground='#827475', foreground='#ffffff')
button_0.grid(row=4, column=1, pady=(0, 10))

button_clear = tk.Button(root, font='Futura 22', text='C', command=lambda: clear(), width=5, height=2,
                         background='#f6e0b5', activebackground='#f6e0b5', foreground='#ffffff')
button_clear.grid(row=4, column=2, pady=(0, 10))

button_add = tk.Button(root, font='Futura 22', text='+', command=lambda: update_expression('+'), width=5, height=2,
                       background='#a39193', activebackground='#a39193', foreground='#ffffff')
button_add.grid(row=4, column=3, pady=(0, 10))

# fifth row ( ) & =
button_bracket_left = tk.Button(root, font='Futura 22', text='(', command=lambda: update_expression('('), width=5,
                                height=2, background='#a39193', activebackground='#a39193', foreground='#ffffff')
button_bracket_left.grid(row=5, column=0, pady=(0, 10))

button_bracket_right = tk.Button(root, font='Futura 22', text=')', command=lambda: update_expression(')'), width=5,
                                 height=2, background='#a39193', activebackground='#a39193', foreground='#ffffff')
button_bracket_right.grid(row=5, column=1, pady=(0, 10))

button_equal = tk.Button(root, font='Futura 22', text='=', command=lambda: calculate(), width=11, height=2,
                         background='#eea990', activebackground='#eea990', foreground='#ffffff')
button_equal.grid(row=5, column=2, columnspan=2, pady=(0, 10))

root.mainloop()

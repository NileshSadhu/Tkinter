from tkinter import *

num1 = num2 = operator = None


def clear_result():
    result_label.config(text='')


def print_digit(num):
    current = result_label.cget('text')
    new = current + str(num)
    result_label.config(text=new)


def get_operator(op):
    global num1, operator
    num1 = int(result_label.cget('text'))
    operator = op
    result_label.config(text='')


def print_result():
    global num1, operator, num2
    num2 = int(result_label.cget('text'))

    if (operator == '+'):
        result_label.config(text=str(num1+num2))
    elif (operator == '-'):
        result_label.config(text=str(num1-num2))
    elif (operator == '*'):
        result_label.config(text=str(num1*num2))
    else:
        if (num2 == 0):
            result_label.config(text='Error')
        else:
            result_label.config(text=str(round(num1 / num2, 2)))


root = Tk()
root.title('Calculator')
root.geometry('305x380')
#root.resizable(0, 0)
root.config(bg='black')

result_label = Label(root, text='', bg='black', fg='white')
result_label.config(font=('arial', 30, 'bold'))
result_label.grid(row=0, column=0, columnspan=5, pady=24, padx=5, sticky='w')

btn_clear = Button(root, text='C', fg='black', bg='#fdb320',
                   width=10, height=3, command=lambda: clear_result())
btn_clear.grid(row=1, column=0)

btn_owner = Button(root, text='Nilesh',fg='black', bg='#fdb320', width=20, height=3)
btn_owner.grid(row=1, column=1, columnspan=2)

btn_mod = Button(root, text='%', fg='black', bg='#fdb320',
                 width=9, height=3, command=lambda: get_operator('%'))
btn_mod.grid(row=1, column=3)

btn_7 = Button(root, text='7', fg='black', bg='white', width=10,
               height=3, command=lambda: print_digit('7'))
btn_7.grid(row=2, column=0)

btn_8 = Button(root, text='8', fg='black', bg='white', width=10,
               height=3, command=lambda: print_digit('8'))
btn_8.grid(row=2, column=1)

btn_9 = Button(root, text='9', fg='black', bg='white', width=9,
               height=3, command=lambda: print_digit('9'))
btn_9.grid(row=2, column=2)

btn_plus = Button(root, text='+', fg='black', bg='#fdb320',
                  width=9, height=3, command=lambda: get_operator('+'))
btn_plus.grid(row=2, column=3)

btn_4 = Button(root, text='4', fg='black', bg='white', width=10,
               height=3, command=lambda: print_digit('4'))
btn_4.grid(row=3, column=0)

btn_5 = Button(root, text='5', fg='black', bg='white', width=10,
               height=3, command=lambda: print_digit('5'))
btn_5.grid(row=3, column=1)

btn_6 = Button(root, text='6', fg='black', bg='white', width=9,
               height=3, command=lambda: print_digit('6'))
btn_6.grid(row=3, column=2)

btn_pinus = Button(root, text='-', fg='black', bg='#fdb320',
                   width=9, height=3, command=lambda: get_operator('-'))
btn_pinus.grid(row=3, column=3)

btn_1 = Button(root, text='1', fg='black', bg='white', width=10,
               height=3, command=lambda: print_digit('1'))
btn_1.grid(row=4, column=0)

btn_2 = Button(root, text='2', fg='black', bg='white', width=10,
               height=3, command=lambda: print_digit('2'))
btn_2.grid(row=4, column=1)

btn_3 = Button(root, text='3', fg='black', bg='white', width=9,
               height=3, command=lambda: print_digit('3'))
btn_3.grid(row=4, column=2)

btn_mul = Button(root, text='*', fg='black', bg='#fdb320',
                 width=9, height=3, command=lambda: get_operator('*'))
btn_mul.grid(row=4, column=3)

btn_0 = Button(root, text='0', fg='black', bg='white', width=22,
               height=3, command=lambda: print_digit('0'))
btn_0.grid(row=5, column=0, columnspan=2)

btn_equal = Button(root, text='=', fg='black', bg='white',
                   width=9, height=3, command=print_result)
btn_equal.grid(row=5, column=2)

btn_div = Button(root, text='/', fg='black', bg='#fdb320',
                 width=9, height=3, command=lambda: get_operator('/'))
btn_div.grid(row=5, column=3)

root.mainloop()

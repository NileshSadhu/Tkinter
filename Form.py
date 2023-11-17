from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox

root = Tk()
root.title('Registeration')
root.geometry('380x300')
root.config(bg='lightblue')

def get_data():
    store_name = name.get()
    store_last = last.get()
    user_address = add_text.get('1.0', END)
    user_amount = amount.get()
    user_gender = gender_var.get()
    user_pay = pay.get()

    if not store_name or not store_last or not user_address or not user_amount or not user_gender or not user_pay:
        messagebox.showinfo('Error','Please Fill every box.')
        return

    print('Thanks '+ store_name + ' ' + store_last + ' from \n ' + user_address +'gender : ' + user_gender + ' for donating amount ' + user_amount + ' from banking : ' + user_pay)

    name.delete(0,END)
    last.delete(0,END)
    add_text.delete('1.0',END)
    gender_var.set('')
    pay.set('')
    amount.delete(0,END)


head_title = Label(root, text='Registeration', bg='lightblue')
head_title.config(font=('Registeration', 12, 'bold'))
head_title.grid(row=0, column=1, columnspan=3)

user_name = Label(root, text='User Name : ', bg='lightblue')
user_name.grid(row=1, column=1, padx=10)

name = Entry(root, width=30)
name.grid(row=1, column=2, padx=10, pady=5)

last_name = Label(root, text='Last Name : ', bg='lightblue')
last_name.grid(row=2, column=1, padx=10)

last = Entry(root, width=30)
last.grid(row=2, column=2, padx=10, pady=5)

address = Label(root, text='Address : ', bg='lightblue')
address.grid(row=3, column=1, padx=10)

add_text = Text(root, height=3, width=22)
add_text.grid(row=3, column=2, pady=3)

gender_var = StringVar()

gender = Label(root, text='Gender : ', bg='lightblue')
gender.grid(row=4, column=1)

gender1 = Radiobutton(root, text='Male', value='Male', bg='lightblue', padx=3, variable=gender_var)
gender1.grid(row=4, column=2)

gender2 = Radiobutton(root, text='Female', value='Female', bg='lightblue', padx=3, variable=gender_var)
gender2.grid(row=4, column=3)

payment = Label(root, text='Payment : ', bg='lightblue')
payment.grid(row=5, column=1, padx=10)

types = ['Rupay', 'MasterCard', 'Visa', 'American Express', 'CRED']
pay = Combobox(root, value=types)
pay.bind("<<Combobox Select>>")
pay.grid(row=5, column=2)

paid = Label(root, text='Amount : ', bg='lightblue')
paid.grid(row=6, column=1, padx=10)

amount = Entry(root, width=30)
amount.grid(row=6, column=2, padx=10, pady=5)

submit_btn = Button(root, text='Submit', width=8,  command=get_data)
submit_btn.grid(row=7, column=2, pady=5)

root.mainloop()
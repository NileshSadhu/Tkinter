from tkinter import *
from tkinter import messagebox
import os

root = Tk()
root.title('To-Do')
root.geometry('435x400')
root.config(bg='lightblue')

# Functions 
def AddTask():
    user_task = task_input.get()
    try:
        if len(user_task) == 0:
            print_message.config(text='Task Added None !', bg='lightblue')

        else:
            with open('task.txt', 'a') as file1:
                file1.write(user_task + '\n')

            task_input.delete(0,END)
            print_message.config(text=f'Task you added : {user_task}', bg='lightblue')

    except FileNotFoundError:
            messagebox.showinfo('Error', 'File Not Found !')

def ShowTask():
    print_task.delete('1.0', END)
    try:
        if os.path.getsize('task.txt') == 0:
            print_task.config(text='File is Empty.....')

        else:
            with open('task.txt', 'r') as file1:
                for line in file1:
                    print_task.insert(INSERT,line)


    except FileNotFoundError:
        messagebox.showinfo('Error', 'File Not Found !')

def RemoveTask():
    try:
        line_num = int(task_input.get())

        with open('task.txt', 'r') as file1:
            lines = file1.readlines()

            if 1 <= line_num <= len(lines):
                del lines[line_num- 1]

                with open('task.txt', 'w') as file2:
                    file2.writelines(lines)

                print_message.config(text='Task is deleted.')

            else:
                print_message.config(text='Line '+ str(line_num) +' not in file.')
                print_message.config(text=f'File length is : {len(lines)}')

    except FileNotFoundError:
        messagebox.showinfo('Error', 'File Not Found !')
    except ValueError:
        messagebox.showinfo('Error', 'Please enter a valid line number.')


# Task Input -->
head = Label(root, text='Task : ', bg='lightblue')
head.grid(row=1, padx=10)

task_input = Entry(root, width=50)
task_input.grid(row=1, column=1, columnspan=3)


# Button Section -->
add_task = Button(root, text='Add Task', borderwidth=3, command=AddTask)
show_task = Button(root, text='Show Task', borderwidth=3, command=ShowTask)
remove_task = Button(root, text='Remove Task', borderwidth=3, command=RemoveTask)

add_task.grid(row=2, column=1, pady=5)
show_task.grid(row=2, column=2, pady=5)
remove_task.grid(row=2, column=3, pady=5)


div1 = Label(root, text='------------------------------------------------------------------------------------', bg='lightblue')
div1.grid(row=3, pady=5, padx=5, columnspan=4)

print_message = Label(root, text='', bg='lightblue')
print_message.grid(row=4, column=0, columnspan=2)

div2 = Label(root, text='------------------------------------------------------------------------------------', bg='lightblue')
div2.grid(row=5, pady=5, padx=5, columnspan=4)

print_task = Text(root, bg='lightblue', width=40, height=10)
print_task.grid(row=6, columnspan=4, padx=5, pady=5)

root.mainloop()
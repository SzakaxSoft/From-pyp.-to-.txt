import os
import tkinter as tk
from tkinter import messagebox

def save_name():
    name = name_input.get()

    if not name:
        messagebox.showwarning('Warning', 'Please enter your name')
        return
    
    with open('save_file.txt', 'a') as file:
        file.write(name + ' and ')

    messagebox.showinfo('Succes', name + ' succesfully saved')
    name_input.delete(0, tk.END)

root = tk.Tk()
root.title('Save')
root.geometry('500x400')

name_label = tk.Label(root, text='Enter Your Name Below')
name_label.grid(row=0, column=0, sticky='nsew')

name_input = tk.Entry(root)
name_input.grid(row=1, column=0, sticky='nsew')

save_name_input = tk.Button(root,text='Save Name', command=save_name)
save_name_input.grid(row=2, column=0, sticky='nsew')

root.mainloop()
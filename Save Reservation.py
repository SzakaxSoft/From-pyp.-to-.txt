import os
import tkinter as tk
from tkinter import messagebox

def save_sale_price_weight():
    sale = add_sale_input.get()
    price = add_price_input.get()
    weight = add_weight_input.get()

    if not sale and price and weight:
        messagebox.showwarning('Error', 'Please enter valid name')
        return
    
    with open('Save_Reservation.txt', 'a') as file:
        file.write('You sold a/an ' + sale + ' for ' + price + ' for ' + weight + 'kg-s')
    
    messagebox.showinfo('Succes', 'Succesfully saved')
    add_sale_input.delete(0, tk.END)
    add_price_input.delete(0, tk.END)
    add_weight_input.delete(0, tk.END)

root = tk.Tk()
root.title('Main Menu')
root.geometry('500x400')

add_sale_label = tk.Label(root, text='Add Sale Below')
add_sale_label.grid(row=0, column=0, sticky='nsew')

add_sale_input = tk.Entry(root)
add_sale_input.grid(row=1, column=0, sticky='nsew')

add_price_label = tk.Label(root, text='Add Price Below')
add_price_label.grid(row=0, column=1, sticky='nsew')

add_price_input = tk.Entry(root)
add_price_input.grid(row=1, column=1, sticky='nsew')

add_price_button = tk.Button(root, text='Add Price', command=save_sale_price_weight)
add_price_button.grid(row=2, column=1, sticky='nsew')

add_weight_label = tk.Label(root, text='Add Weight Below')
add_weight_label.grid(row=0, column=2, sticky='nsew')

add_weight_input = tk.Entry(root)
add_weight_input.grid(row=1, column=2, sticky='nsew')

root.mainloop()

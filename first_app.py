#import
import tkinter as tk
from tkinter import messagebox

bg = 'blue'

click = 0
def button_click():
    global click
    click += 1
    lablel.config(text=f'Клики: {click}')

root = tk.Tk()

root.title('абвгдеё')

label = tk.Label(root, text='Мой первый кликер', font =('Ink Free', 30))
label.pack()
lablel = tk.Label(root, text='Клики', font =('Castellar', 30))
lablel.place(x=865,y=100)

root.geometry('1920x1080')

button = tk.Button(root, text='кликай',font=('Ink free',26),width=30,height=10, bg='skyblue', fg='black', command=button_click).place(x=650,y=350)

root.mainloop()

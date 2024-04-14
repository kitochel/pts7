import tkinter as tk
from time import*
from tkinter import ttk


class FinalProject(tk.Tk):

    color = '#c2c2c2'
    color2 = 'white'

    def __init__(self):
        super().__init__()
        self.window_settings()
        self.create_entry()
        self.create_button()
        self.create_label()
        self.solve_problem
        self.solve_bmi
        self.create_bmi()

    def window_settings(self):
        self.title('Калькулятор')
        self.resizable(False, False)
        self.configure(background=self.color)

    def create_entry(self):
        self.entry = tk.Entry(self, font=('Arial', 12), width=20, background='#545454')
        self.entry.grid(row=1, column=0, padx=15, pady=15)

    def create_button(self):
        self.button = tk.Button(self, text='=', font=('Arial', 12), width=4, command=self.solve_problem, background='#ff7b2e')
        self.button.grid(row=2, column=0, padx=15, pady=15)

    def create_label(self):
        self.labl1 = tk.Label(self, text='Калькулятор', font=('Arial', 12))
        self.labl1.grid(row=0, column=0, padx=15, pady=15)

        self.labl1 = tk.Label(self, text='ИМТ(Индекс Массы Тела)', font=('Arial', 12))
        self.labl1.grid(row=0, column=1, padx=15, pady=5)

        self.labl = tk.Label(self, text='0', font=('Arial', 12), background='white')
        self.labl.grid(row=3, column=0, padx=15, pady=15)

    def create_bmi(self):

        self.label_bmi1 = tk.Label(self, text='Введите свой вес(кг)', font=('Arial', 12))
        self.label_bmi1.grid(row=1, column=1, padx=15, pady=0)

        self.entry_bmi1 = tk.Entry(self, font=('Arial', 12), width=15, background='#545454')
        self.entry_bmi1.grid(row=2, column=1, padx=15, pady=0)

        self.label_bmi2 = tk.Label(self, text='Введите свой рост(м)', font=('Arial', 12))
        self.label_bmi2.grid(row=3, column=1, padx=15, pady=0)

        self.entry_bmi2 = tk.Entry(self, font=('Arial', 12), width=15, background='#545454')
        self.entry_bmi2.grid(row=4, column=1, padx=15, pady=5)

        self.button_bmi = tk.Button(self, text='Рассчитать', font=('Arial', 12), command=self.solve_bmi, background='#ff7b2e')
        self.button_bmi.grid(row=5, column=1, padx=15, pady=15)

        self.labl_bmi = tk.Label(self, text='0', font=('Arial', 12), background='white')
        self.labl_bmi.grid(row=6, column=1, padx=15, pady=15)

    def solve_problem(self):
        self.labl.configure(text=str(eval(self.entry.get())))

    def solve_bmi(self):
        ressult = (float(self.entry_bmi1.get()) / float(self.entry_bmi2.get()) ** int(2))
        self.labl_bmi.configure(text=round(ressult, 1))

app = FinalProject()
app.mainloop()

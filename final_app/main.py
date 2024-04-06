import tkinter
from tkinter import ttk


class FinalProject(tkinter.Tk):
    color = '#dbf4ff'

    def __init__(self):
        super().__init__()
        self.window_settings()
        self.create_label()
        self.create_buttons()
        self.create_entry()

    def window_settings(self):
        self.title('final project')
        # self.geometry('400x200')
        self.configure(background=self.color)
        self.resizable(False, False)

    def create_label(self):
        self.lbl1 = tkinter.Label(self, text='Test label', font=('Arial', 15), background=self.color)
        self.lbl1.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    def create_buttons(self):
        self.btn1 = tkinter.Button(self, text='OK', font=('Arial', 12))
        self.btn1.grid(row=2, column=0, padx=10, pady=10)

        self.btn2 = tkinter.Button(self, text='Cancel', font=('Arial', 12))
        self.btn2.grid(row=2, column=1, padx=10, pady=10)

    def create_entry(self):
        self.entry = tkinter.Entry(self, font=('Arial', 12), width=20)
        self.entry.grid(row=1, column=0, columnspan=2, padx=10, pady=10)


app = FinalProject()
app.mainloop()
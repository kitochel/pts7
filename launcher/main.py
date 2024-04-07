import tkinter as tk
import subprocess
import webbrowser
from PIL import Image, ImageTk


class LauncherApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.window_settings()
        self.setup_icons()
        self.setup_ui()

    def window_settings(self):
        self.title('Launcher App')
        # self.geometry('350x250')
        self.resizable(False, False)

    def setup_icons(self):
        self.notepad_icon = Image.open('images/notepad.png')
        self.notepad_icon = self.notepad_icon.resize((35, 35))
        self.notepad_icon_tk = ImageTk.PhotoImage(self.notepad_icon)

        self.calculator_icon = Image.open('images/calculator.png')
        self.calculator_icon = self.calculator_icon.resize((25, 35))
        self.calculator_icon_tk = ImageTk.PhotoImage(self.calculator_icon)

        self.paint_icon = Image.open('images/paint.png')
        self.paint_icon = self.paint_icon.resize((35, 35))
        self.paint_icon_tk = ImageTk.PhotoImage(self.paint_icon)

        self.browser_icon = Image.open('images/browser1.png')
        self.browser_icon = self.browser_icon.resize((35, 35))
        self.browser_icon_tk = ImageTk.PhotoImage(self.browser_icon)

        self.kitochel_icon = Image.open('images/кит.png')
        self.kitochel_icon = self.kitochel_icon.resize((35, 35))
        self.kitochel_icon_tk = ImageTk.PhotoImage(self.kitochel_icon)

    def create_button(self, text, image, action, action_args, row, column):
        button = tk.Button(self, text=text, image=image, compound='left', font=('Arial', 12), command=lambda: action(action_args))
        button.grid(row=row, column=column, padx=5, pady=5, sticky='we', ipadx=5)
        return button

    def run_program(self, program_path: str):
        subprocess.Popen(program_path)

    def open_browser(self, path: str):
        webbrowser.open(path)

    def setup_ui(self):
        apps_label = tk.Label(self, text='Приложения', font=('Arial', 16))
        apps_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        notepad_button = self.create_button(text='блокнот', image=self.notepad_icon_tk, action=self.run_program,
                                            action_args='notepad.exe', row=1, column=0)

        calc_button = self.create_button(text='калькулятор', image=self.calculator_icon_tk, action=self.run_program,
                                         action_args='calc.exe', row=1, column=1)

        paint_button = self.create_button(text='рисовалка', image=self.paint_icon_tk, action=self.run_program,
                                         action_args='mspaint.exe', row=2, column=0)

        browser_button = self.create_button(text='браузер', image=self.browser_icon_tk, action=self.open_browser,
                                          action_args='chrome.exe', row=2, column=1)

        websites_label = tk.Label(self, text='Вебсайты', font=('Arial', 16))
        websites_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        kitochel_button = self.create_button(text='канал киточела', image=self.kitochel_icon_tk, action=self.open_browser,
                                            action_args='https://www.youtube.com/@kitochel/videos', row=4, column=0)


if __name__ == '__main__':
    app = LauncherApp()
    app.mainloop()

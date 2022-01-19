import tkinter as tk
from tkinter import messagebox, LEFT, RIGHT
from tkinter.ttk import Button, Style


class DButton(Button):
    def __init__(self, root=None, **kwargs):
        super().__init__(root, **kwargs)
        super().config(command=self.command)

    def command(self):
        pass


class OKButton(DButton):
    def __init__(self, root):
        super().__init__(root, text='OK')
        self.pack(side=LEFT, padx=10)

    def command(self):
        messagebox.showinfo('our message', 'tkinter is easy to use')


class QuitButton(DButton):
    def __init__(self, root):
        Style().configure('W.TButton', foreground='red')
        super().__init__(root, text='Quit', style='W.TButton')
        self.pack(side=RIGHT, padx=10)

    def command(self):
        quit()


def build_ui():
    root = tk.Tk()
    root.geometry('200x100+300+300')
    root.title('pick one')

    slogan = OKButton(root)
    button = QuitButton(root)

    root.mainloop()


def main():
    build_ui()


if __name__ == '__main__':
    main()

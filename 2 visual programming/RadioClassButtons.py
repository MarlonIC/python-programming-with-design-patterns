from tkinter import ttk
import tkinter as tk
from tkinter import *


class ChoiceButton(tk.Radiobutton):
    gvar = None

    def __init__(self, rt, color, index, cLabel):
        super().__init__(rt, text=color, padx=20, command=self.comd, variable=ChoiceButton.gvar, value=index)
        self.pack(anchor=W)

        self.color = color
        self.cLabel = cLabel
        self.index = index

    def comd(self):
        self.cLabel.configure(fg=self.color, text=self.color)


def main():
    root = tk.Tk()
    tk.Label(root, text='Choose your favourite color:', justify=LEFT, padx=20).pack()

    cLabel = Label(root, text='color')
    ChoiceButton.gvar = IntVar()
    ChoiceButton.gvar.set(None)
    ChoiceButton(root, 'Red', 0, cLabel)
    ChoiceButton(root, 'Blue', 1, cLabel)
    ChoiceButton(root, 'Green', 2, cLabel)

    cLabel.pack()
    mainloop()


if __name__ == '__main__':
    main()

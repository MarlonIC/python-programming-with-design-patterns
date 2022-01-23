from tkinter import ttk
import tkinter as tk
from tkinter import *


class ChoiceButton(tk.Radiobutton):
    def __init__(self, rt, color, index, gvar, clabel):
        super().__init__(rt, text=color, padx=20, command=self.comd, variable=gvar, value=index)

        self.pack(anchor=W)
        self.root = rt
        self.color = color
        self.index = index
        self.var = gvar
        self.clabel = clabel

    def comd(self):
        self.clabel.configure(fg=self.color, text=self.color)


def main():
    root = tk.Tk()
    tk.Label(root, text='Choose your favourite color:', justify=LEFT, padx=20).pack()
    groupv = tk.IntVar()
    cLabel = Label(root, text='color')
    ChoiceButton(root, 'Red', 0, groupv, cLabel)
    ChoiceButton(root, 'Blue', 1, groupv, cLabel)
    ChoiceButton(root, 'Green', 2, groupv, cLabel)
    cLabel.pack()

    groupv.set(None)
    root.mainloop()


if __name__ == '__main__':
    main()

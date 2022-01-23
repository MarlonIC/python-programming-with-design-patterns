import tkinter as tk
from tkinter import *


class OKButton(Button):
    def __init__(self, root, boxes):
        super().__init__(root, text='Order')
        super().config(command=self.comd)
        self.boxes = boxes

    def comd(self):
        for box in self.boxes:
            print(box.text, box.getVar())


class Checkbox(Checkbutton):
    def __init__(self, root, btext, gvar):
        super().__init__(root, text=btext, variable=gvar)
        self.text = btext
        self.var = gvar

        if self.text == 'Pineapple':
            self.configure(state=DISABLED)

    def getVar(self):
        return self.var.get()


class InitUI:
    def __init__(self, root):
        self.names = ['Cheese', 'Pepperoni', 'Mushrooms', 'Sausage', 'Peppers', 'Pineapple']
        root.title('Pizza')
        root.geometry('200x175')

        boxes = []
        r = 0

        for name in self.names:
            var = IntVar()
            cb = Checkbox(root, name, var)
            boxes.append(cb)
            cb.grid(column=0, row=r, sticky=W)
            r += 1

        OKButton(root, boxes).grid(column=1, row=3, padx=20)
        mainloop()


def main():
    root = Tk()
    InitUI(root)


if __name__ == '__main__':
    main()

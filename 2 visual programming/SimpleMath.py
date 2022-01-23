import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *


class Builder:
    def get_sum(self):
        try:
            x_val = float(self.xEntry.get())
            y_val = float(self.yEntry.get())
            self.cLabel.configure(text='Sum =' + str(x_val + y_val))
        except:
            messagebox.showerror('Conversion error', 'Not numbers')

    def build(self):
        root = tk.Tk()
        root.geometry('350x200')
        Label(root, text='''Enter numbers to add''', justify=LEFT, fg='blue', pady=10, padx=20)\
            .grid(row=0, column=0, columnspan=2)

        Label(text='x=', fg='blue').grid(row=1, column=0)
        self.xEntry = Entry(root)
        self.xEntry.grid(row=1, column=1, padx=10)

        Label(text='y=', fg='blue').grid(row=2, column=0)
        self.yEntry = Entry(root)
        self.yEntry.grid(row=2, column=1, padx=10)

        self.okButton = Button(root, text='OK', command=self.get_sum)
        self.okButton.grid(row=3, column=0, columnspan=2)

        self.cLabel = Label(root, text='sum', fg='blue')
        self.cLabel.grid(row=4, column=0, columnspan=2)
        mainloop()


if __name__ == '__main__':
    builder = Builder()
    builder.build()

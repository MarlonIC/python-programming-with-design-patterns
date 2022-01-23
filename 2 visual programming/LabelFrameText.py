import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
from tkinter.ttk import *


def main():
    root = tk.Tk()
    root.geometry('100x250')
    style = Style()
    style.theme_use('alt')

    labelFrame = LabelFrame(root, text='State data', borderwidth=7, relief=RAISED)
    labelFrame.pack(pady=5)

    Label(labelFrame, text='State').pack()
    Label(labelFrame, text='Abbrev').pack()
    Label(labelFrame, text='Capital').pack()
    Label(labelFrame, text='Founded').pack()

    mainloop()


if __name__ == '__main__':
    main()

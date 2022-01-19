import sys
import tkinter as tk
from tkinter import Button, messagebox, LEFT, RIGHT


def disp_slogan():
    messagebox.showinfo('our message', 'tkinter is easy to use')


root = tk.Tk()
root.geometry('200x100+300+300')
slogan = Button(root, text='Hello', command=disp_slogan)
slogan.pack(side=LEFT, padx=10)

button = Button(root, text='QUIT', fg='red', command=sys.exit)
button.pack(side=RIGHT, padx=10)

root.mainloop()

import tkinter as tk
from tkinter import Frame, Label, LEFT, Entry, X


root = tk

frame1 = Frame()
frame1.pack(fill=X)

label1 = Label(frame1, text='Name', width=7)
label1.pack(side=LEFT, padx=5, pady=5)
entry1 = Entry(frame1)
entry1.pack(fill=X, padx=5, expand=True)

frame2 = Frame()
frame2.pack(fill=X)

label2 = Label(frame2, text='Address', width=7)
label2.pack(side=LEFT, padx=5, pady=5)

entry2 = Entry(frame2)
entry2.pack(fill=X, padx=5, expand=True)

root.mainloop()

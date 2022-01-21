import tkinter as tk
from tkinter import Label, LEFT, Entry, Button, mainloop


class Builder:
    def get_name(self):
        new_name = self.name_entry.get()
        self.cLabel.configure(text='Hi ' + new_name + ' boy!')

    def build(self):
        root = tk.Tk()
        Label(root, text='What is your name?', justify=LEFT, fg='blue', pady=10, padx=20).pack()

        self.name_entry = Entry(root)
        self.name_entry.pack()

        self.ok_button = Button(root, text='ok', command=self.get_name)
        self.ok_button.pack()

        self.cLabel = Label(root, text='name', fg='blue')
        self.cLabel.pack()
        mainloop()


if __name__ == '__main__':
    builder = Builder()
    builder.build()

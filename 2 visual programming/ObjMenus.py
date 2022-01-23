import sys
import tkinter as tk
from tkinter import filedialog
from tkinter import *


class MenuBar(Menu):
    def __init__(self, root):
        super().__init__(root)
        root.config(menu=self)


class MenuCommand:
    def __init__(self, root, label):
        self.root = root
        self.label = label

    def getLabel(self):
        return self.label

    def comd(self):
        pass


class OpenCommand(MenuCommand):
    def __init__(self, root, label):
        super().__init__(root, label)

    def comd(self):
        fname = filedialog.askopenfilename(title='Select file')

        if len(fname.strip()) > 0:
            nameparts = fname.split('/')
            k = len(nameparts)

            if k > 0:
                fname = nameparts[k-1]
            self.root.title(fname)


class QuitCommand(MenuCommand):
    def __init__(self, root, label):
        super().__init__(root, label)

    def comd(self):
        sys.exit()


class DrawCircle(MenuCommand):
    def __init__(self, root, canvas, label):
        super().__init__(root, label)
        self.canvas = canvas

    def comd(self):
        self.canvas.create_oval(130, 40, 200, 110, fill='red')


class DrawSquare(MenuCommand):
    def __init__(self, root, canvas, label):
        super().__init__(root, label)
        self.canvas = canvas

    def comd(self):
        self.canvas.create_rectangle(10, 80, 110, 180, fill='blue')


class TopMenu:
    def __init__(self, root, label, menubar):
        self.mb = menubar
        self.root = root
        self.fmenu = Menu(self.mb, tearoff=0)
        self.mb.add_cascade(label=label, menu=self.fmenu)

    def addMenuItem(self, mcomd):
        self.fmenu.add_command(label=mcomd.getLabel(), command=mcomd.comd)

    def addSeparator(self):
        self.fmenu.add_separator()


def InitUI(root: Tk):
    root.title('Menu demo')
    root.geometry('300x200')
    canvas = Canvas(root)
    canvas.pack()
    menubar = MenuBar(root)

    file_menu = TopMenu(root, 'File', menubar)
    file_menu.addMenuItem(MenuCommand(root, 'New'))
    file_menu.addMenuItem(OpenCommand(root, 'Open'))
    file_menu.addSeparator()
    file_menu.addMenuItem(QuitCommand(root, 'Quit'))

    draw_menu = TopMenu(root, 'Draw', menubar)
    draw_menu.addMenuItem(DrawCircle(root, canvas, 'Circle'))
    draw_menu.addMenuItem(DrawSquare(root, canvas, 'Square'))


def main():
    root = tk.Tk()
    InitUI(root)
    mainloop()


if __name__ == '__main__':
    main()

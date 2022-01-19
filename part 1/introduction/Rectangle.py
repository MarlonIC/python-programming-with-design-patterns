from tkinter import Tk, Canvas, Frame, BOTH


class Rectangle:
    def __init__(self, canvas):
        self.canvas = canvas

    def draw(self, x, y, w, h):
        self.canvas.create_rectangle(x, y, x+w, y+h)


class Square(Rectangle):
    def __init__(self, canvas):
        super().__init__(canvas)

    def draw(self, x, y, w):
        super().draw(x, y, w, w)


def main():
    root = Tk()
    canvas = Canvas(root)
    rectangle = Rectangle(canvas)
    rectangle.draw(30, 10, 120, 80)

    square1 = Square(canvas)
    square1.draw(200, 50, 60)

    canvas.pack(expand=1)
    root.mainloop()


if __name__ == '__main__':
    main()

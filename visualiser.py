from tkinter import Tk, Canvas, Frame, BOTH


x = 100
y = 100

class defCircle(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.master.title("Visual ePapers")
        self.pack(fill=BOTH, expand=1)
        canvas = Canvas(self)
        canvas.create_oval(10, 10, x, y, outline="#1f1", fill="#1f1", width=2)
        canvas.pack(fill=BOTH, expand=1)


def main():
    root = Tk()
    ex = defCircle()
    root.geometry("600x600")
    root.mainloop()


if __name__ == '__main__':
    main()

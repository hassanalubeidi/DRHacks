from tkinter import Tk, Canvas, Frame, BOTH


size = []
y = 100
type = []
f = open('tmp.txt')
c = 0
line = f.readline()
 #! - id, @ - Title, # - Type, $ - URI, % - Size, ^ - Author
num_lines = sum(1 for line in open('tmp.txt'))

while line:
    if line.startswith("!"):
    #    print("ID: " + str(line))
        line = line[1:]
    if line.startswith("@"):
    #    print("TITLE: " + str(line))
        line = line[1:]
    if line.startswith("#"):
        line = line[1:]

        if str(line).find("article"):
            type.append("#1f1")

        if str(line).find("article"):
            type.append("#11f")

    if line.startswith("$"):
        #    print("URI: " + str(line))
            line = line[1:]
    if line.startswith("%"):
        #    print("File Size: " + str(line))
        #    x.append(line[1:] / 100)
            line = line[1:]
            j = int(line) / 1000
            size.append(j)

    if line.startswith("^"):
    #        print("Author: " + str(line))
            line = line[1:]
    line = f.readline()

f.close()

class defCircle(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.master.title("Visual ePapers")
        self.pack(fill=BOTH, expand=1)
        canvas = Canvas(self)
        print("Length of size array: " + str(len(size)))
        print("Length of type array: " + str(len(type)))
        for h in range(0, 30):
            canvas.create_oval(0 , 0 , size[h] , size[h], outline=type[0], fill=type[0], width=2)

        canvas.pack(fill=BOTH, expand=1)


def main():
    root = Tk()
    ex = defCircle()
    root.geometry("600x600")
    root.mainloop()


if __name__ == '__main__':
    main()

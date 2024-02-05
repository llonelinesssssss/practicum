from tkinter import *


class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.build()

    def build(self):
        self.formula = "0"
        self.lbl = Label(text=self.formula, font=("ChareInk Bold", 15, "bold"), bg="#fff", foreground="#000")
        self.lbl.place(x=11, y=50)

        btns = [
            "C", "⌫", "*", "=",
            "1", "2", "3", "/",
            "4", "5", "6", "+",
            "7", "8", "9", "-",
            "(", "0", ")", "X²"
        ]

        x = 10
        y = 120
        for bt in btns:
            com = lambda x=bt: self.logicalc(x)
            Button(text=bt, bg="#FFF",
                   font=("ChareInk Bold", 15),
                   command=com).place(x=x, y=y,
                                      width=90,
                                      height=50)
            x += 100
            if x > 400:
                x = 10
                y += 81

    def logicalc(self, operation):
        if operation == "C":
            self.formula = ""
        elif operation == "⌫":
            self.formula = self.formula[0:-1]
        elif operation == "X²":
            self.formula = str((eval(self.formula))**2)
        elif operation == "=":
            self.formula = str(eval(self.formula))
        else:
            if self.formula == "0":
                self.formula = ""
            self.formula += operation
        self.update()

    def update(self):
        if self.formula == "":
            self.formula = "0"
        self.lbl.configure(text=self.formula)


if __name__ == '__main__':
    root = Tk()
    root["bg"] = "#000"
    root.geometry("410x510+700+200")
    root.title("Calc by Sviridov")
    root.resizable(False, False)
    app = Main(root)
    app.pack()
    root.mainloop()
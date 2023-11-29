import tkinter as tk

class MyCalculator:
    def __init__(self):

        self.root = tk.Tk()

        self.root.geometry("300x300")
        self.root.title("My Calculator")

        self.label = tk.Label(self.root, text="hello DIP01", font=('Arial', 18))
        self.label.pack()
 
        self.button = tk.Button(self.root, text="C",height=3, width=7)
        self.button.place(x=20, y=50)

        self.button = tk.Button(self.root, text="( )",height=3, width=7)
        self.button.place(x=80, y=50)

        self.button = tk.Button(self.root, text="%",height=3, width=7)
        self.button.place(x=140, y=50)

        self.button = tk.Button(self.root, text="/",height=3, width=7)
        self.button.place(x=200, y=50)

        self.button = tk.Button(self.root, text="7",height=3, width=7)
        self.button.place(x=20, y=110)

        self.button = tk.Button(self.root, text="8",height=3, width=7)
        self.button.place(x=80, y=110)

        self.button = tk.Button(self.root, text="9",height=3, width=7)
        self.button.place(x=140, y=110)

        self.button = tk.Button(self.root, text="x",height=3, width=7)
        self.button.place(x=200, y=110)

        self.button = tk.Button(self.root, text="4",height=3, width=7)
        self.button.place(x=20, y=170)

        self.button = tk.Button(self.root, text="5",height=3, width=7)
        self.button.place(x=80, y=170)

        self.button = tk.Button(self.root, text="6",height=3, width=7)
        self.button.place(x=140, y=170)

        self.button = tk.Button(self.root, text="-",height=3, width=7)
        self.button.place(x=200, y=170)

        self.button = tk.Button(self.root, text="1",height=3, width=7)
        self.button.place(x=20, y=230)

        self.button = tk.Button(self.root, text="2",height=3, width=7)
        self.button.place(x=80, y=230)

        self.button = tk.Button(self.root, text="3",height=3, width=7)
        self.button.place(x=140, y=230)

        self.button = tk.Button(self.root, text="+",height=3, width=7)
        self.button.place(x=200, y=230)

        self.button = tk.Button(self.root, text="+/-",height=3, width=7)
        self.button.place(x=20, y=290)

        self.button = tk.Button(self.root, text="0",height=3, width=7)
        self.button.place(x=80, y=290)

        self.button = tk.Button(self.root, text=".",height=3, width=7)
        self.button.place(x=140, y=290)

        self.button = tk.Button(self.root, text="=",height=3, width=7)
        self.button.place(x=200, y=290)





        self.root.mainloop()

MyCalculator()
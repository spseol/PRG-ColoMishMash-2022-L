#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk
from tkinter import HORIZONTAL, Scale, Frame


class Application(tk.Tk):
    name = "ColorMishMash"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        # self.geometry('800x600')

        self.bind("<Escape>", self.quit)

        self.lblHlavni = tk.Label(self, text="ColorMishMash")
        self.lblHlavni.pack(anchor="w")
        self.btnQuit = tk.Button(self, text="Quit", command=self.quit)
        self.btnQuit.pack(anchor="e")

        self.frameR = tk.Frame(self)
        self.frameR.pack()
        self.frameG = tk.Frame(self)
        self.frameG.pack()
        self.frameB = tk.Frame(self)
        self.frameB.pack()

        self.varR = tk.IntVar()
        self.varR.trace("w", self.setcolor)
        self.varG = tk.IntVar(self, 0, "varG")
        self.varG.trace("w", self.setcolor)
        self.varB = tk.IntVar(self, 0, "varB")
        self.varB.trace("w", self.setcolor)

        self.lblR = tk.Label(self.frameR, text="R", fg="#ff0000")
        self.lblR.pack(side="left", anchor="s")
        self.scaleR = Scale(
            self.frameR,
            from_=0,
            to=0xFF,
            orient="horizontal",
            length=333,
            variable=self.varR,
        )
        self.scaleR.pack(side="left", anchor="s")
        self.entryR = tk.Entry(self.frameR, width=4, textvariable=self.varR)
        self.entryR.pack(side="left", anchor="s")

        self.lblG = tk.Label(self.frameG, text="G", fg="#00ff00")
        self.lblG.pack(side="left", anchor="s")
        self.scaleG = Scale(
            self.frameG,
            from_=0,
            to=0xFF,
            orient="horizontal",
            length=333,
            variable=self.varG,
        )
        self.scaleG.pack(side="left", anchor="s")
        self.entryG = tk.Entry(self.frameG, width=4, textvariable=self.varG)
        self.entryG.pack(side="left", anchor="s")

        self.lblB = tk.Label(self.frameB, text="B", fg="#0000ff")
        self.lblB.pack(side="left", anchor="s")
        self.scaleB = Scale(
            self.frameB,
            from_=0,
            to=0xFF,
            orient="horizontal",
            length=333,
            variable=self.varB,
        )
        self.scaleB.pack(side="left", anchor="s")
        self.entryB = tk.Entry(self.frameB, width=4, textvariable=self.varB)
        self.entryB.pack(side="left", anchor="s")

        self.canvasMain = tk.Canvas(self, width=333, height=222, bg="#ffffff")
        self.canvasMain.pack()

        self.varMain = tk.StringVar()
        self.entryMain = tk.Entry(
            self, width=8, textvariable=self.varMain, state="readonly"
        )
        self.entryMain.pack(anchor="e")

        self.entryR.bind("<Key>", self.callback)
        self.entryG.bind("<Key>", self.callback)
        self.entryB.bind("<Key>", self.callback)

        self.frameMemory = tk.Frame(self)
        self.frameMemory.pack()
        self.listMemory = []
        for r in range(3):
            for column in range(7):
                canvas = tk.Canvas(self.frameMemory, width=50, height=50, bg="#12abc3")
                canvas.grid(row=r, column=column)
                self.listMemory.append(canvas)
                canvas.bind('<Button-1>', self.clickHandler)
    
    def clickHandler(self, event:tk.Event):
        if self.cget('cursor') != 'pencil':
            self.config(cursor='pencil')
        else:
            self.config(cursor='')


    def callback(self, event: tk.Event):
        print(type(event))
        print(event.keycode, event.keysym, event.keysym_num, event.x, event.y)

    def setcolor(self, variabe, index, mode):
        r = self.varR.get()
        g = self.varG.get()
        b = self.varB.get()

        self.canvasMain.config(bg=f"#{r:02X}{g:02X}{b:02X}")

        # self.entryMain.delete(0,'end')
        # self.entryMain.insert(0, f'#{r:02X}{g:02X}{b:02X}')
        self.varMain.set(f"#{r:02X}{g:02X}{b:02X}")

    def quit(self, event=None):
        super().quit()

    def set(self, value):
        self.varR.set(value)


app = Application()
app.set(50)

app.mainloop()

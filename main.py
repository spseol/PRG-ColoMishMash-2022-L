#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk
from tkinter import HORIZONTAL, Scale


class Application(tk.Tk):
    name = "ColorMishMash"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        #self.geometry('800x600')

        self.bind("<Escape>", self.quit)

        self.lblHlavni = tk.Label(self, text="Hello World")
        self.lblHlavni.pack(anchor='w')
        self.btnQuit = tk.Button(self, text="Quit", command=self.quit)
        self.btnQuit.pack(anchor='e')

        self.frameR = tk.Frame(self)
        self.frameR.pack()
        self.frameG = tk.Frame(self)
        self.frameG.pack()
        self.frameB = tk.Frame(self)
        self.frameB.pack()

        self.lblR = tk.Label(self.frameR, text='R')
        self.lblR.pack(side='left', anchor='s')
        self.scaleR = Scale(self.frameR, from_=0, to=0xff, orient='horizontal', length=333)
        self.scaleR.pack(side='left', anchor='s')
        self.entryR = tk.Entry(self.frameR, width=4)
        self.entryR.pack(side='left', anchor='s')

        self.scaleG = Scale(self, from_=0, to=0xff, orient='horizontal', length=333)
        self.scaleG.pack()

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()

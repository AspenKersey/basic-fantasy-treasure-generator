#!/usr/bin/python3
# Basic Fantasy Treasure Generator
# Thorin Schmidt
# 9/13/2018

from tkinter import *
from tkinter import ttk
from tkinter import font

class Application(Frame):
    
    def __init__(self, master):
        """ initialize rthe frame"""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        
        
    def create_widgets(self):
        """ create widgets in frame """
        self.lblLair = Label(self, text = "Lair Types")
        self.lblLair.grid(row = 0, column = 0, columnspan = 3, sticky="w")
        
        ttk.Separator(self, orient=HORIZONTAL).grid(row=1, column=0,
                                                    columnspan=5, sticky="ew")
        
        self.chkBtnA = BooleanVar()
        Checkbutton(self, text = "A",
                    variable = self.chkBtnA
                    ).grid(row = 2, column = 0)
    
        self.chkBtnB = BooleanVar()
        Checkbutton(self, text = "B",
                    variable = self.chkBtnB
                    ).grid(row = 2, column = 1)
    
        self.chkBtnC = BooleanVar()
        Checkbutton(self, text = "C",
                    variable = self.chkBtnC
                    ).grid(row = 2, column = 2)
    
        self.chkBtnD = BooleanVar()
        Checkbutton(self, text = "D",
                    variable = self.chkBtnD
                    ).grid(row = 2, column = 3)
    
        self.chkBtnE = BooleanVar()
        Checkbutton(self, text = "E",
                    variable = self.chkBtnE
                    ).grid(row = 2, column = 4)
    
        
        self.chkBtnF = BooleanVar()
        Checkbutton(self, text = "F",
                    variable = self.chkBtnF
                    ).grid(row = 3, column = 0)
    
        self.chkBtnG = BooleanVar()
        Checkbutton(self, text = "G",
                    variable = self.chkBtnG
                    ).grid(row = 3, column = 1)
    
        self.chkBtnH = BooleanVar()
        Checkbutton(self, text = "H",
                    variable = self.chkBtnH
                    ).grid(row = 3, column = 2)
    
        self.chkBtnI = BooleanVar()
        Checkbutton(self, text = "I",
                    variable = self.chkBtnI
                    ).grid(row = 3, column = 3)
    
        self.chkBtnJ = BooleanVar()
        Checkbutton(self, text = "J",
                    variable = self.chkBtnJ
                    ).grid(row = 3, column = 4)
    
        
        ttk.Separator(self, orient=HORIZONTAL).grid(row=12, column=0,
                                                    columnspan=5, sticky="ew")
        
        Label(self, text="Treasure Report").grid(row=13, column=0, columnspan=5,
                                                 sticky="w")
        
        self.textBoxReport = Text(self, width = 50, height = 20, wrap = WORD)
        self.textBoxReport.grid(row=14, column =0, columnspan=5)

#main section
root = Tk()
root.title("BF Treasure Generator")
#root.geometry('500x500')
default_font = font.nametofont("TkDefaultFont")
default_font.configure(size=20)

app = Application(root)
root.mainloop()
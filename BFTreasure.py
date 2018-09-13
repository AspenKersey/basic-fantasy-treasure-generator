#!/usr/bin/python3
# Basic Fantasy Treasure Generator
# Thorin Schmidt
# 9/13/2018

from tkinter import *

class Application(Frame):
    
    def __init__(self, master):
        """ initialize rthe frame"""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        
        
    def create_widgets(self):
        """ create widgets in frame """
        self.lblLair = Label(self, text = "Lair Types")
        self.lblLair.grid(row = 0, column = 0, columnspan = 5)
        
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
                    variable = self.chkBtnA
                    ).grid(row = 2, column = 2)
    
        self.chkBtnD = BooleanVar()
        Checkbutton(self, text = "D",
                    variable = self.chkBtnA
                    ).grid(row = 2, column = 3)
    
        self.chkBtnE = BooleanVar()
        Checkbutton(self, text = "E",
                    variable = self.chkBtnA
                    ).grid(row = 2, column = 4)
    


#main section
root = Tk()
root.title("BF Treasure Generator")
root.geometry('500x500')
app = Application(root)
root.mainloop()
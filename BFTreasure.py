#!/usr/bin/python3
# Basic Fantasy Treasure Generator
# Thorin Schmidt
# 9/13/2018

from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import simpledialog
from random import randint
from TreasureType import *

class Application(Frame):
    
    def __init__(self, master):
        """ initialize rthe frame"""
        super(Application, self).__init__(master)
        self.grid()
        
        #variables
        self.cp =0
        self.sp=0
        self.ep=0
        self.gp=0
        self.pp=0
        self.multiplier=1
        
        self.create_widgets()
        
        
    def create_widgets(self):
        """ create widgets in frame """
        self.lblLair = Label(self, text = "Lair Types")
        self.lblLair.grid(row = 0, column = 0, columnspan = 3, sticky="w")
        
        self.btnLairClear = Button(self, text="Clear",
                                   command = self.clear_lair_types)
        self.btnLairClear.grid(row=0, column=6, columnspan=2)
        
        ttk.Separator(self, orient=HORIZONTAL).grid(row=1, column=0,
                                                    columnspan=8, sticky="ew")
        
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
                    ).grid(row = 2, column = 5)
    
        self.chkBtnG = BooleanVar()
        Checkbutton(self, text = "G",
                    variable = self.chkBtnG
                    ).grid(row = 2, column = 6)
    
        self.chkBtnH = BooleanVar()
        Checkbutton(self, text = "H",
                    variable = self.chkBtnH
                    ).grid(row = 2, column = 7)
    
        self.chkBtnI = BooleanVar()
        Checkbutton(self, text = "I",
                    variable = self.chkBtnI
                    ).grid(row = 3, column = 0)
    
        self.chkBtnJ = BooleanVar()
        Checkbutton(self, text = "J",
                    variable = self.chkBtnJ
                    ).grid(row = 3, column = 1)
        
        self.chkBtnK = BooleanVar()
        Checkbutton(self, text = "K",
                    variable = self.chkBtnK
                    ).grid(row = 3, column = 2)
    
        self.chkBtnL = BooleanVar()
        Checkbutton(self, text = "L",
                    variable = self.chkBtnL
                    ).grid(row = 3, column = 3)
    
        self.chkBtnM = BooleanVar()
        Checkbutton(self, text = "M",
                    variable = self.chkBtnM
                    ).grid(row = 3, column = 4)
    
        self.chkBtnN = BooleanVar()
        Checkbutton(self, text = "N",
                    variable = self.chkBtnN
                    ).grid(row = 3, column = 5)
    
        self.chkBtnO = BooleanVar()
        Checkbutton(self, text = "O",
                    variable = self.chkBtnO
                    ).grid(row = 3, column = 6)

        self.lblInd = Label(self, text = "Individual Types")
        self.lblInd.grid(row = 5, column = 0, columnspan = 3, sticky="w")
        
        self.btnIndClear = Button(self, text="Clear",
                                   command = self.clear_ind_types)
        self.btnIndClear.grid(row=5, column=6, columnspan=2)
        
        ttk.Separator(self, orient=HORIZONTAL).grid(row=6, column=0,
                                                    columnspan=8, sticky="ew")    
        
        self.chkBtnP = BooleanVar()
        Checkbutton(self, text = "P",
                    variable = self.chkBtnP
                    ).grid(row = 7, column = 0)
    
        self.chkBtnQ = BooleanVar()
        Checkbutton(self, text = "Q",
                    variable = self.chkBtnQ
                    ).grid(row = 7, column = 1)
    
        self.chkBtnR = BooleanVar()
        Checkbutton(self, text = "R",
                    variable = self.chkBtnR
                    ).grid(row = 7, column = 2)
    
        self.chkBtnS = BooleanVar()
        Checkbutton(self, text = "S",
                    variable = self.chkBtnS
                    ).grid(row = 7, column = 3)
    
        self.chkBtnT = BooleanVar()
        Checkbutton(self, text = "T",
                    variable = self.chkBtnT
                    ).grid(row = 7, column = 4)
    
        self.chkBtnU = BooleanVar()
        Checkbutton(self, text = "U",
                    variable = self.chkBtnU
                    ).grid(row = 7, column = 5)
    
        self.chkBtnV = BooleanVar()
        Checkbutton(self, text = "V",
                    variable = self.chkBtnV
                    ).grid(row = 7, column = 6)

        ttk.Separator(self, orient=HORIZONTAL).grid(row=8, column=0,
                                                    columnspan=8, sticky="ew")
        
        Label(self, text="Treasure").grid(row=13, column=0, columnspan=5,
                                                 sticky="w")
        
        self.btnGenerateReport = Button(self, text="Generate",
                                        command=self.generate_report)
        self.btnGenerateReport.grid(row=13, column=6, columnspan=2)


        self.textBoxReport = Text(self, width = 50, height = 15, wrap = WORD)
        self.textBoxReport.grid(row=14, column =0, columnspan=8)

    def clear_lair_types(self):
        """clear the lair type checkboxes"""
        self.chkBtnA.set(False)
        self.chkBtnB.set(False)
        
    def clear_ind_types(self):
        """clear the lair type checkboxes"""
        self.chkBtnP.set(0)
        self.chkBtnQ.set(0)
        
    def generate_report(self):
        """ calculate treasure and display the results"""
        message = "LAIR\n------------------------------\n"
        self.run_through_lair_treasures()

        message += "INDIVIDUAL\n------------------------------\n"
        if self.chkBtnQ.get():
            self.get_numbers("Q")
            message += "\n" + str(self.multiplier)

        message += "UNGUARDED\n------------------------------\n"
        
        self.textBoxReport.delete(0.0,END)
        self.textBoxReport.insert(0.0, message)

        
    def get_numbers(self, treasureType):
        self.multiplier = \
          simpledialog.askinteger("Input", "Type "+treasureType+" multiplier?",
                                  minvalue=1, maxvalue=99)

    def run_through_lair_treasures(self):
      lairTreasureLists = []
      self.cp =0
      self.sp =0
      self.ep =0
      self.gp =0
      self.pp =0
      
      if self.chkBtnA.get():
          lairTreasureLists.append(type_a())
      
      for list in lairTreasureLists:
        self.cp += list[0]
        self.sp += list[1]
        self.ep += list[2]
        self.gp += list[3]
        self.pp += list[4]
        
      print(self.cp, self.sp, self.ep, self.gp, self.pp)
        
      

#main section
print(randint(1,6))
root = Tk()
root.title("BF Treasure Generator")
#root.geometry('500x500')
default_font = font.nametofont("TkDefaultFont")
default_font.configure(size=20)

app = Application(root)
root.mainloop()
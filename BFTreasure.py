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
from Magic import *

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
        self.gems=0
        self.jewels=0
        self.magic=[]  #list of strings
        self.multiplier=1
        
        self.create_widgets()
        
        
    def create_widgets(self):
        """ create widgets in frame """
        self.bind_all('<Key>',self.key)
        
        
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

        
        Label(self, text = "Unguarded").grid(row=9, column =0, columnspan=5,
                                             sticky="w")
        
        self.btnUnguardedClear = Button(self, text="Clear",
                                           command = self.clear_ung_types)
        self.btnUnguardedClear.grid(row=9, column=6, columnspan=2)
        
        self.chkBtn1 = BooleanVar()
        Checkbutton(self, text = "1",
                    variable = self.chkBtn1
                    ).grid(row = 10, column = 0)
        
        self.chkBtn2 = BooleanVar()
        Checkbutton(self, text = "2",
                    variable = self.chkBtn2
                    ).grid(row = 10, column = 1)
        
        self.chkBtn3 = BooleanVar()
        Checkbutton(self, text = "3",
                    variable = self.chkBtn3
                    ).grid(row = 10, column = 2)
        
        self.chkBtn45 = BooleanVar()
        Checkbutton(self, text = "4-5",
                    variable = self.chkBtn45
                    ).grid(row = 10, column = 3)
        
        self.chkBtn67 = BooleanVar()
        Checkbutton(self, text = "6-7",
                    variable = self.chkBtn67
                    ).grid(row = 10, column = 4)
        
        self.chkBtn8 = BooleanVar()
        Checkbutton(self, text = "8+",
                    variable = self.chkBtn8
                    ).grid(row = 10, column = 5)
                        
        ttk.Separator(self, orient=HORIZONTAL).grid(row=12, column=0,
                                                    columnspan=8, sticky="ew")        
        Label(self, text="Treasure").grid(row=13, column=0, columnspan=5,
                                                 sticky="w")
        
        self.btnGenerateReport = Button(self, text="Generate",
                                        command=self.generate_report)
        self.btnGenerateReport.grid(row=13, column=6, columnspan=2)


        self.textBoxReport = Text(self, width = 50, height = 15, wrap = WORD)
        self.textBoxReport.grid(row=14, column =0, columnspan=8)
        
    def key(self, event):
        if event.char in  ('1','!'):
            if self.chkBtn1.get()==False:
                self.chkBtn1.set(True)
            else:
                self.chkBtn1.set(False)        
        
        if event.char in  ('2','@'):
            if self.chkBtn2.get()==False:
                self.chkBtn2.set(True)
            else:
                self.chkBtn2.set(False)
                
        if event.char in  ('3','#'):
            if self.chkBtn3.get()==False:
                self.chkBtn3.set(True)
            else:
                self.chkBtn3.set(False)

        if event.char in  ('4','$', '5', '%'):
            if self.chkBtn45.get()==False:
                self.chkBtn45.set(True)
            else:
                self.chkBtn45.set(False)
        
        if event.char in  ('6','^', '7', '&'):
            if self.chkBtn67.get()==False:
                self.chkBtn67.set(True)
            else:
                self.chkBtn67.set(False)
        
        if event.char in  ('8','*'):
            if self.chkBtn8.get()==False:
                self.chkBtn8.set(True)
            else:
                self.chkBtn8.set(False)
        
        if event.char in  ('a','A'):
            if self.chkBtnA.get()==False:
                self.chkBtnA.set(True)
            else:
                self.chkBtnA.set(False)
                
        if event.char in  ('b','B'):
            if self.chkBtnB.get()==False:
                self.chkBtnB.set(True)
            else:
                self.chkBtnB.set(False)
                
        if event.char in  ('c','C'):
            if self.chkBtnC.get()==False:
                self.chkBtnC.set(True)
            else:
                self.chkBtnC.set(False)
                
        if event.char in  ('d','D'):
            if self.chkBtnD.get()==False:
                self.chkBtnD.set(True)
            else:
                self.chkBtnD.set(False)
                
        if event.char in  ('e','E'):
            if self.chkBtnE.get()==False:
                self.chkBtnE.set(True)
            else:
                self.chkBtnE.set(False)

        if event.char in  ('f', 'F'):
            if self.chkBtnF.get()==False:
                self.chkBtnF.set(True)
            else:
                self.chkBtnF.set(False)
                
        if event.char in  ('g','G'):
            if self.chkBtnG.get()==False:
                self.chkBtnG.set(True)
            else:
                self.chkBtnG.set(False)
                
        if event.char in  ('h','H'):
            if self.chkBtnH.get()==False:
                self.chkBtnH.set(True)
            else:
                self.chkBtnH.set(False)
                
        if event.char in  ('i','I'):
            if self.chkBtnI.get()==False:
                self.chkBtnI.set(True)
            else:
                self.chkBtnI.set(False)
                
        if event.char in  ('j','J'):
            if self.chkBtnJ.get()==False:
                self.chkBtnJ.set(True)
            else:
                self.chkBtnJ.set(False)
                
        if event.char in  ('k','K'):
            if self.chkBtnK.get()==False:
                self.chkBtnK.set(True)
            else:
                self.chkBtnK.set(False)
                
        if event.char in  ('l','L'):
            if self.chkBtnL.get()==False:
                self.chkBtnL.set(True)
            else:
                self.chkBtnL.set(False)
                
        if event.char in  ('m','M'):
            if self.chkBtnM.get()==False:
                self.chkBtnM.set(True)
            else:
                self.chkBtnM.set(False)
                
        if event.char in  ('n','N'):
            if self.chkBtnN.get()==False:
                self.chkBtnN.set(True)
            else:
                self.chkBtnN.set(False)
                
        if event.char in  ('o','O'):
            if self.chkBtnO.get()==False:
                self.chkBtnO.set(True)
            else:
                self.chkBtnO.set(False)
                
        if event.char in  ('p','P'):
            if self.chkBtnP.get()==False:
                self.chkBtnP.set(True)
            else:
                self.chkBtnP.set(False)
                
        if event.char in  ('q','Q'):
            if self.chkBtnQ.get()==False:
                self.chkBtnQ.set(True)
            else:
                self.chkBtnQ.set(False)
                
        if event.char in  ('r','R'):
            if self.chkBtnR.get()==False:
                self.chkBtnR.set(True)
            else:
                self.chkBtnR.set(False)
                
        if event.char in  ('s','S'):
            if self.chkBtnS.get()==False:
                self.chkBtnS.set(True)
            else:
                self.chkBtnS.set(False)
                
        if event.char in  ('t','T'):
            if self.chkBtnT.get()==False:
                self.chkBtnT.set(True)
            else:
                self.chkBtnT.set(False)        

        if event.char in  ('u','U'):
            if self.chkBtnU.get()==False:
                self.chkBtnU.set(True)
            else:
                self.chkBtnU.set(False)
                
        if event.char in  ('v','V'):
            if self.chkBtnV.get()==False:
                self.chkBtnV.set(True)
            else:
                self.chkBtnV.set(False)        


    def clear_lair_types(self):
        """clear the lair type checkboxes"""
        self.chkBtnA.set(False)
        self.chkBtnB.set(False)
        self.chkBtnC.set(False)
        self.chkBtnD.set(False)
        self.chkBtnE.set(False)
        self.chkBtnF.set(False)
        self.chkBtnG.set(False)
        self.chkBtnH.set(False)
        self.chkBtnI.set(False)
        self.chkBtnJ.set(False)
        self.chkBtnK.set(False)
        self.chkBtnL.set(False)
        self.chkBtnM.set(False)
        self.chkBtnN.set(False)
        self.chkBtnO.set(False)
        
    def clear_ind_types(self):
        """clear the lair type checkboxes"""
        self.chkBtnP.set(0)
        self.chkBtnQ.set(0)
        self.chkBtnR.set(0)
        self.chkBtnS.set(0)
        self.chkBtnT.set(0)
        self.chkBtnU.set(0)
        self.chkBtnV.set(0)
        
    def clear_ung_types(self):
        """clear the unguarded treasure type checkboxes"""
        self.chkBtn1.set(0)
        self.chkBtn2.set(0)
        self.chkBtn3.set(0)
        self.chkBtn45.set(0)
        self.chkBtn67.set(0)
        self.chkBtn8.set(0)
        
    def generate_report(self):
        """ calculate treasure and display the results"""
        message = "LAIR\n------------------------------\n"
        message += self.run_through_lair_treasures()

        message += "INDIVIDUAL\n------------------------------\n"
        message += "\n" + str(self.run_through_ind_treasures)

        message += "UNGUARDED\n------------------------------\n"
        #message += "\n" + str(self.run_through_ung_treasures)
        
        self.textBoxReport.delete(0.0,END)
        self.textBoxReport.insert(0.0, message)

        
    def get_numbers(self):
        self.multiplier = \
          simpledialog.askinteger("Input", "How many individuals?",
                                  minvalue=1, maxvalue=99)
        
    def print_treasure(self, tList):
        ''' print details of randomly generated treasure'''
        
        msg = ""
        
        msg = "Type " + tList[0] + "\n"
        msg +=  "  COINS\n"
        msg += "  -----\n"
        msg += "   " + str(tList[1]) + " copper pieces\n"
        msg += "   " + str(tList[2]) + " silver pieces\n"
        msg += "   " + str(tList[3]) + " electrum pieces\n"
        msg += "   " + str(tList[4]) + " gold pieces\n"
        msg += "   " + str(tList[5]) + " platinum pieces\n"
        msg += "\n"
        msg += "  GEMS\n"
        msg += "  ----\n"
        if tList[6] == 0:
            msg += "   NONE\n"
        else:
            for i in range(tList[6]):
                msg += "   " + get_gem() + "\n"
                
        msg += "\n"
        msg += "  JEWELRY\n"
        msg += "  -------\n"
        if tList[7] == 0:
            msg += "   NONE\n"
        else:
            for i in range(tList[7]):
                msg += "   " + get_jewelry() + "\n"
        
        msg += "\n"
        msg += "  MAGIC ITEMS\n"
        msg += "  -----------\n"
        
        if tList[8] == []:
            msg += "   NONE\n"
        else:
            magicList = get_magic(tList[8])
            for item in magicList:
                msg += "   " + item + "\n"
        
        msg += "\n"
        
        return msg

    def run_through_lair_treasures(self):
        msg = ""
        
        if self.chkBtnA.get():
            msg += self.print_treasure(type_a())
      
        if self.chkBtnB.get():
            msg += self.print_treasure(type_b())
        
        if self.chkBtnC.get():
            msg += self.print_treasure(type_c())
      
        if self.chkBtnD.get():
            msg += self.print_treasure(type_d())
        
        if self.chkBtnE.get():
            msg += self.print_treasure(type_e())
      
        if self.chkBtnF.get():
            msg += self.print_treasure(type_f())

        if self.chkBtnG.get():
            msg += self.print_treasure(type_g())
      
        if self.chkBtnH.get():
            msg += self.print_treasure(type_h())
            
        if self.chkBtnI.get():
            msg += self.print_treasure(type_i())
      
        if self.chkBtnJ.get():
            msg += self.print_treasure(type_j())
        
        if self.chkBtnK.get():
            msg += self.print_treasure(type_k())
      
        if self.chkBtnL.get():
            msg += self.print_treasure(type_l())
        
        if self.chkBtnM.get():
            msg += self.print_treasure(type_m())
      
        if self.chkBtnN.get():
            msg += self.print_treasure(type_n())

        if self.chkBtnO.get():
            msg += self.print_treasure(type_o())
           
        return msg
    
    def run_through_ind_treasures(self):
        msg = ""
        multiplier = self.get_numbers()
        
        if self.chkBtnP.get():
            msg += self.print_treasure(type_p(multiplier))
      
        if self.chkBtnQ.get():
            msg += self.print_treasure(type_q(multiplier))
        
        if self.chkBtnR.get():
            msg += self.print_treasure(type_r(multiplier))
      
        if self.chkBtnS.get():
            msg += self.print_treasure(type_s(multiplier))
        
        if self.chkBtnT.get():
            msg += self.print_treasure(type_t(multiplier))
      
        if self.chkBtnU.get():
            msg += self.print_treasure(type_u(multiplier))

        if self.chkBtnV.get():
            msg += self.print_treasure(type_v(multiplier))
         
        return msg
    
      

#main section 
root = Tk()
root.title("BF Treasure Generator")
#root.geometry('500x500')
default_font = font.nametofont("TkDefaultFont")
default_font.configure(size=20)

app = Application(root)

root.mainloop()
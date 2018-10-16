# Wands.py
# Thorin Schmidt
# 10/16/2018

'''central project file for producing random wands'''

from dice import *

def get_wand():
    ''' obtains a randomly generated wand'''
    
    msg = ""
    index = d100()
    wand = "NIL"
    
    if index in (1,2,3,4,5,6,8):
        wand = "Rod of Cancellation"
    elif index in (9,10,11,12,13):
        wand = "Snake Staff"
    elif index in (14,15,16,17):
        wand = "Staff of Commanding"
    elif index in (18,19,20,21,22,23,24,25,26,27,28):
        wand = "Staff of Healing"
    elif index in (29,30):
        wand = "Staff of Power"
    elif index in (31,32,33,34):
        wand = "Staff of Striking"
    elif index == 35:
        wand = "Staff of Wizardry"
    elif index in (36,37,38,39,40):
        wand = "Wand of Cold"
    elif index in (41,42,43,44,45):
        wand = "Wand of Enemy Detection"
    elif index in (46,47,48,49,50):
        wand = "Wand of Fear"
    elif index in (51,52,53,54,55):
        wand = "Wand of Fireballs"
    elif index in (56,57,58,59,60):
        wand = "Wand of Illusion"
    elif index in (61,62,63,64,65):
        wand = "Wand of Lightning Bolts"
    elif index in (66,67,68,69,70,71,72,73):
        wand = "Wand of Magic Detection"
    elif index in (74,75,76,77,78,79):
        wand = "Wand of Paralyzation"
    elif index in (80,81,82,83,84):
        wand = "Wand of Polymorph"
    elif index in (85,86,87,88,89,90,91,92):
        wand = "Wand of Secret Door Detection"
    else:
        wand = "Wand of Trap Detection"
        
    msg = wand
    return msg

#testing
if __name__ == '__main__':
    for i in range(10):
        print(get_wand())

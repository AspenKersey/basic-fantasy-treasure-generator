# Weapons.py
# Thorin Schmidt
# 10/16/2018

'''central project file for producing random weapons'''

from dice import *

def get_weapon():
    ''' obtains a randomly generated weapon'''
    
    msg = ""
    index = d100()
    weapon = "NIL"
    
    if index in (1,2,3,4,5,6,8):
        weapon = "Rod of Cancellation"
    elif index in (9,10,11,12,13):
        weapon = "Snake Staff"
    elif index in (14,15,16,17):
        weapon = "Staff of Commanding"
    elif index in (18,19,20,21,22,23,24,25,26,27,28):
        weapon = "Staff of Healing"
    elif index in (29,30):
        weapon = "Staff of Power"
    elif index in (31,32,33,34):
        weapon = "Staff of Striking"
    elif index == 35:
        weapon = "Staff of Wizardry"
    elif index in (36,37,38,39,40):
        weapon = "weapon of Cold"
    elif index in (41,42,43,44,45):
        weapon = "weapon of Enemy Detection"
    elif index in (46,47,48,49,50):
        weapon = "weapon of Fear"
    elif index in (51,52,53,54,55):
        weapon = "weapon of Fireballs"
    elif index in (56,57,58,59,60):
        weapon = "weapon of Illusion"
    elif index in (61,62,63,64,65):
        weapon = "weapon of Lightning Bolts"
    elif index in (66,67,68,69,70,71,72,73):
        weapon = "weapon of Magic Detection"
    elif index in (74,75,76,77,78,79):
        weapon = "weapon of Paralyzation"
    elif index in (80,81,82,83,84):
        weapon = "weapon of Polymorph"
    elif index in (85,86,87,88,89,90,91,92):
        weapon = "weapon of Secret Door Detection"
    else:
        weapon = "weapon of Trap Detection"
        
    msg = weapon
    return msg

#testing
if __name__ == '__main__':
    for i in range(10):
        print(get_weapon())

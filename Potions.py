# Potions.py
# Thorin Schmidt
# 10/15/2018

'''central project file for producing random potions'''

from dice import *

def get_potion():
    ''' obtains a randomly generated potion'''
    
    msg = "potion of "
    index = d100()
    potion = "NIL"
    
    if index in (1,2,3):
        potion = "Clairaudience"
    elif index in (4,5,6):
        potion = "Clairvoyance"
    elif index in ():
        potion = ""
    elif index in (7,8):
        potion = "Cold Resistance"
    elif index in (9,10,11):
        potion = "Control Animal"
    elif index in (12,13):
        potion = "Control Dragon"
    elif index in (14,15,16):
        potion = "Control Giant"
    elif index in (17,18,19):
        potion = "Control Human"
    elif index in (20,21,22):
        potion = "Control Plant"
    elif index in (23,24,25):
        potion = "Control Undead"
    elif index in (26,27,28,29,30,31,32):
        potion = "Delusion"
    elif index in (33,34,35):
        potion = "Diminution"
    elif index in (36,37,38,39):
        potion = "ESP"
    elif index in (40,41,42,43):
        potion = "Fire Resistance"
    elif index in (44,45,46,47):
        potion = "Flying"
    elif index in (48,49,50,51):
        potion = "Gaseous Form"
    elif index in (52,53,54,55):
        potion = "Giant Strength"
    elif index in (56,57,58,59):
        potion = "Growth"
    elif index in (60,61,62,63):
        potion = "Healing"
    elif index in (64,65,66,67,68):
        potion = "Heroism"
    elif index in (69,70,71,72):
        potion = "Invisibility"
    elif index in (73,74,75,76):
        potion = "Invulnerability"
    elif index in (77,78,79,80):
        potion = "Levitation"
    elif index in (81,82,83,84):
        potion = "Longevity"
    elif index in (85,86):
        potion = "Poison"
    elif index in (87,88,89):
        potion = "Polymorph Self"
    elif index in (90,91,92,93,94,95,96,97):
        potion = "Speed"
    else:
        potion = "Treasure Finding"
        
    msg += potion
    return msg

#testing
if __name__ == '__main__':
    for i in range(10):
        print(get_potion())
                                                    
# MiscMagic.py
# Thorin Schmidt
# 10/16/2018

'''central project file for producing random miscellaneous magic items'''

from dice import *

def get_misc():
    ''' obtains a randomly generated misc'''
    
    msg = ""
    index = d100()
    misc = "NIL"
    
    if index in (1,2,3,4):
        misc = "Amulet of Proof against Detection and Location"
    elif index in (5,6):
        misc = "Bag of Devouring"
    elif index in (7,8,9,10,11,12):
        misc = "Bag of Holding"
    elif index in (13,14,15,16,17):
        misc = "Boots of Levitation"
    elif index in (18,19,20,21,22):
        misc = "Boots of Speed"
    elif index in (23,24,25,26,27):
        misc = "Boots of Traveling and Leaping"
    elif index == 28:
        misc = "Bowl Commanding Water Elementals"
    elif index == 29:
        misc = "Brazier Commanding Fire Elementals"        
    elif index in (30,31,32,33,34,35):
        misc = "Broom of Flying"
    elif index == 36:
        misc = "Censer Commanding Air Elementals"
    elif index in (37,38,39):
        misc = "Cloak of Displacement"
    elif index in (40,41,42,43):
        misc = "Crystal Ball"
    elif index in (44,45):
        misc = "Crystal Ball with Clairaudience"
    elif index == 46:
        misc = "Drums of Panic"
    elif index == 47:
        misc = "Efreeti Bottle"        
    elif index in (48,49,50,51,52,53,54):
        misc = "Elven Boots"
    elif index in (55,56,57,58,59,60,61):
        misc = "Elven Cloak"
    elif index in (62,63):
        misc = "Flying Carpet"
    elif index in (64,65,66,67,68,69,70):
        misc = "Gauntlets of Ogre Power"
    elif index in (71,72):
        misc = "Girdle of Giant Strength"
    elif index in (73,74,75,76,77,78):
        misc = "Helm of Reading Languages and Magic"
    elif index == 79:
        misc = "Helm of Telepathy"
    elif index == 80:
        misc = "Helm of Teleportation"
    elif index == 81:
        misc = "Horn of Blasting"
    elif index == 82:
        misc = "Horn of Doom"
    elif index in (83,84,85,86,87,88,89,90,91):
        misc = "Medallion of ESP"
    elif index == 92:
        misc = "Mirror of Life Trapping"
    elif index in (93,94,95,96,97):
        misc = "Rope of Climbing"
    elif index in (98,99):
        misc = "Scarab of Protection"
    else:
        misc = "Stone Commanding Earth Elementals"
        
    msg = misc
    return msg

#testing
if __name__ == '__main__':
    for i in range(10):
        print(get_misc())

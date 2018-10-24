#!/usr/bin/python3
# Magic.py
# Thorin Schmidt
# 10/23/2018

from dice import *
from Armor import *
from MiscMagic import *
from Potions import *
from Rings import *
from Scrolls import *
from Wands import *
from Weapons import *


def get_magic(mList):
    '''randomly determine a category of magic item'''
    itemList = []
    
    if mList[0][0] > 0:
        for i in range(die_roller(mList[0][0],mList[0][1])):
            itemList.append(get_any())
        
    if mList[1][0] > 0:
        for i in range(die_roller(mList[1][0],mList[1][1])):
            itemList.append(get_any_weap_or_arm())
            
    if mList[2][0] > 0:
        for i in range(die_roller(mList[2][0],mList[2][1])):
            itemList.append(get_any_exc_Weap())
            
    if mList[3][0] > 0:
        for i in range(die_roller(mList[3][0],mList[3][1])):
            itemList.append(get_potion())
            
    if mList[4][0] > 0:
        for i in range(die_roller(mList[4][0],mList[4][1])):
            itemList.append(get_scroll())

    return itemList

def get_any():

        index = d100()
        
        if index in range(1, 26):
            return get_weapon()
        elif index in range(26,36):
            return get_armor()
        elif index in range(36,56):
            return get_potion()
        elif index in range(56,86):
            return get_scroll()
        elif index in range(86,91):
            return get_ring()
        elif index in range(91,96):
            return get_wand()
        else:
            return get_misc()

def get_any_weap_or_arm():

    index = d100()
    
    if index in range(1, 71):
        return get_weapon()
    else:
        return get_armor()

def get_any_exc_Weap():

    index = d100()
    
    if index in range(1,13):
        return get_armor()
    elif index in range(13,41):
        return get_potion()
    elif index in range(41,80):
        return get_scroll()
    elif index in range(80,87):
        return get_ring()
    elif index in range(87,93):
        return get_wand()
    else:
        return get_misc()

#testing
if __name__ == '__main__':
    print(get_magic([(3,1),(0,0),(0,0),(0,0),(0,0)]))
    print(get_magic([(0,0),(1,1),(0,0),(0,0),(0,0)]))
    print(get_magic([(1,2),(0,0),(0,0),(0,0),(0,0)]))
    print(get_magic([(3,1),(0,0),(0,0),(1,1),(0,0)]))
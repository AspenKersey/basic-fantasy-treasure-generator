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
        itemList.append(get_any(mList[0]))
        
    if mList[1][0] > 0:
        itemList.append(get_any_weap_or_arm(mList[1]))
            
    if mList[2][0] > 0:
        itemList.append(get_any_exc_Weap(mList[2]))
            
    if mList[3][0] > 0:
        for i in range(die_roller(mList[3][0],mList[3][1])):
            itemList.append(get_potion())
            
    if mList[4][0] > 0:
        for i in range(die_roller(mList[4][0],mList[4][1])):
            itemList.append(get_scroll())

    return itemList

def get_any(diceList):
    
    anyList = []
    for i in range(die_roller(diceList[0],diceList[1])):
        index = d100()
        
        if index in range(1, 26):
            anyList.append(get_weapon())
        elif index in range(26,36):
            anyList.append(get_armor())
        elif index in range(36,56):
            anyList.append(get_potion())
        elif index in range(56,86):
            anyList.append(get_scroll())
        elif index in range(86,91):
            anyList.append(get_ring())
        elif index in range(91,96):
            anyList.append(get_wand())
        else:
            anyList.append(get_misc())
                
    return anyList

def get_any_weap_or_arm(diceList):
    anyWeapList = []
    
    for i in range(die_roller(diceList[0],diceList[1])):
        index = d100()
        
        if index in range(1, 71):
            anyWeapList.append(get_weapon())
        else:
            anyWeapList.append(get_armor())
       
    return anyWeapList

def get_any_exc_Weap(diceList):
    excWeapList = ""
    
    for i in range(die_roller(diceList[0],diceList[1])):
        index = d100()
        
        if index in range(1,13):
            excWeapList.append(get_armor())
        elif index in range(13,41):
            excWeapList.append(get_potion())
        elif index in range(41,80):
            excWeapList.append(get_scroll())
        elif index in range(80,87):
            excWeapList.append(get_ring())
        elif index in range(87,93):
            excWeapList.append(get_wand())
        else:
            excWeapList.append(get_misc())    
    
    return excWeapList

#testing
if __name__ == '__main__':
    print(get_magic([(3,1),(0,0),(0,0),(0,0),(0,0)]))
    print(get_magic([(0,0),(1,1),(0,0),(0,0),(0,0)]))
    print(get_magic([(1,2),(0,0),(0,0),(0,0),(0,0)]))
    print(get_magic([(3,1),(0,0),(0,0),(1,1),(0,0)]))
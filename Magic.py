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

    return itemList

def get_any(dicelist):
    
    anyList = []
    for i in range(die_roller(dicelist[0],dicelist[1])):
        index = d100()
        
        if index in range(1, 26):
            anyList.append(get_weapon())
        elif index in range(26,36):
            anyList.append(get_armor())
        
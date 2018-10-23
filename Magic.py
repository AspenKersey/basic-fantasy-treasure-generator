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


def get_magic(howmany):
    '''randomly determine a category of magic item'''
    number = howmany[0]
    sides = howmany[1]
    
    return (number, sides)
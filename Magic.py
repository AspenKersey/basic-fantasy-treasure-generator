#!/usr/bin/python3
# Magic.py
# Thorin Schmidt
# 10/23/2018

from dice import *

def get_magic(howmany):
    '''randomly determine a category of magic item'''
    number = howmany[0]
    sides = howmany[1]
    
    return (number, sides)
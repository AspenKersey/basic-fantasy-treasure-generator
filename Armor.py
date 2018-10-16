# Armor.py
# Thorin Schmidt
# 10/16/2018

'''central project file for producing random magic armor'''

from dice import *

def get_curse():
    ''' randomly generates an AC curse and returns it as a string'''
    curse = "NILCURSE"
    index = die_roller(1,90)
    
    if index in range(1,51):
        curse = "-1 (appears +1)"
    elif index in range(51,81):
        curse = "-2 (appears +2)"
    else:
        curse = "-3 (appears +3)"  
    
    return curse

def get_bonus():
    ''' randomly generates an AC bonus and returns it as a string'''
    bonus = "NILBONUS"
    index = d100()
    
    if index in range(1,51):
        bonus = "+1"
    elif index in range(51,81):
        bonus = "+2"
    elif index in range(81,91):
        bonus = "+3"
    elif index in range(91,95):
        bonus = "Cursed " + get_curse()    
    else:
        bonus = "Cursed, AC 11 (appears +1)"
    
    return bonus

def get_armor():
    ''' obtains a randomly generated armor'''
    
    msg = ""
    index = d100()
    armor = "NIL"
    bonus = "NIL"
    
    if index in range(1,10):
        armor = "Leather Armor"
    elif index in range(10,29):
        armor = "Chain Mail"
    elif index in range(29,44):
        armor = "Plate Mail"
    else:
        armor = "Shield"
        
    bonus = get_bonus()
    msg = armor + " " + bonus
    return msg

#testing
if __name__ == '__main__':
    for i in range(10):
        print(get_armor())
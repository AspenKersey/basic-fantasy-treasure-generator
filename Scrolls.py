# Scrolls.py
# Thorin Schmidt
# 10/16/2018

'''central project file for producing random scrolls'''

from dice import *

def get_scroll():
    ''' obtains a randomly generated scroll'''
    
    msg = ""
    index = d100()
    scroll = "NIL"
    
    if index in (1,2,3):
        scroll = "Cleric Spell Scroll (1 Spell)"
    elif index in (4,5,6):
        scroll = "Cleric Spell Scroll (2 Spells)"
    elif index in (7,8):
        scroll = "Cleric Spell Scroll (3 Spells)"
    elif index == 9:
        scroll = "Cleric Spell Scroll (4 Spells)"
    elif index in (10,11,12,13,14,15):
        scroll = "Magic-User Spell Scroll (1 Spell)"
    elif index in (16,17,18,19,20):
        scroll = "Magic-User Spell Scroll (2 Spells)"
    elif index in (21,22,23,24,25):
        scroll = "Magic-User Spell Scroll (3 Spells)"
    elif index in (26,27,28,29):
        scroll = "Magic-User Spell Scroll (4 Spells)"        
    elif index in (30,31,32):
        scroll = "Magic-User Spell Scroll (5 Spells)"
    elif index in (33,34):
        scroll = "Magic-User Spell Scroll (6 Spells)"
    elif index == 35:
        scroll = "Magic-User Spell Scroll (7 Spells)"
    elif index in (36,37,38,39,40):
        scroll = "Cursed Scroll - " + choose_curse()
    elif index in (41,42,43,44,45,46):
        scroll = "Scroll: Protection from Elementals"
    elif index in(47,48,49,50,51,52,53,54,55,56):
        scroll = "Scroll: Protection from Lycanthropes"
    elif index in(57,58,59,60,61):
        scroll = "Scroll: Protection from Magic"        
    elif index in (62,63,64,65,66,67,68,69,70,71,72,73,74,75):
        scroll = "Scroll: Protection from Undead"
    elif index in (76,77,78,79,80,81,82,83,84,85):
        scroll = "Map to Treasure Type A"
    elif index in (86,87,88,89):
        scroll = "Map to Treasure Type E"
    elif index in (90,91,92):
        scroll = "Map to Treasure Type G"
    else:
        scroll = "Map to 1d4 Magic Items"
        
    msg = scroll
    return msg

def choose_curse():
    curse = ""
    
    index = d4()
    
    if index == 1:
        curse = "-4 decrease to an ability score (minimum 1)."
    elif index == 2:
        curse = "-4 penalty on attack rolls and saves."
    elif index == 3:
        curse = "Each round of combat, the target has a 50% chance to act normally; otherwise, it takes no action."
    else:
        curse = "GM's Diabolical Choice!"
    
    return curse

#testing
if __name__ == '__main__':
    for i in range(10):
        print(get_scroll())
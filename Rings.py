# Rings.py
# Thorin Schmidt
# 10/16/2018

'''central project file for producing random rings'''

from dice import *

def get_ring():
    ''' obtains a randomly generated ring'''
    
    msg = "Ring of "
    index = d100()
    ring = "NIL"
    
    if index in (1,2,3,4,5,6):
        ring = "Control Animal"
    elif index in (7,8,9,10,11,12):
        ring = "Control Human"
    elif index in (13,14,15,16,17,18,19):
        ring = "Control Plant"
    elif index in (20,21,22,23,24,25,26,27,28,29,30):
        ring = "Delusion"
    elif index in (31,32,33):
        ring = "Djinni Summoning"
    elif index in (34,35,36,37,38,39,40,41,42,43,44):
        ring = "Fire Resistance"
    elif index in (45,46,47,48,49,50,51,52,53,54,55,56,57):
        ring = "Invisibility"
    elif index in (58,59,60,61,62,63,64,65,66):
        ring = "Protection +1"
    elif index in (67,68,69,70):
        ring = "Protection +2"
    elif index == 71:
        ring = "Protection +3"
    elif index in (72,73):
        ring = "Regeneration"
    elif index in (74,75):
        ring = "Spell Storing"
    elif index in (76,77,78,79,80,81):
        ring = "Spell Turning"
    elif index in (82,83):
        ring = "Telekinesis"
    elif index in (74,75):
        ring = "Water Walking"
    elif index in (91,92,93,94,95,96,97):
        ring = "Weakness"
    elif index == 98:
        ring = "Wishes"
    else:
        ring = "X-Ray Vision"
        
    msg += ring
    return msg

#testing
if __name__ == '__main__':
    for i in range(10):
        print(get_ring())

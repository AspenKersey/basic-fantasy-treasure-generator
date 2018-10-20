# Weapons.py
# Thorin Schmidt
# 10/16/2018

'''central project file for producing random weapons'''

from dice import *

def get_enemy():
    ''' returns special enemy name as a string'''
    
    enemy = "NIL_ENEMY"
    index = d6()
    
    if index == 1:
        enemy = "Dragons"
    elif index == 2:
        enemy = "Enchanted"
    elif index == 3:
        enemy = "Lycanthropes"
    elif index == 4:
        enemy = "Regenerators"
    elif index == 5:
        enemy = "Spell Users"
    else:
        enemy = "Undead"
        
    return enemy

def get_ability(bonus):
    '''returns special ability as a string
    
    there is a possibility to enter this even though the weapon is cursed.
    if so, return "" as the special ability string'''
    
    if bonus[0] == "C" or "SA:" in bonus:
        return ""
    
    ability = "  - SA: "
    index = d20()
    
    if index in (1,2,3,4,5,6,7,8,9):
        ability += "Casts Light on Command"
    elif index in (10,11):
        ability += "Charm Person"
    elif index == (12):
        ability += "Drains Energy"
    elif index in (13,14,15,16):
        ability += "Flames on Command"
    elif index in (17,18,19):
        ability += "Locate Objects"
    else:
        ability += "Wishes"
        
    return ability

def get_bonus(isMelee):
    ''' returns the randomly generated weapon bonus as a string'''
    
    bonus ="NIL_BONUS"
    index = d100()
    
    if isMelee:
        if index in range(1,41):
            bonus = "+1"
        elif index in range(41,51):
            bonus = "+2"
        elif index in range(51,56):
            bonus = "+3"
        elif index in range(56,58):
            bonus = "+4"
        elif index == 58:
            bonus = "+5"
        elif index in range(59,76):
            bonus = "+1, +2 vs. " + get_enemy()
        elif index in range(76,86):
            bonus = "+1, +3 vs. " + get_enemy()
        elif index in range(86,96):
            #roll again + special ability(unless cursed)
            bonus = get_bonus(True)
            bonus += get_ability(bonus)
        elif index in range(96,99):
            bonus = "Cursed, -1"
        else:
            bonus = "Cursed, -2"
    else:
        if index in range(1,47):
            bonus = "+1"
        elif index in range(47,59):
            bonus = "+2"
        elif index in range(59,65):
            bonus = "+3"
        elif index in range(65,83):
            bonus = "+1, +2 vs. " + get_enemy()
        elif index in range(83,94):
            bonus = "+1, +3 vs. " + get_enemy()
        elif index in range(95,99):
            bonus = "Cursed, -1"
        else:
            bonus = "Cursed, -2"
            
    return bonus
    
def get_weapon():
    ''' obtains a randomly generated weapon'''
    
    msg = ""
    index = d100()
    weapon = "NIL"
    isMelee = False
    
    if index in (1,2):
        weapon = "Great Axe"
        isMelee = True
    elif index in (3,4,5,6,7,8,9):
        weapon = "Battle Axe"
        isMelee = True
    elif index in (10,11):
        weapon = "Hand Axe"
        isMelee = True
    elif index in (12,13,14,15,16,17,18,19):
        weapon = "Shortbow"
        isMelee = False
    elif index in (20,21,22,23,24,25,26,27):
        weapon = "Shortbow Arrow"
        isMelee = False
    elif index in (28,29,30,31):
        weapon = "Longbow"
        isMelee = False
    elif index in (32,33,34,35):
        weapon = "Longbow Arrow"
        isMelee = False
    elif index in (36,37,38,39,40,41,42,43):
        weapon = "Light Quarrel"
        isMelee = False
    elif index in (44,45,46,47):
        weapon = "Heavy Quarrel"
        isMelee = False
    elif index in (48,49,50,51,52,53,54,55,56,57,58,59):
        weapon = "Dagger"
        isMelee = True
    elif index in (60,61,62,63,64,65):
        weapon = "Shortsword"
        isMelee = True
    elif index in (66,67,68,69,70,71,72,73,74,75,76,77,78,79):
        weapon = "Longsword"
        isMelee = True
    elif index in (80,81):
        weapon = "Scimitar"
        isMelee = True
    elif index in (82,83):
        weapon = "Two-Handed Sword"
        isMelee = True
    elif index in (84,85,86):
        weapon = "Warhammer"
        isMelee = True
    elif index in (87,88,89,90,91,92,93,94):
        weapon = "Mace"
        isMelee = True
    elif index == 95:
        weapon = "Maul"
        isMelee = True
    elif index == 96:
        weapon = "Maul"
        isMelee = True
    elif index == 97:
        weapon = "Sling Bullet"
        isMelee = False        
    else:
        weapon = "Spear"
        isMelee = True
        
    msg = weapon
    msg += " " + get_bonus(isMelee)
    
    return msg

#testing
if __name__ == '__main__':
    for i in range(10):
        print(get_weapon())
       
    print("ability test:", get_ability("+3 - SA: Wishes"))

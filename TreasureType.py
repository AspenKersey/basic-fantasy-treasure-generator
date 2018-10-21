# TreasureType.py
# Thorin Schmidt
# 9/16/2018

from dice import *

def percent_less_than(num):
  if randint(1, 100) <= num:
    return True
  else:
    return False
def type_a():
  '''calculates and returns amount of treasure based on type
  
  the treasure types are those listed in the treasure tables from page
  130 of the Basic Fantasy Rulebook. '''
  
  copper = 0
  silver = 0
  electrum = 0
  gold = 0
  platinum = 0
  gems = 0
  jewels = 0
  magic = ""
  
  #copper
  if percent_less_than(50):
    copper += die_roller(5,6) *100
  
  #silver
  if percent_less_than(60):
    silver += die_roller(5,6)*100
  
  #electrum
  if percent_less_than(40):
    electrum += die_roller(5,4)*100
  
  #gold
  if percent_less_than(70):
    gold += die_roller(10,6)*100
  
  #platinum
  if percent_less_than(50):
    platinum += die_roller(1,10)*100
  
  #gems
  if percent_less_than(50):
    gems += die_roller(6,6)
  
  #jewelry
  if percent_less_than(50):
    jewels += die_roller(6,6)
  
  #magic items
  if percent_less_than(30):
    magic += "Any 3"  
  
  return ("A",copper, silver, electrum, gold, platinum, gems, jewels, magic)

def type_b():
  '''calculates and returns amount of treasure based on type
  
  the treasure types are those listed in the treasure tables from page
  130 of the Basic Fantasy Rulebook. '''
  
  copper = 0
  silver = 0
  electrum = 0
  gold = 0
  platinum = 0
  gems = 0
  jewels = 0
  magic = ""
  
  #copper
  if percent_less_than(75):
    copper += die_roller(5,10) *100
  
  #silver
  if percent_less_than(50):
    silver += die_roller(5,6)*100
  
  #electrum
  if percent_less_than(50):
    electrum += die_roller(5,4)*100
  
  #gold
  if percent_less_than(50):
    gold += die_roller(3,6)*100
  
  #platinum
  '''none'''
  
  #gems
  if percent_less_than(25):
    gems += die_roller(1,6)
  
  #jewelry
  if percent_less_than(25):
    jewels += die_roller(1,6)
  
  #magic items
  if percent_less_than(10):
    magic += "1 weapon or armor"  
  
  return ("B", copper, silver, electrum, gold, platinum, gems, jewels, magic)

def type_c():
  '''calculates and returns amount of treasure based on type
  
  the treasure types are those listed in the treasure tables from page
  130 of the Basic Fantasy Rulebook. '''
  
  copper = 0
  silver = 0
  electrum = 0
  gold = 0
  platinum = 0
  gems = 0
  jewels = 0
  magic = ""
  
  #copper
  if percent_less_than(60):
    copper += die_roller(6,6) *100
  
  #silver
  if percent_less_than(60):
    silver += die_roller(5,4)*100
  
  #electrum
  if percent_less_than(30):
    electrum += die_roller(2,6)*100
  
  #gold
  #platinum
  '''none'''
  
  #gems
  if percent_less_than(25):
    gems += die_roller(1,4)
  
  #jewelry
  if percent_less_than(25):
    jewels += die_roller(1,4)
  
  #magic items
  if percent_less_than(15):
    magic += "any 1d2"  
  
  return ("C", copper, silver, electrum, gold, platinum, gems, jewels, magic)

def type_d():
  '''calculates and returns amount of treasure based on type
  
  the treasure types are those listed in the treasure tables from page
  130 of the Basic Fantasy Rulebook. '''  
  
  copper = 0
  silver = 0
  electrum = 0
  gold = 0
  platinum = 0
  gems = 0
  jewels = 0
  magic = ""
  
  #copper
  if percent_less_than(30):
    copper += die_roller(4,6) *100
  
  #silver
  if percent_less_than(45):
    silver += die_roller(6,6)*100
  
  #electrum
  '''none'''
  
  #gold
  if percent_less_than(90):
    gold += die_roller(5,8)*100
  
  #platinum
  '''none'''
  
  #gems
  if percent_less_than(30):
    gems += die_roller(1,8)
  
  #jewelry
  if percent_less_than(30):
    jewels += die_roller(1,8)
  
  #magic items
  if percent_less_than(20):
    magic += "any 1d2 + 1 potion"  
  
  return ("D", copper, silver, electrum, gold, platinum, gems, jewels, magic)

def type_e():
  '''calculates and returns amount of treasure based on type
  
  the treasure types are those listed in the treasure tables from page
  130 of the Basic Fantasy Rulebook. '''  
  
  copper = 0
  silver = 0
  electrum = 0
  gold = 0
  platinum = 0
  gems = 0
  jewels = 0
  magic = ""
  
  #copper
  if percent_less_than(30):
    copper += die_roller(2,8) *100
  
  #silver
  if percent_less_than(60):
    silver += die_roller(6,10)*100
  
  #electrum
  if percent_less_than(50):
    electrum += die_roller(3,8)*100
  
  #gold
  if percent_less_than(50):
    gold += die_roller(4,10)*100
  
  #platinum
  '''none'''
  
  #gems
  if percent_less_than(10):
    gems += die_roller(1,10)
  
  #jewelry
  if percent_less_than(10):
    jewels += die_roller(1,10)
  
  #magic items
  if percent_less_than(30):
    magic += "any 1d4 + 1 scroll"  
  
  return ("E", copper, silver, electrum, gold, platinum, gems, jewels, magic)

def type_f():
  '''calculates and returns amount of treasure based on type
  
  the treasure types are those listed in the treasure tables from page
  130 of the Basic Fantasy Rulebook. '''  
  
  copper = 0
  silver = 0
  electrum = 0
  gold = 0
  platinum = 0
  gems = 0
  jewels = 0
  magic = ""
  
  #copper
  '''none'''
  
  #silver
  if percent_less_than(40):
    silver += die_roller(3,8)*100
  
  #electrum
  if percent_less_than(50):
    electrum += die_roller(4,8)*100
  
  #gold
  if percent_less_than(85):
    gold += die_roller(6,10)*100
  
  #platinum
  if percent_less_than(70):
    platinum += die_roller(2,8)*100
  
  #gems
  if percent_less_than(20):
    gems += die_roller(2,12)
  
  #jewelry
  if percent_less_than(10):
    jewels += die_roller(1,12)
  
  #magic items
  if percent_less_than(35):
    magic += "any 1d4 except weapons + 1 potion + 1 scroll"  
  
  return ("F", copper, silver, electrum, gold, platinum, gems, jewels, magic)

def type_g():
  '''calculates and returns amount of treasure based on type
  
  the treasure types are those listed in the treasure tables from page
  130 of the Basic Fantasy Rulebook. '''  
  
  copper = 0
  silver = 0
  electrum = 0
  gold = 0
  platinum = 0
  gems = 0
  jewels = 0
  magic = ""
  
  #copper
  #silver
  #electrum
  '''none'''
  
  #gold
  if percent_less_than(90):
    gold += die_roller(4,6)*10*100
  
  #platinum
  if percent_less_than(75):
    platinum += die_roller(5,8)*100
  
  #gems
  if percent_less_than(25):
    gems += die_roller(3,6)
  
  #jewelry
  if percent_less_than(25):
    jewels += die_roller(1,10)
  
  #magic items
  if percent_less_than(50):
    magic += "any 1d4 = 1 scroll"  
  
  return ("G", copper, silver, electrum, gold, platinum, gems, jewels, magic)

def type_h():
  '''calculates and returns amount of treasure based on type
  
  the treasure types are those listed in the treasure tables from page
  130 of the Basic Fantasy Rulebook. '''  
  
  copper = 0
  silver = 0
  electrum = 0
  gold = 0
  platinum = 0
  gems = 0
  jewels = 0
  magic = ""
  
  #copper
  if percent_less_than(75):
    copper += die_roller(8,10) *100
  
  #silver
  if percent_less_than(75):
    silver += die_roller(6,10)*10*100
  
  #electrum
  if percent_less_than(75):
    electrum += die_roller(3,10)*10*100
  
  #gold
  if percent_less_than(75):
    gold += die_roller(5,8)*10*100
  
  #platinum
  if percent_less_than(75):
    platinum += die_roller(9,8)*100
  
  #gems
  if percent_less_than(50):
    gems += die_roller(1,100)
  
  #jewelry
  if percent_less_than(50):
    jewels += die_roller(10,4)
  
  #magic items
  if percent_less_than(20):
    magic += "any 1d4 + 1 potion + 1 scroll"  
  
  return ("H", copper, silver, electrum, gold, platinum, gems, jewels, magic)


def type_i():
  '''calculates and returns amount of treasure based on type
  
  the treasure types are those listed in the treasure tables from page
  130 of the Basic Fantasy Rulebook. '''  
  
  copper = 0
  silver = 0
  electrum = 0
  gold = 0
  platinum = 0
  gems = 0
  jewels = 0
  magic = ""
  
  #copper
  #silver
  #electrum
  #gold
  '''none'''
  
  #platinum
  if percent_less_than(80):
    platinum += die_roller(3,10)*100
  
  #gems
  if percent_less_than(50):
    gems += die_roller(2,6)
  
  #jewelry
  if percent_less_than(50):
    jewels += die_roller(2,6)
  
  #magic items
  if percent_less_than(15):
    magic += "any 1"  
  
  return ("I", copper, silver, electrum, gold, platinum, gems, jewels, magic)


def type_j():
  '''calculates and returns amount of treasure based on type
  
  the treasure types are those listed in the treasure tables from page
  130 of the Basic Fantasy Rulebook. '''  
  
  copper = 0
  silver = 0
  electrum = 0
  gold = 0
  platinum = 0
  gems = 0
  jewels = 0
  magic = ""
  
  #copper
  if percent_less_than(45):
    copper += die_roller(3,8)*100
  
  #silver
  if percent_less_than(45):
    silver += die_roller(1,8)*100
  
  #electrum
  #gold
  #platinum
  #gems
  #jewelry
  #magic items
  '''none'''
  
  return ("J", copper, silver, electrum, gold, platinum, gems, jewels, magic)


def type_k():
  '''calculates and returns amount of treasure based on type
  
  the treasure types are those listed in the treasure tables from page
  130 of the Basic Fantasy Rulebook. '''  
  
  copper = 0
  silver = 0
  electrum = 0
  gold = 0
  platinum = 0
  gems = 0
  jewels = 0
  magic = ""
  
  #copper
  '''none'''
  
  #silver
  if percent_less_than(90):
    silver += die_roller(2,10)*100
  
  #electrum
  if percent_less_than(35):
    electrum += die_roller(1,8)*100
  
  #gold
  #platinum
  #gems
  #jewelry
  #magic items
  '''none'''
  
  return ("K", copper, silver, electrum, gold, platinum, gems, jewels, magic)


def type_l():
  '''calculates and returns amount of treasure based on type
  
  the treasure types are those listed in the treasure tables from page
  130 of the Basic Fantasy Rulebook. '''  
  
  copper = 0
  silver = 0
  electrum = 0
  gold = 0
  platinum = 0
  gems = 0
  jewels = 0
  magic = ""
  
  #copper
  #silver
  #electrum  
  #gold
  #platinum
  '''none'''
  
  #gems
  if percent_less_than(50):
    gems += die_roller(1,4)
  
  #jewelry
  #magic items
  '''none'''
  
  return ("L", copper, silver, electrum, gold, platinum, gems, jewels, magic)


def type_m():
  '''calculates and returns amount of treasure based on type
  
  the treasure types are those listed in the treasure tables from page
  130 of the Basic Fantasy Rulebook. '''  
  
  copper = 0
  silver = 0
  electrum = 0
  gold = 0
  platinum = 0
  gems = 0
  jewels = 0
  magic = ""
  
  #copper
  #silver
  #electrum
  '''none'''
  
  #gold
  if percent_less_than(90):
    gold += die_roller(4,10)*100
  
  #platinum
  if percent_less_than(90):
    platinum += die_roller(2,8)*10*100
  
  #gems
  if percent_less_than(55):
    gems += die_roller(5,4)
  
  #jewelry
  if percent_less_than(45):
    jewels += die_roller(2,6)
  
  #magic items
  '''none'''
  
  return ("M", copper, silver, electrum, gold, platinum, gems, jewels, magic)


def type_n():
  '''calculates and returns amount of treasure based on type
  
  the treasure types are those listed in the treasure tables from page
  130 of the Basic Fantasy Rulebook. '''  
  
  copper = 0
  silver = 0
  electrum = 0
  gold = 0
  platinum = 0
  gems = 0
  jewels = 0
  magic = ""
  
  #copper
  #silver
  #electrum
  #gold
  #platinum
  #gems
  #jewelry
  '''none'''

  #magic items
  if percent_less_than(40):
    magic += "2d4 potions"  
  
  return ("N", copper, silver, electrum, gold, platinum, gems, jewels, magic)


def type_o():
  '''calculates and returns amount of treasure based on type
  
  the treasure types are those listed in the treasure tables from page
  130 of the Basic Fantasy Rulebook. '''  
  
  copper = 0
  silver = 0
  electrum = 0
  gold = 0
  platinum = 0
  gems = 0
  jewels = 0
  magic = ""
  
  #copper
  #silver
  #electrum
  #gold
  #platinum
  #gems
  #jewelry
  '''none'''

  #magic items
  if percent_less_than(50):
    magic += "1d4 scrolls"
        
  return ("O", copper, silver, electrum, gold, platinum, gems, jewels, magic)


def type_p():
  '''calculates and returns amount of treasure based on type
  
  the treasure types are those listed in the treasure tables from page
  130 of the Basic Fantasy Rulebook. '''  
  
  copper = 0
  silver = 0
  electrum = 0
  gold = 0
  platinum = 0
  gems = 0
  jewels = 0
  magic = ""
  
  #copper
  copper += die_roller(3,8)
    
  #silver
  #electrum
  #gold
  #platinum
  #gems
  #jewelry
  #magic items
  '''none''' 
  
  return ("P", copper, silver, electrum, gold, platinum, gems, jewels, magic)


def type_q():
  '''calculates and returns amount of treasure based on type
  
  the treasure types are those listed in the treasure tables from page
  130 of the Basic Fantasy Rulebook. '''  
  
  copper = 0
  silver = 0
  electrum = 0
  gold = 0
  platinum = 0
  gems = 0
  jewels = 0
  magic = ""
  
  #copper
  '''none'''
    
  #silver
  silver += die_roller(3,8)  
  
  #electrum
  #gold
  #platinum
  #gems
  #jewelry
  #magic items
  '''none'''   
  
  return ("Q", copper, silver, electrum, gold, platinum, gems, jewels, magic)


def type_r():
  '''calculates and returns amount of treasure based on type
  
  the treasure types are those listed in the treasure tables from page
  130 of the Basic Fantasy Rulebook. '''  
  
  copper = 0
  silver = 0
  electrum = 0
  gold = 0
  platinum = 0
  gems = 0
  jewels = 0
  magic = ""
  
  #copper
  #silver
  '''none'''
  
  #electrum
  electrum += die_roller(2,6)
  
  #gold
  #platinum
  #gems
  #jewelry
  #magic items
  '''none'''
  
  return ("R", copper, silver, electrum, gold, platinum, gems, jewels, magic)


def type_s():
  '''calculates and returns amount of treasure based on type
  
  the treasure types are those listed in the treasure tables from page
  130 of the Basic Fantasy Rulebook. '''  
  
  copper = 0
  silver = 0
  electrum = 0
  gold = 0
  platinum = 0
  gems = 0
  jewels = 0
  magic = ""
  
  #copper
  #silver
  #electrum
  '''none'''
  
  #gold
  gold += die_roller(2,4)
  
  #platinum
  #gems
  #jewelry
  #magic items
  '''none'''
  
  return ("S", copper, silver, electrum, gold, platinum, gems, jewels, magic)


def type_t():
  '''calculates and returns amount of treasure based on type
  
  the treasure types are those listed in the treasure tables from page
  130 of the Basic Fantasy Rulebook. '''  
  
  copper = 0
  silver = 0
  electrum = 0
  gold = 0
  platinum = 0
  gems = 0
  jewels = 0
  magic = ""
  
  #copper
  #silver
  #electrum
  #gold
  '''none'''
  
  #platinum
  platinum += die_roller(1,6)
  
  #gems
  #jewelry
  #magic items
  '''none'''

  return ("T",copper, silver, electrum, gold, platinum, gems, jewels, magic)


def type_u():
  '''calculates and returns amount of treasure based on type
  
  the treasure types are those listed in the treasure tables from page
  130 of the Basic Fantasy Rulebook. '''  
  
  copper = 0
  silver = 0
  electrum = 0
  gold = 0
  platinum = 0
  gems = 0
  jewels = 0
  magic = ""
  
  #copper
  if percent_less_than(50):
    copper += die_roller(1,20)
  
  #silver
  if percent_less_than(50):
    silver += die_roller(1,20)
  
  #electrum
  '''none'''

  #gold
  if percent_less_than(25):
    gold += die_roller(1,20)
  
  #platinum
  '''none'''
  
  #gems
  if percent_less_than(5):
    gems += die_roller(1,4)
  
  #jewelry
  if percent_less_than(5):
    jewels += die_roller(1,4)
  
  #magic items
  if percent_less_than(2):
    magic += "any 1"  
  
  return ("U", copper, silver, electrum, gold, platinum, gems, jewels, magic)


def type_v():
  '''calculates and returns amount of treasure based on type
  
  the treasure types are those listed in the treasure tables from page
  130 of the Basic Fantasy Rulebook. '''  
  
  copper = 0
  silver = 0
  electrum = 0
  gold = 0
  platinum = 0
  gems = 0
  jewels = 0
  magic = ""
  
  #copper
  '''none'''
  
  #silver
  if percent_less_than(25):
    silver += die_roller(1,20)
  
  #electrum
  if percent_less_than(25):
    electrum += die_roller(1,20)
  
  #gold
  if percent_less_than(50):
    gold += die_roller(1,20)
  
  #platinum
  if percent_less_than(25):
    platinum += die_roller(1,20)
  
  #gems
  if percent_less_than(10):
    gems += die_roller(1,4)
  
  #jewelry
  if percent_less_than(10):
    jewels += die_roller(1,4)
  
  #magic items
  if percent_less_than(5):
    magic += "any 1"  
  
  return ("V", copper, silver, electrum, gold, platinum, gems, jewels, magic)

def gem_value():
  '''calculates the value of a single gem, then returns it as a string
  
  also calls the helper function gem_adjust which alters the base class
  and/or value of the gem.'''
  
  GEM_TYPES = ('Ornamental','Semiprecious','Fancy','Precious','Gem','Jewel')
  VALUES = (10,50,100,500,1000,5000)
  index = -1
  gemType = ''
  value = 0
  multiplier = 0
  result = die_roller(1,100)
  
  if result in range(1,21):
    index = 0
  elif result in range(21,46):
    index = 1
  elif result in range(46,76):
    index = 2
  elif result in range(76,96):
    index = 3
  else:
    index = 4
    
  index, multiplier = gem_adjust(index)  
  
  gemType = GEM_TYPES[index]
  value = int(VALUES[index]*multiplier)
  
  return gemType, str(value)

def gem_adjust(index):
  multiplier = 1.0
  result = die_roller(2,6)
  
  if result == 2:
    index -= 1
    multiplier = 1
  elif result == 3:
    multiplier = .5
  elif result == 4:
    multiplier = .75
  elif result in (5,6,7,8,9):
    multiplier = 1.0
  elif result == 10:
    multiplier = 1.5
  elif result == 11:
    multiplier = 2.0
  else:
    multiplier =1.0
    index += 1
    
  return (index, multiplier)

def gem_name():
  result = die_roller(1,100)
  
  if result in range(1,11):
    return "Greenstone"
  elif result in range(11,21):
    return "Malachite"
  elif result in range(21,29):
    return "Aventurine"
  elif result in range(29,39):
    return "Phenalope"  
  elif result in range(39,46):
    return "Amethyst"  
  elif result in range(46,55):
    return "Fluorospar"  
  elif result in range(55,61):
    return "Garnet"  
  elif result in range(61,66):
    return "Alexandrite"  
  elif result in range(66,71):
    return "Topaz"  
  elif result in range(71,76):
    return "Bloodstone"  
  elif result in range(76,80):
    return "Sapphire"  
  elif result in range(80,90):
    return "Diamond"
  elif result in range(90,95):
    return "Fire Opal"
  elif result in range(95,98):
    return "Ruby"  
  else:
    return "Emerald"
  

def get_gem():
  name = gem_name()
  gemType, value = gem_value()
  
  msg = value + "gp   " + name + "(" + gemType +")"
  
  return msg

def get_jewelry():
  ''' obtains the name and value of jewelry and returns it as a string'''
  value = die_roller(2,8)*100
  result = die_roller(1,100)
  jewelType = ""
  
  if result in (1,2,3,4,5,6):
    jewelType = 'Anklet'
  elif result in(7,8,9,10,11,12):
    jewelType = "Belt"
  elif result in (13,14):
    jewelType = 'Bowl'
  elif result in (15,16,17,18,19,20,21):
    jewelType = 'Bracelet'
  elif result in (22,23,24,25,26,27):
    jewelType = 'Brooch'
  elif result in (28,29,30,31,32):
    jewelType = 'Buckle'
  elif result in (33,34,35,36,37):
    jewelType = 'Chain'
  elif result in (38,39,40):
    jewelType = 'Choker'
  elif result in (41,42):
    jewelType = 'Circlet'
  elif result in (43,44,45,46,47):
    jewelType = 'Clasp'
  elif result in (48,49,50,51):
    jewelType = 'Comb'
  elif result == 52:
    jewelType = 'Crown'
  elif result in (53,54,55):
    jewelType = 'Cup'
  elif result in (56,57,58,59,60,61,62):
    jewelType = 'Earring'
  elif result in (63,64,65):
    jewelType = 'Flagon'
  elif result in (66,67,68):
    jewelType = 'Goblet'
  elif result in (69,70,71,72,73):
    jewelType = 'Knife'
  elif result in (74,75,76,77):
    jewelType = 'Letter Opener'
  elif result in (78,79,80):
    jewelType = 'Locket'
  elif result in (81,82):
    jewelType = 'Medal'
  elif result in (83,84,85,86,87.88,89):
    jewelType = 'Necklace'
  elif result == 90:
    jewelType = 'Plate'
  elif result in (91,92,93,94,95):
    jewelType = 'Pin'
  elif result == 96:
    jewelType = 'Sceptre'
  elif result in (97,98,99):
    jewelType = 'Statuette'
  else:
    jewelType = 'Tiara'
    
  return jewelType + "  " + str(value) + "gp"

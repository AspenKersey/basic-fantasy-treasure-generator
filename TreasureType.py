# TreasureType.py
# Thorin Schmidt
# 9/16/2018

from random import randint

def percent_less_than(num):
  if randint(1, 100) <= num:
    return True
  else:
    return False

def die_roller(num, sides):
  total = 0
  for i in range(num):
    total += randint(1, sides)
  return total

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
  
  return (copper, silver, electrum, gold, platinum, gems, jewels, magic)

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
  
  return (copper, silver, electrum, gold, platinum, gems, jewels, magic)

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
  '''none'''
  
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
  
  return (copper, silver, electrum, gold, platinum, gems, jewels, magic)

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
  
  return (copper, silver, electrum, gold, platinum, gems, jewels, magic)

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
  
  return (copper, silver, electrum, gold, platinum, gems, jewels, magic)

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
  
  return (copper, silver, electrum, gold, platinum, gems, jewels, magic)

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
  '''none'''
  
  #silver
  '''none'''
  
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
  
  return (copper, silver, electrum, gold, platinum, gems, jewels, magic)

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
  
  return (copper, silver, electrum, gold, platinum, gems, jewels, magic)


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
  '''none'''
  
  #silver
  '''none'''
  
  #electrum
  '''none'''
  
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
  
  return (copper, silver, electrum, gold, platinum, gems, jewels, magic)


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
  '''none'''
  
  #gold
  '''none'''
  
  #platinum
  '''none'''
  
  #gems
  '''none'''
  
  #jewelry
  '''none'''
  
  #magic items
  '''none'''
  
  return (copper, silver, electrum, gold, platinum, gems, jewels, magic)


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
  '''none'''
  
  #platinum
  '''none'''
  
  #gems
  '''none'''
  
  #jewelry
  '''none'''
  
  #magic items
  '''none'''
  
  return (copper, silver, electrum, gold, platinum, gems, jewels, magic)


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
  '''none'''
  
  #silver
  '''none'''
  
  #electrum
  '''none'''
  
  #gold
  '''none'''
  
  #platinum
  '''none'''
  
  #gems
  if percent_less_than(50):
    gems += die_roller(1,4)
  
  #jewelry
  '''none'''
  
  #magic items
  '''none'''
  
  return (copper, silver, electrum, gold, platinum, gems, jewels, magic)


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
  '''none'''
  
  #silver
  '''none'''
  
  #electrum
  '''none'''
  
  #gold
  if percent_less_than(90):
    gold += die_roller(4,10)100
  
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
  
  return (copper, silver, electrum, gold, platinum, gems, jewels, magic)


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
  
  return (copper, silver, electrum, gold, platinum, gems, jewels, magic)


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
    
  return (copper, silver, electrum, gold, platinum, gems, jewels, magic)


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
  
  return (copper, silver, electrum, gold, platinum, gems, jewels, magic)


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
  
  return (copper, silver, electrum, gold, platinum, gems, jewels, magic)


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
  
  return (copper, silver, electrum, gold, platinum, gems, jewels, magic)


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
  
  return (copper, silver, electrum, gold, platinum, gems, jewels, magic)


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
  
  return (copper, silver, electrum, gold, platinum, gems, jewels, magic)


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
  
  return (copper, silver, electrum, gold, platinum, gems, jewels, magic)


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
  
  return (copper, silver, electrum, gold, platinum, gems, jewels, magic)


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
  
  return (copper, silver, electrum, gold, platinum, gems, jewels, magic)


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
  if percent_less_than(-1):
    platinum += die_roller(0,0)*100
  
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


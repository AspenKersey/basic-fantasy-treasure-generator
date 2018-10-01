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
  #copper
  if percent_less_than(50):
    copper += die_roller(5,6)
  if percent_less_than(60):
    silver += die_roller(5,6)
  if percent_less_than(40):
    electrum += die_roller(5,4)
  if percent_less_than(70):
    gold += die_roller(10,6)
  if percent_less_than(50):
    platinum += die_roller(1,10)
  return (copper, silver, electrum, gold, platinum)



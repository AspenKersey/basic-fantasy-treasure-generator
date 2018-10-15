# Dice.py
# Thorin Schmidt
# 10/15/2018

'''central project file for dice rolling functions'''

from random import randint

def die_roller(num, sides):
    total = 0
    for i in range(num):
        total += randint(1, sides)
    return total

def d4(plus = 0):
    ''' returns a random value plus any modifier '''
    result = randint(1,4) + plus
    if result < 1:
        result = 1
    return result

def d6(plus = 0):
    ''' returns a random value plus any modifier '''
    result = randint(1,6) + plus
    if result < 1:
        result = 1
    return result

def d8(plus = 0):
    ''' returns a random value plus any modifier '''
    result = randint(1,8) + plus
    if result < 1:
        result = 1
    return result

def d10(plus = 0):
    ''' returns a random value plus any modifier '''
    result = randint(1,10) + plus
    if result < 1:
        result = 1
    return result

def d12(plus = 0):
    ''' returns a random value plus any modifier '''
    result = randint(1,12) + plus
    if result < 1:
        result = 1
    return result

def d20(plus = 0):
    ''' returns a random value plus any modifier '''
    result = randint(1,20) + plus
    if result < 1:
        result = 1
    return result

def d100(plus = 0):
    ''' returns a random value plus any modifier '''
    result = randint(1,100) + plus
    if result < 1:
        result = 1
    return result

#testing
if __name__ == '__main__':
    print("rolling a d4:  ", d4())
    print("rolling a d6:  ", d6())
    print("rolling a d8:  ", d8())
    print("rolling a d10: ", d10())
    print("rolling a d12: ", d12())
    print("rolling a d20: ", d20())
    print("rolling a d100:", d100())
    print()
    print("rolling a d4-1:  ", d4(-1))
    print("rolling a d6+2:  ", d6(+2))
    print("rolling a d8-3:  ", d8(-3))
    
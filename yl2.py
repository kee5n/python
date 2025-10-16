# yl2
# Kirjuta programm, mis küsib kasutajalt raadiuse ja arvutab ringi pindala ja ümbermõõdu. (math.pi)

import math

rad = int(input('Raadius: '))

p = (2 * math.pi * rad)

s = (math.pi * rad * rad)

print('Ümbermõõt', round(p), 'cm')

print('Pindala', round(s), 'cm')

# õpetaja
# from math import pi
# r = int(input('Sisesta raadius: '))

# p = 2 * pi * r
# print('Ümbermõõt on. ', round(p, 3))

# s = pi * r ** 2
# print('Pindala on:', round(s, 3))
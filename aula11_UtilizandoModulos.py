#import math
from math import sqrt, ceil, pow


num = int(input('Digite um número: '))

raiz = sqrt(num)

print(f'Número {num} - Raiz {ceil(raiz)}')

print(f'Pot: {pow(num, 3)}')
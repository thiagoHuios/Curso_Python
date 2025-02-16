#import math
print('='*8, 'Primeira maneira de fazer', '='*8)
from math import trunc
nr = float(input('Digite um número real, para obter seu valor inteiro: '))
print('O número {}, tem a orção inteira de: {}'.format(nr, trunc(nr)))

print('='*8, 'Segunda maneira de fazer', '='*8)
num = float(input('Digite um número: '))
print('O número {}, tem sua inteira sendo: {:.0f}'.format(num, num))

print('='*8, 'Terceira maneira de fazer', '='*8)
num = float(input('Digite um número: '))
print('O número {}, tem sua inteira sendo: {}'.format(num, int(num)))

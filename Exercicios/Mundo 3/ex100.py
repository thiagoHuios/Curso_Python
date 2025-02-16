from random import randint
from time import sleep

def sorteio(lst):
    print('Sorteando 5 valores da lista:', end=' ')
    for s in range(0 ,5):
        n = randint(1, 10)
        print(n, end=' ')
        lst.append(n)
        sleep(0.5)
    print('Pronto!')

def somapar(lst):
    s = 0
    for l in lst:
        if l % 2 == 0:
            s += l
    return s

numeros = list()

sorteio(numeros)
print(f'Somando os valores {numeros}, temos: {somapar(numeros)}')
import random

quat = int(input('Insira o tamanho da tupla: '))
ate = int(input('Até qual número deve ser pensado aleatoriamente? '))

b = ()

for c in range(0, quat):
    a = (random.randrange(ate),)
    b = b + a

print(f'\nA tupla gerada aleatoriamente foi: \n{b}\n')
print(f'O maior valor da tupla foi: {max(b)} \nE o menor foi: {min(b)}')
    
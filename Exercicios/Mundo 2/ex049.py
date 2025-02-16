print('tabuada')

from time import sleep

while True:
    try:
        num = int(input('Digite um número para ver sua tabuada: '))
        break

    except ValueError:
        print('Insira um número inteiro!')

print('='*20)

for t in range(0, 11):
    print('{} x {:2} = {}'.format(num, t, num * t))
    sleep(0.25)

print('='*20)

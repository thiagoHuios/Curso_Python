import random, time
print('Advinhador de Números')
time.sleep(0.5)
print('Vou pensar em um número entre 1 e 10, e você tenta adivinhar, certo?')
time.sleep(1)
print('Lá vou eu então!')
time.sleep(1)
num = random.randint(0 , 10)
print('Pensando em um número...')
time.sleep(2)
adivinhação = int(input('Tente adivinhar qual numero pensei: '))
time.sleep(0.5)
print('Verificando...')
time.sleep(1)

cont = 0

while adivinhação != num:
    print('Que pena, você errou!')
    time.sleep(0.5)
    print('Tente novamente, até acertar!')
    adivinhação = int(input('Tente adivinhar qual numero pensei: '))
    cont += 1

print('Parabéns, você acertou!!!')
time.sleep(0.5)
print('Eu pesei no número: {}'.format(num))

if cont == 1:
    print('Vocé acertou de priemira em! \nMeus parabens!!!')
else:
    print('Vocé tentou {} vezes, até acertar! \nMais sorte na próxima!'.format(cont))

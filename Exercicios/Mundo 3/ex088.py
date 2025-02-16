import random, time

palpite = []
palpites = []
ciclo = True
contador_palpite = 0

print(f'-' * 40 , f'\n{'MEGA SENA':^40} \n' + '-' * 40)

while True:
    try:
        qtd = int(input('Insira quantos palpetes serão gerados: '))
        break
    except ValueError:
        print('Insira um valor válido!')

print('-' * 40)

while len(palpites) != qtd:
    while contador_palpite != 6:
        num = random.randrange(1, 60)
        if num not in palpite:
            palpite.append(num)
            contador_palpite += 1
    palpites.append(palpite[:])
    palpite.clear()
    contador_palpite = 0

for i, p in enumerate(palpites):
    print(f'JOGO {(i + 1):>2}: {p}')
    time.sleep(0.5)

print('-' * 40)


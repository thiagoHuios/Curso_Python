import time, random

time.sleep(0.5)

times = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional', 'São Paulo', 'Corrinthians',
         'Bahia', 'Cruzeiro', 'Vasco', 'Vitória', 'Atletico-MG', 'Fluminense', 'Grêmio', 'Juventude', 'Bragantino',
         'Athletico Paranaense', 'Criciúma', 'Altético-GO', 'Cuiabá')

time.sleep(0.5)

time_aleaorio = random.choice(times)

print('Os times do Brasileirão 2024 são:')

for t in times:
    print(t)

print('\nOs primeiros 5 cololacos do Brasileirão 2024 são: \n')

time.sleep(0.5)

for cinc in range(0, 6):
    print(f'{times[cinc]}')

time.sleep(0.5)

print('\nOs ultimos 4 cololacos do Brasileirão 2024 são: \n')

time.sleep(0.5)

for quat in range(3, -1, -1):
    print(f'{times[quat]}')

print('')

time.sleep(0.5)

print(sorted(times))

time.sleep(0.5)

print(f'\nO time {time_aleaorio} está na posição {times.index(time_aleaorio) + 1} \n')

while True:
    posição_escolhida = str(input('Insira uma posição para saber qual time é: '))
    if posição_escolhida.isdigit():
        posição_escolhida = int(posição_escolhida)
        if 20 > posição_escolhida < 1:
            print('Insira uma posição entre 1 e 20!')
        else:
            break

print(f'\nA possição {posição_escolhida}º está ocupada pelo {times[posição_escolhida - 1]}')
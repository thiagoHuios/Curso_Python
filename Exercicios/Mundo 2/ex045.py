from time import sleep
from random import choice
print('\033[1;33m' + '-'*20 + 'JOKENPÔ' + '-'*20, '\033[m')
print('\033[1;36m'+'VAMOS VER SE VOCê CONSEGUE GANAHAR DE MIM!', '\033[m')
sleep(1)
pedra = 'PEDRA'
papel = 'PAPEL'
tessoura = 'TESSOURA'

print('\33[35m' + '='*20, '\033[m')

escolha = str(input('Escolha entre pedra, papel ou tessoura: ')).lower().strip()

while escolha not in ['pedra', 'papel', 'tessoura']:
    print('Você que necessariamente esolher entre: pedra, papel ou tessoura')
    sleep(1.5)
    escolha = str(input('Tente novamente: '))

print('vamos ver quem é o melhor! ')

print('\33[35m' + '='*20, '\033[m')

sleep(1.5)
print('Agora e a minha vez de escolher!')
sleep(1)
print('Escolhendo...')
sleep(1.5)
escolha_maquina = choice(['pedra', 'papel', 'tessoura'])

print('\33[35m' + '='*20, '\033[m')
sleep(1)

if escolha == 'pedra' and escolha_maquina == 'tessoura':
    print(f'{'\033[1;32m'}Droga! Você venceu... Eu escolhi {escolha_maquina}')
if escolha == 'pedra' and escolha_maquina == 'pedra':
    print(f'{'\033[1;33m'}Quase! Foi um empate... Eu também escolhi {escolha_maquina}')
if escolha == 'pedra' and escolha_maquina == 'papel':
    print(f'{'\033[1;31m'}HAHAHAHA eu vencei!!! Eu escolhi {escolha_maquina}')

if escolha == 'tessoura' and escolha_maquina == 'papel':
    print(f'{'\033[1;32m'}Droga! Você venceu... Eu escolhi {escolha_maquina}')
if escolha == 'tessoura' and escolha_maquina == 'tessoura':
    print(f'{'\033[1;33m'}Quase! Foi um empate... Eu também escolhi {escolha_maquina}')
if escolha == 'tessoura' and escolha_maquina == 'pedra':
    print(f'{'\033[1;31m'}HAHAHAHA eu vencei!!! Eu escolhi {escolha_maquina}')

if escolha == 'papel' and escolha_maquina == 'pedra':
    print(f'{'\033[1;32m'}Droga! Você venceu... Eu escolhi {escolha_maquina}')
if escolha == 'papel' and escolha_maquina == 'papel':
    print(f'{'\033[1;33m'}Quase! Foi um empate... Eu também escolhi {escolha_maquina}')
if escolha == 'papel' and escolha_maquina == 'tessoura':
    print(f'{'\033[1;31m'}HAHAHAHA eu vencei!!! Eu escolhi {escolha_maquina}')

print('\33[35m' + '='*20, '\033[m')
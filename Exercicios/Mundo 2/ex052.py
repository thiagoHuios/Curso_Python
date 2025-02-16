print('Leitor de Números Primos')

while True:
    try:
        num = int(input('Insira um número inteiro para saber se ele é primo: '))
        break
    except ValueError:
        print('Insira um valor inteiro valido! ')

if num < 2:
    print(f'O número {num}, NÃO É PRIMO')

else:
    for primo in range(2, (num)):
        if num % primo == 0:
            print(f'O número {num}, NÃO É PRIMO')
            break
    else:
        print(f'O número {num}, É PRIMO')

#solução proposta pelo exercicio

num = int(input('Digite um número: '))

tot = 0

for p in range(1, (num +1)):
    if num % p == 0:
        tot += 1
if tot == 2:
    print(f'O número {num}, É PRIMO')
else:
    print(f'O número {num}, NÃO É PRIMO')



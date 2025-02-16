while True:
    num = int(input('Insira um número para ver sua tabuada: '))
    if num < 0:
        print('TABUADA ENCERRADA!')
        break
    print('-' * 20)
    for tabuada in range(1, 11):
        print(f'{num} x {tabuada} = {num * tabuada}')
    print('-' * 20)
from time import sleep

def maior(* num):
    if len(num) <= 0:
        ma = qtd = 0
    else:
        ma = max(num)
        qtd = len(num)

    print('-' * 60)
    print('Analisando os valores passados...')
    for t in num:
        if qtd == 0:
            print(0, end=' ')
        else:
            print(t, end=' ')
    print(f'Foram informados {qtd} valores ao todo. \nO maior valor informado foi {ma}')
    sleep(0.5)

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

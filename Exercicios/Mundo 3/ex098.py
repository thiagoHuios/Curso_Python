def contagem(a, b, c):
    test = 0
    if c == 0:
        c = 1
    if a > b and c > 0:
        c = -(c)
        test = b
    elif a < b and c < 0:
        c = abs(c)
        test = b
    elif b > a or a > b:
        test = b
    print(f'Contagem {a} até {b} de {abs(c)} em {abs(c)}')
    for c in range(a, b, c):
        print(c, end=' ')
    if test != 0:
        print(test, end=' ')
    print('Fim!')


print('=' * 40)
print('Contagem de 1 até 10 de 1 em 1')
contagem(1, 10, 1)
print('=' * 40)
print('Contagem de 10 até 0 de 2 em 2')
contagem(10, 0, -2)
print('=' * 40)
print('Agora é a sua vez de personalizar a contagem!')
while True:
    try:
        In = int(input('Início: '))
        Fim = int(input('Fim:    '))
        Pas = int(input('Passo:  '))
        break
    except ValueError:
        print('Insira um valor válido!')
print('=' * 40)
contagem(In, Fim, Pas)

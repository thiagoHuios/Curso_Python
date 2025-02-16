tamanho_tupla = int(input('Insira o tamanho da tupla desejada: '))

tupla = ()
tupla_par = ()

for c in range(1, tamanho_tupla + 1):
    a = (int(input(f'Insira o {c} valor da tupla: ')),)
    tupla += a

print('')
print(tupla, '\n')

if tupla.count(9) == 1:
    print(f'O valor 9, apareceu {tupla.count(9)} vez')
elif tupla.count(9) == 0:
    print('Não houve nenhum número 9')
else:
    print(f'O valor 9, apareceu {tupla.count(9)} vezes')

if 3 not in tupla:
    print('Não houve aparição do número 3')
else:
    print(f'A primeira aparição do valor 3 foi na posição de: {tupla.index(3) + 1}')

for par in range(0, tamanho_tupla):
    if tupla[par] % 2 == 0:
        b = (tupla[par],)
        tupla_par += b

if len(tupla_par) == 1:
    print(f'O unico valor par da tupla foi: {tupla_par[0]}')
elif len(tupla_par) == 0:
    print('Não existe números pares nessa tupla!')
else:
    print(f'Os valores pares da tupla foram: {tupla_par}')
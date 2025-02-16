print('{:=^80} \n'.format(' TESTADOR DE VOGAIS '))

tupla_palavras = ()

tupla = ('banana', 'maca', 'laranja', 'morango', 'abacaxi', 'uva', 'melao', 'pera', 'kiwi', 'goiaba', 'mamao',
         'cabeludinha', 'caju', 'tamarindo', 'ameixa', 'coco', 'figo')

while True:
    try:
        qtd_palavras = int(input('Insira quantas palavras quer testar [Ou insira 0 para usar o padrão]: '))
        break
    except ValueError:
        print('Insira uma valor válido!')

print(''+'\n'+'-'*80+'\n')

if qtd_palavras != 0:
    for pa in range(1, (qtd_palavras + 1)):
        palavras_escolidas = input(f'Insira a {pa}º palavras: ').lower().strip()
        tupla_palavras += (palavras_escolidas,)
    escolha = tupla_palavras
    print(''+'\n'+'-'*80)
else:
    escolha = tupla
    print(''+'\n'+'-'*80, end='')

for a in escolha:
    print(f'\nNa palavra: {a}, temos as seguintes vogais: ', end='')
    for letra in a:
        if letra in 'aeiou':
            print(letra, end=' ')

print('\n'+'-'*80+'\n')

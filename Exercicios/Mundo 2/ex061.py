print('Calculador de Progressão Arritimedica')

primeiro_termo = int(input('Insira o priemiro termo da PA: '))
razão = int(input('Insira a razão da PA: '))
numero_termos = int(input('Insira o número de PA: '))

ultimo_termo = primeiro_termo + (numero_termos - 1) * razão

print('Com o primeiro termo: {}, e a razão de: {}'.format(primeiro_termo, razão))
print(primeiro_termo, end=' ')

while primeiro_termo != ultimo_termo:
    primeiro_termo += razão
    print(primeiro_termo, end=' ')

#forma alternativa:

cont = 1
termo = primeiro_termo

while cont < numero_termos:
    print('{} ->'.format(termo), end=' ')
    cont += 1
    termo += 1
print('FIM')

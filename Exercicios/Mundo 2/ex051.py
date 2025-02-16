print('Calculador de Progressão Arritimedica')

while True:
    try:
        primeiro_termo = int(input('Insira o priemiro termo da PA: '))
        razão = int(input('Insira a razão da PA: '))
        numero_termos = int(input('Insira o número de PA: '))
        break
    except ValueError:
        print('Insira o um valores interios validos!')

print('Com o primeiro termo: {}, e a razão de: {} \nTemos a seguinte PA:'.format(primeiro_termo, razão))

ultimo_termo = primeiro_termo + (numero_termos - 1) * razão

for pa in range(primeiro_termo, (ultimo_termo + razão), razão):
    print(pa, end=' ')
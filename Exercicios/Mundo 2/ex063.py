qtd = int(input('Insira quantos números da sequência de fibonatti quer ver: '))

count = 3
primeiro_termo = 0
segundo_termo = 1
resultado = 0
total = 0
mais_termos = qtd

print('0 1', end=' ')

while qtd != 0:
    total += mais_termos
    while count <= total:
        count += 1
        resultado = primeiro_termo + segundo_termo
        primeiro_termo = segundo_termo
        segundo_termo = resultado
        print(resultado, end=' ')
        if count == total + 1:
            print(resultado)
        else:
            print(resultado, end=' ')
    qtd = int(input('Insira quantos número  a mais quer ver ou insira [0] para finalizar: '))

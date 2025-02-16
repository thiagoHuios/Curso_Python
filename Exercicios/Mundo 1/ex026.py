print('Achador da letra A')
frase = str(input('Digite uma frase: ')).lower().strip()
print('A quantidade de vezes que a letra A aparece é: {}'.format(frase.count('a')))
print('A primeira vez que a letra A aparece, ela está na posição: {}'.format(frase.find('a')+1))
print('A ultima vez que a letra A aparece, ela está na posição: {}'.format(frase.rfind('a')+1))
#O uso de "R" ou "L" pode alterar o intervalo de ação, como o r fazendo de tras para frente, e l sendo normal

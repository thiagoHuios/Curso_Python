print('Leitor de palindromos')

frase = str(input('Insira a frase: ')).lower().strip()
frase_sem_espaço = frase.replace(' ', '')

s =''

for p in range(len(frase_sem_espaço) -1, -1, -1):
    s += frase_sem_espaço[p]
if frase_sem_espaço == s:
    print(f'{frase}, {s} \nÉ um Palindromo!')
else:
    print(f'{frase}, {s} \nNão é um Palindromo!')

#forma alternativa:

print('Leitor de palindromos')

frase = str(input('Insira a frase: ')).lower().strip()
frase_sem_espaço = frase.replace(' ', '')
inverso = frase_sem_espaço[::-1]

if frase_sem_espaço == s:
    print(f'{frase}, {s} \nÉ um Palindromo!')
else:
    print(f'{frase}, {s} \nNão é um Palindromo!')
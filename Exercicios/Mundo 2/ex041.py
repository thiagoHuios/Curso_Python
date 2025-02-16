from datetime import date
print('Classificação de Categoria')
nascimento = int(input('Insira o ano de nascimento: '))
idade = (date.today().year - nascimento)

while idade > 120:
    nascimento = int(input('Insira o ano de nascimento valido: '))

print('Com uma idade de {} anos, sua classificação  é:'.format(idade))
if idade <= 9:
    print('Sua classificação é: Mirim')
elif idade <= 14:
    print('Sua classificação é: Infantil')
elif idade <= 19:
    print('Sua classificação é: Junior')
elif idade <= 25:
    print('Sua classificação é: Sênior')
else:
    print('Sua classificação é: Master')
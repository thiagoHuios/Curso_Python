from datetime import date
print('Veirificação de Alistamento')
print('Vamos validar quando tempo falta pra você se alistar, se você já pode se alistar ou se ja faz tempo que você deveria se alistar, ')
nasc = int(input('Insira seu ano de nascimento: '))
idade = date.today().year - nasc

print('Quem nasceu em {}, tem atualmente {} anos.'.format(nasc, idade, date.today().year))

if idade == 18:
    print('Você deve se alistar esse ano!')
elif idade > 18:
    print('Você já deveria ter se {} anos atras, em {}.'.format((idade - 18), (nasc + 18)))
elif idade < 18:
    print('Você deverá se alistar daqui {} anos, em {}.'.format((18 - idade), (nasc + 18)))


print('Calculador de IMC')
peso = float(input('Insira seu peso em Kg: '))
altura = float(input('Insira sua altura em metros: '))
imc = peso / (altura * altura)

print('Com o peso de {} Kg e uma altura de {} metros. Seu IMC é: {:.1f}'.format(peso, altura, imc))

if imc <= 18.5:
     print('Com a classificação de: Abaixo do Peso')
elif imc <= 25:
    print('Com a classificação de: Peso ideal')
elif imc <= 30:
    print('Com a classificação de: Sobrepeso')
elif imc <= 40:
    print('Com a classificação de: Obesidade')
elif imc > 40:
    print('Com a classificação de: Obesidade Mobida')

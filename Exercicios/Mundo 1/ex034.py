print('Calculador de aumento de salario')
salario = float(input('Insira o valor do sálario: '))
if salario > 1250.00:
    print('O salario de R${:.2f}, receberá um aumento de R${:.2f} \nSerá ajustado para: R${:.2f}'.format(salario, (salario * 0.10), (salario * 0.10 + salario)))
else:
    print('O salario de R${:.2f}, receberá um aumento de R${:.2f} \nSerá ajustado para: R${:.2f}'.format(salario, (salario * 0.15), (salario * 0.15 + salario)))
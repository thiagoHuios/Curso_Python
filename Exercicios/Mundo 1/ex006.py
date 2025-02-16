print('Vou calcular o dobro, o triplo e a raiz quadrada donúmero da sua esolha')
n=int(input('Digite algum número:'))
d=n*2
t=n*3
r=n**(1/2)
print('O dobro de seu número é: {} \nO triplo equivale a: {} \nE sua raiz é: {:.2f}'.format(d, t, r))
#utilizando o "\n" e possivel quebrar quebrar a frase de um print; E também e possivel fundir dois print's usuando o comando (end=' ')
#Para utlização da potêntencia e da raiz pode se usar "pow" que também se faz:
#Por exeemplo:
#print('E sua raiz é: {:.3f}'.format(pow(n, (1/2))))

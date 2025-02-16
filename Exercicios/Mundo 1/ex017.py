import math
print('Calculador de hipotenusa')
co = float(input('Digite o comprimento do Cateto Oposto em cm: '))
ca = float(input('Digite o comprimento do Cateto Adjacente em cm: '))
h = math.hypot(co, ca)
print('O valor da hipotenusa de um triangulo retangulo com o catetos sendo {}cm e {}cm \nTem o valor de: {:.2f}cm'.format(co, ca, h))

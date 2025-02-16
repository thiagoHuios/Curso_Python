import math
print('Calculador de Seno, Cosseno e Tangente')
an= float(input('Digite o valor de um angulo: '))
sen = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print('Os valores de Seno, Cosseno e Tangente do angulo {:.2f}, são: \nSeno: {:.2f} \nCosseno: {:.2f} \nTangente: {:.2f}'.format(an, sen, cos, tan))

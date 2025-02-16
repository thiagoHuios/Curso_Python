print('Area de Pintura')
print('Para saber quantos litros de tinta precisa para pintar uma parede, vamos precisar saber seu tamanho')
ap=float(input('QUal a altura da parede em metros:'))
lp=float(input('Qual a largura da parede em metros:'))
area=ap*lp
ql=area/2
print('Com uma area de {:.2f}m², são necesasrios {:.2f} litros de tinta'.format(area, ql))

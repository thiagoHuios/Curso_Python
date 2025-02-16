retas = list(map(float, input('Insira três comprimentos de retas, para saber se é possivel formar um trinagulo: ').split()))
if retas[0] + retas[1] > retas[2] and retas[0] + retas[2] > retas[1] and retas[1] + retas[2] > retas[0]:
    print('Os valores de: {} \nPodem formar um triangulo.'.format(retas,))
else:
    print('Os valores de: {} \nNão podem formar um triangulo.'.format(retas))


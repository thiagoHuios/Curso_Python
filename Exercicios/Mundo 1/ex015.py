dias=int(input('Por quantos dias o carro foi alugado? '))
k=float(input('Quantos quilometros foram percorridos? '))
print('O valor do aluguel de {} dias, rodando por {}Km, é de {:.2f}:'.format(dias, k, (dias * 60) + (k * 0.15)))
#pd= dias * 60
#pk= k * 0.15
#v = (dias * 60) + (k * 0.15)
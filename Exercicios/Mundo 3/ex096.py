def area(a, b):
    s = a * b
    return s

larg = float(input('Insira a largura  em metros do terrano: '))
comp = float(input('Insira o comprimento em metros do terreno: '))
print('-' * 40)
print(f'A área do terro é de: {area(larg, comp)} m²')
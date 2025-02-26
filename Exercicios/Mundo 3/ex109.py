from utilitários import moedas

while True:
    try:
        num = int(input("Insira o preço a ser analisado: "))
        break
    except ValueError:
        print("Insirá um valor válido!")

while True:
    try:
        op = int(input("Insira o valor para aumentar e dimnuir baseado no preço: "))
        break
    except ValueError:
        print("Insirá um valor válido!")

while True:
    adp = str(input("Deseja fazer a adaptação para moeda automarica? [S/N]: ")).lower().strip()[0]
    if adp in "SsNn":
        if adp == 's':
            adp = True
        else:
            adp = False
        break


print(f"O número: R${num:.2f}, tem:")
print(f"Dobro: {moedas.dobro(num, adp)}")
print(f"Metade: {moedas.metade(num, adp)}")
print(f"Aumentado: {moedas.aumentar(num, op, adp)}")
print(f"Diminuido: {moedas.dimunuir(num, op, adp)}")

from utilitários import moedas

while True:
    try:
        num = int(input("Insira o preço a ser analisado: "))
        break
    except ValueError:
        print("Insirá um valor válido!")

print(f"O número: R${num:.2f}, tem:")
print(f"Dobro: {moedas.adaptação(moedas.dobro(num))}")
print(f"Dobro: {moedas.adaptação(moedas.metade(num))}")

while True:
    try:
        op = int(input("Insira o valor para aumentar e dimnuir: "))
        break
    except ValueError:
        print("Insirá um valor válido!")

print(f"Dobro: {moedas.adaptação(moedas.aumentar(num, op))}")
print(f"Dobro: {moedas.adaptação(moedas.dimunuir(num, op))}")

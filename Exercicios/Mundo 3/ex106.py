def linha(txt):
    n = len(txt) + 4
    print("~" * n)
    print(f"{txt:^{n}}")
    print("~" * n)

while True:
    linha("SISTEMA DE AJUDA PyHELP")
    fun = str(input("Função ou Biblioteca > ")).strip()
    if fun == 'fechar':
        print("Programa encerrado!")
        break
    linha(F"ACESSANDO MANUAL DO COMANDO {fun}")
    print(help(fun))
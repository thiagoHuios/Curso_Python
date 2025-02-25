def fatorial(a=0, show=False):
    f = 1
    for fat in range(a, 0, -1):
        f *= fat
        if show == True:
            if fat == 1:
                print(f"{fat} =", end=' ')
            else:
                print(f"{fat} x", end=' ')
    print(f)


while True:
    try:
        fa = int(input("Insira o numero para ver seu fatorial: "))
        fa = abs(fa)
        break
    except ValueError:
        print("Insira um valor válido!")

while True:
    des = str(input("Deseja ver a base do calculo? [S/N]: ")).lower().strip()[0]
    if des in "SsNn":
        if des == "s":
            des = True
            break
        else:
            des = False
            break
    print("Selecione uma opção válida!")

fatorial(fa, des)
    
            
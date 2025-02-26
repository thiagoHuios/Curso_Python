def adaptação(num):
    r = f'R${num:.2f}'
    return r

def dobro(n, adp=False):
    n *= 2
    if adp:
        return adaptação(n)
    else:
        return n

def metade(n, adp=False):
    n /= 2
    if adp:
        return adaptação(n)
    else:
        return n

def aumentar(n, a, adp=False):
    r = (n + (n *(a / 100)))
    if adp:
        return adaptação(r)
    else:
        return r

def dimunuir(n, d, adp=False):
    r = (n - (n *(d / 100)))
    if adp:
        return adaptação(r)
    else:
        return r
    
def resumo(n, a, d):
    print("-" * 40)
    print('RESUMO DO VALOR'.center(40))
    print("-" * 40)
    print(f"Preço Analisado: \t{adaptação(n)}")
    print(f"Dobro do Preço: \t{dobro(n, True)}")
    print(f"Metade do Preço: \t{metade(n, True)}")
    print(f"{a}% de Aumento: \t{aumentar(n, a, True)}")
    print(f"{d}% de Redução: \t{dimunuir(n, d, True)}")
    print("-" * 40)
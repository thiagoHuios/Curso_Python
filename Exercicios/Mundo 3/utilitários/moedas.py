def adaptação(txt):
    return f"R${txt:.2f}"

def dobro(n, adp=True):
    n *= 2
    if adp == True:
        return adaptação(n)
    else:
        return n

def metade(n, adp=True):
    n /= 2
    if adp == True:
        return adaptação(n)
    else:
        return n

def aumentar(n, a, adp=True):
    r = (n + (n *(a / 100)))
    if adp == True:
        return adaptação(r)
    else:
        return r

def dimunuir(n, d, adp=True):
    r = (n - (n *(d / 100)))
    if adp == True:
        return adaptação(r)
    else:
        return r
    
def resumo(n, a, d):
    print("-" * 40)
    print(f"{'RESUMO DO VALOR':^40}")
    print("-" * 40)
    print(f"{'Preço Analisado: ':<20}{adaptação(n)}")
    print(f"{'Dobro do Preço: ':<20}{dobro(n)}")
    print(f"{'Metade do Preço: ':<20}{metade(n)}")
    print(f"{f'{a}% de Aumento: ':<20}{aumentar(n, a)}")
    print(f"{f'{d}% de Redução: ':<20}{dimunuir(n, d)}")
    print("-" * 40)
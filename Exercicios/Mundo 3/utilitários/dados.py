from asyncio.proactor_events import BaseProactorEventLoop


def leiadinheiro(lista):
    resp = list()
    for l in lista:
        valido = True
        while valido:
            n = str(input(l)).replace(',','.').strip()
            if n.isalpha() or n == "":
                print("Valor invalido!")
            else:

                valido = False
                resp.append(float(n))
    return resp

def leiaint(txt):
    banana = True
    while banana:
        while
            try:
                n = int(input(txt))
                break
            except va

def leiafloat(txt):
    while True:
        try:
            n = float(input(txt))
            break
        except ValueError or TypeError:
            if "n" not in locals():
                n = 0
                break
            print("O valor inserido precisas ser um número decimal ou inteiro!")
    return n



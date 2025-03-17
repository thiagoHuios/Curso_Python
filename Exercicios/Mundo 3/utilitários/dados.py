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
    while True:
        try:
            n = int(input(txt))
        except (ValueError, TypeError):
            print("INsira um número inteiro válido!")
        except KeyboardInterrupt:
            print("Entrada de dados interompida pela usuário!")
            return 0
            continue
        else:
            return n

def leiafloat(txt):
    while True:
        try:
            n = float(input(txt))
        except (ValueError, TypeError):
            print("INsira um número inteiro válido!")
        except KeyboardInterrupt:
            print("Entrada de dados interompida pela usuário!")
            return 0
            continue
        else:
            return n


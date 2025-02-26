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



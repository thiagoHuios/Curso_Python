def notas(* num, sit=False):

    '''->Função feita para analisar notas de alunos, e sua aituação.
    :param num: Uma ou mais notas de alunos
    :param sit: valor opcional para saber a situação do alluno em boleano.
    :return: diciolnario  com varias informações  sobre a situação da turma'''
    lista_notas = [*num]
    sala = dict()
    sala["Total de Notas"] = len(lista_notas)
    sala["Maior Nota"] = max(lista_notas)
    sala["Menor Nota"] = min(lista_notas)
    sala["Média das Notas"] = sum(lista_notas) / len(lista_notas)
    if sit == True:
        if sala["Média das Notas"] >= 7:
            sala["Situação das Notas"] = "BOA"
        elif sala["Situação das Notas"] >= 5.5:
            sala["Situação das Notas"] = "RAZOAVEL"
        else:
            sala["Situação das Notas"] = "RUIM"

    return sala

resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(f"Total de notas foi: {resp}")
help(notas)

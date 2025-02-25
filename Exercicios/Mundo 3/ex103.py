def ficha(nome="Nome_Jogador", gols="Número_Gols"):
    if nome == '':
        nome = "<Desconhecido>"
    if gols == '':
        gols = 0
    return print(f"O jogador {nome} fez {gols} gol's no campeonato.")

name = str(input("Insira o nome do jogador: "))
gol = str(input("Número de Gols: "))

ficha(name, gol)
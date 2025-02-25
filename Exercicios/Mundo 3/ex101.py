def voto(num=0):
    from datetime import datetime
    ano_atual = datetime.today().year
    idade = ano_atual - nasc

    if idade < 18:
        return print(f"Com a idade de: {idade} anos, NÂO VOTA")
    elif idade > 65:
        return print(f"Com a idade de: {idade} anos, VOTO OPCIONAL")
    else:
        return print(f"Com a idade de: {idade} anos, VOTO OBRIGATORIO")

while True:
    try:
        nasc = int(input("Insira o ano de nascimento: "))
        break
    except ValueError:
        print("Insira uma data válida!")
print("-" * 40)
voto(nasc)


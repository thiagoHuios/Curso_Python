def LeiaInt(frase):
    while True:
        num = str(input(frase)).strip()
        if num.digit():
            break
        print("Insira um número inteiro!")

n = LeiaInt("Insira um número: ")
print(f'O número digitado foi: {n}')

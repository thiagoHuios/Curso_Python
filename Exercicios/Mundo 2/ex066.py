cont = soma = 0

while True:
    num = int(input('Insira um número [Insira 999 para finalizar!]: '))
    if num == 999:
        break
    cont += 1
    soma += num

print(f'''A soma dos {cont} números, foi: {soma}''')
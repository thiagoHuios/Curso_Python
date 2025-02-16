import colorsys
print('Radar Eletronico')
velocidade = float(input('Qual a velocidade atual: '))
if velocidade > 80:
    print('Você foi multado node: R${:.2f}. O limite da via é 80 km/h'.format((velocidade-80)*7))

print('Tenha um bom dia! Dirija com segurança!')

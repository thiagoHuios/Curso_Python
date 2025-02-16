print('Calculador de preço de viagem')
km = float(input('Digite distancia da viagem em Km: '))
#maneira curta que eu achie
if km > 200:
    if km == int(km):
        preço = int(km) * 0.45
    else:
        preço = km * 0.45
else:
    if km == int(km):
        preço = int(km) * 0.5
    else:
        preço = int(km) * 0.5

print('O valor cobrado por uma viagem de {} km, é: R${:.2f}'.format(km, preço))

#maneira longa que eu achei
'''if km >= 200:
    if km == int(km):
        print('O valor cobrado por uma viagem de {:.0f} km, é: R${:.2f}'.format(km, (int(km) * 0.45)))
    else:
        print('O valor cobrado por uma viagem de {} km, é: R${:.2f}'.format(km, km * 0.45))
else:
    if km == int(km):
        print('O valor cobrado por uma viagem de {:.0f} km, é: R${:.2f}'.format(km, (int(km) * 0.5)))
    else:
        print('O valor cobrado por uma viagem de {} km, é: R${:.2f}'.format(km, (km * 0.5)))'''


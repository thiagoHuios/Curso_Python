TC = float(input('Informe a temperatura em ºC:'))
TF = (TC * 9 / 5) + 32
TK = TC + 273.15
print('A temperatura de {:.2f}°C, corresponde a {:.2f}°F'.format(TC, TF))
print('A temperatura de {:.2f}°C , corresponde a {:.2f}°K'.format(TC, TK))

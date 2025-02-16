print('Sua cidade começa com Santo?')
cid = str(input('Digite o nome completo da sua cidae: ').strip())
print('Sua cidade começa com Santo: {}'.format(cid[:5].lower() == 'santo'))

print('Interpretador de Nomes')
nome = str(input('"Digite seu nome completo: ')).strip()
print('Seu nome com todas as letras maiúsculas: {}'.format(nome.upper()))
print('Seu nome com todas as letras minúsculas: {}'.format(nome.lower()))
#Minha forma de solução:
quebra_nome = nome.split()
print('Seu nome tem: {} letras, desconsiderando espaços'.format(len(''.join(quebra_nome))))
print('Seu primeiro nome {}, tem: {} letras'.format(quebra_nome[0], len(quebra_nome[0])))
#forma proposta pela atividade:
#print('Seu nome completo tem: {} letras, desconsiderando os espaços'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome, tem {} letras'.format(nome.find(' ')))

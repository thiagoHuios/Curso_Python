print('Interpretador de Nomes')
nome = str(input('Digite seu nome completo: ')).strip()
nome_quebrado = nome.split()
print('Seu primeiro nome é: {}'.format(nome_quebrado[0]))
#minha solução
print('Seu ultimo nome é: {}'.format(nome_quebrado[-1]))
#Solução proposta pela atividade
#print('Seu ultimo nome é: {}'.format(nome_quebrado[len(nome_quebrado)-1]))

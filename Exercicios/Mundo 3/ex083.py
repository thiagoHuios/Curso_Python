print(f'{'Analisador de parenteses de expressões númericas':-^80}')

expressão_lista = []

expressão = str(input('\nInsira a expressão a ser analisada: '))
for e in range(0, len(expressão)):
    a = expressão[e]
    expressão_lista.append(a)

contador_parentese_esq = expressão_lista.count('(')
contador_parentese_dir = expressão_lista.count(')')

if contador_parentese_dir != contador_parentese_esq:
    print('\nSua expressão está errada!')
else:
    print('Sua expressão está válida!')

#solução alternativa (mais eficiente para a proposta

pilha = []

expr = str(input('Digite a expressão: '))
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está invalida!')
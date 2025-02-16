def escreva(txt):
    tamanho = len(txt) + 4
    print('~' * tamanho)
    print(f'{txt:^{tamanho}}')
    print('~' * tamanho)


escreva('Curso em Vídeo')

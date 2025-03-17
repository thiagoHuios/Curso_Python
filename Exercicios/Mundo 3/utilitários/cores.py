'''cores = {'limpa':'\033[m',
         'branco':'\033[30m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'amarelo':'\033[33m',
         'azul':'\033[34m',
         'roxo':'\033[35m'}'''

def branco(txt):
    r = f'{'\033[30m'}{txt}{'\033[m'}'
    return r

def vermelho(txt):
    r = f'{'\033[31m'}{txt}{'\033[m'}'
    return r

def verde(txt):
    r = f'{'\033[32m'}{txt}{'\033[m'}'
    return r

def amarelo(txt):
    r = f'{'\033[33m'}{txt}{'\033[m'}'
    return r

def azul(txt):
    r = f'{'\033[34m'}{txt}{'\033[m'}'
    return r

def roxo(txt):
    r = f'{'\033[35m'}{txt}{'\033[m'}'
    return r

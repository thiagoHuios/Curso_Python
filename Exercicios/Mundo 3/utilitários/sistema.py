from utilitários.cores import azul, verde
from utilitários.dados import leiaint

def linha(num=40):
    return print("-" * num)

def cabeçalio(txt):
    linha()
    print(txt.center(42))
    linha()

def menu(lista):
    cabeçalio("MENU PRINCIPAL")
    for i, l in enumerate(lista):
        print(f'{i + 1} - {azul(l)}')
    print("-" * 40)
    while True:
        op = leiaint(verde("Insira sua opção: "))
        if len(lista) > op > 0 :
            break
        print("Insira uma opção válida!")
    return op


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome='bancoDadosEx115.txt'):
    if arquivoExiste("bancoDadosEx115.txt"):
        'arquivo já existente'
    else:
        try:
            a = open(nome, 'wt+')
        except:
            print("Houve um erro ná criação do arquivo!")


def lerArquivo(nome='bancoDadosEx115.txt'):
    criarArquivo()
    try:
        a = open(nome, "rt")
    except:
        print("Erro ao ler o arquivo!")
    else:
        cabeçalio("PESSOAS CADASTRADOS")
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} Anos')
    finally:
        a.close()


def cadastrarPessoa(arq='bancoDadosEx115.txt', nome='Desconheciddo', idade=0):
    criarArquivo()
    nome = str(input("Insira o nome da pessoa: "))
    idade = leiaint("Insira a idade da pessoa: ")
    try:
        a = open(arq, 'at')
    except:
        print("Erro ao ler o arquivo!")
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print("Erro ao inserir os dados!")
        else:
            print(f'{nome} cadastrado com sucesso!')
            a.close()
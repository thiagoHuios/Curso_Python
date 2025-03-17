from utilitários import sistema, dados

while True:
    resp = sistema.menu(["Ver pessoas cadrastradas", "Cadrastrar Pessoas", "Sair do sistema"])
    if resp == 1:
        sistema.lerArquivo()
    elif resp == 2:
        sistema.cadastrarPessoa()
    else:
        sistema.cabeçalio("SAINDO DO SISTEMA")
        exit()
        break
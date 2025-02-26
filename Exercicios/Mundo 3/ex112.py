from utilitários import moedas, dados

num = dados.leiadinheiro(["Insira o preço a ser analisado: ", "Insira o valor para aumentar: ", "Insira o valor para dimnuir: "])
moedas.resumo(num[0], num[1], num[2])
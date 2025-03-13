from utilitários import moedas, dados

respInt = dados.leiaint("Insira um numero inteiro: ")
moedas.resumo(respInt, 20, 20)
respFloat = dados.leiafloat("Insira um número decimal: ")
moedas.resumo(respFloat, 20, 20)


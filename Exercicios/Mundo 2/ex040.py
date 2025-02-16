print('Validação de Notas')
print('Insiras as notas, para saber a média e aprovação do aluno:')
nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))
média = (nota1 + nota2) / 2
print('O aluno com as nota de {} e {}, tem a média de: {}'.format(nota1, nota2, média))

if média <= 5.0:
    print('Irá ser reprovado pois sua média 5.0')
elif média >= 7.0:
    print('Irá ser aprovado, pois sua média é superior a 7.0')
elif 5.0 < média < 6.9:
    print('Irá pra reculperação, pois média é inferior a 7.0 e superior a 6.9')

sexo = str(input('[M] Masculino \n[F] Fenino \nInsira qual o sexo: ')).strip().upper()[0]

while sexo not in ['M', 'F']:
    print('Insira uma opção valida!')
    sexo = str(input('[M] Masculino \n[F] Fenino \nInsira qual o sexo: ')).strip().upper()

if sexo == 'M':
    print(f'A opção escolhida foi Masculino')
else:
    print(f'A opção escolhida foi Feminino')

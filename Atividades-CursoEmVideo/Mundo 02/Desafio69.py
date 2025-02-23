mais18 = 0
qtdMan = 0
Mulm20 = 0

while True:

  print(20*'---')
  print('CADASTRE UMA PESSOA')
  print(20*'---')

  idade = int(input("Idade: "))
  sexo = input("Sexo (M/F): ").capitalize()
  
  if (idade > 18):
    mais18 += 1
  if (sexo == 'M'):
    qtdMan += 1
  if ((idade < 20) and (sexo == 'F')):
    Mulm20 += 1

  print(20*'---')
  cont = input("Quer continuar? [S/N] ").capitalize().strip()
  if cont == 'N':
    break
  
print(f'Total de pessoas com mais de 18 anos: {mais18}.')
print(f'Ao todo, temos {qtdMan} homens cadastrados.')
print(f'E temos {Mulm20} mulher(es) com menos de 20 anos.')
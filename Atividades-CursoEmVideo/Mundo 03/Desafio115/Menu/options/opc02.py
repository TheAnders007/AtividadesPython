from cores import cor
from Menu.options.pessoascad import pessoascad

def opc02():
    print(50*f'{cor["white"]}-')
    print('{:^50}'.format('NOVO CADASTRO'))
    print(50*'-')
    nome = input(f"Nome: {cor['green']}")   
    while True:
      try:
        idade = int(input(f"{cor['white']}Idade: {cor['green']}"))
      except ValueError:
        print(f"{cor['red']}Digite um valor válido!")
      else:
         break
    pessoascad.append([nome, idade])
    print(f"{cor['white']}Novo registro de {nome} adicionado!")

    
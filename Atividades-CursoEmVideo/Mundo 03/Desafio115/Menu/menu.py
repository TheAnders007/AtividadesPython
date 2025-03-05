from cores import cor
from Menu.option import option

def menu():
  while True:
    print(50*'-')
    print('{:^50}'.format('MENU PRINCIPAL'))
    print(50*'-')
    print(f"{cor['yellow']}1 {cor['white']}- {cor['blue']}Ver Pessoas Cadastradas")
    print(f"{cor['yellow']}2 {cor['white']}- {cor['blue']}Cadastrar Nova Pessoa")
    print(f"{cor['yellow']}3 {cor['white']}- {cor['blue']}Sair do Sistema {cor['white']}")
    print(50*'-')
    if option() == False:
      break
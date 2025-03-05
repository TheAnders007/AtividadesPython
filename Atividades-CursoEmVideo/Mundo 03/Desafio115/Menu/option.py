from cores import cor
from Menu.options.opc03 import opc03
from Menu.options.opc01 import opc01
from Menu.options.opc02 import opc02

def option():
    while True:
      try:
        opc = int(input(f"{cor['yellow']}Sua opção: {cor['green']}"))
        if (opc not in [1, 2, 3]):
          print(f"{cor['red']}Digite uma opção válida!")
        else:
           if opc == 1:
              opc01()
           if opc == 2:
              opc02()
           if opc == 3:
              opc03()
              return False
           break
      except KeyboardInterrupt:
         print(f"{cor['red']}Usuário interrompeu o programa! {cor['white']}")
         return False
      except ValueError:
        print(f"{cor['red']}Digite um valor inteiro!")
      
      
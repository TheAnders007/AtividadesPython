from cores import cor

def leiaInt(texto=''):
    while True:
      try:
        print(cor['white'], end='')
        n = int(input(texto))
      except (ValueError, TypeError):
        print(cor['red'], end='')
        print('ERRO! Há problemas com o tipo de dado informado')
        continue
      except KeyboardInterrupt:
         print(cor['red'], end='')
         print('\nEntrada de dados interrompida pelo usuário')
         return 0
      else:
         return n

def leiaFloat(texto=''):
    while True:
      try:
        print(cor['white'], end='')
        n = float(input(texto))
      except (ValueError, TypeError):
        print(cor['red'], end='')
        print('ERRO! Há problemas com o tipo de dado informado')
        continue
      except KeyboardInterrupt:
         print(cor['red'], end='')
         print('\nEntrada de dados interrompida pelo usuário')
         return 0 
      else:
         return n
      
intei = leiaInt('\033[0mDigite um número inteiro: \033[32m')
real = leiaFloat('\033[0mDigite um número real: \033[32m')
print(f'\033[0mVocê acabou de digitar o número inteiro {intei} e o número real {real}.')
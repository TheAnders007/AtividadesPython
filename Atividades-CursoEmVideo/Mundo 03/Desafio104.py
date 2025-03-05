def leiaInt(texto=''):
    while True:
      n = input(texto)
      if n.isnumeric():
         break
      else:
         print('\033[31mERRO! Digite um número inteiro válido!\033[0m')
    return n
      
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
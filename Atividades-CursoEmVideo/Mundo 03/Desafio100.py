from random import randint

numeros = list()

def sorteia(list):
    print("Sorteando 5 valores para a lista: ", end='')
    for x in range (0, 5):
        sort = randint(0,25)
        list.append(sort)
        print(sort, end=' ')
    print('PRONTO')

def somaPar(list):
    vsumPar = 0
    for num in list:
        if (num % 2 == 0): vsumPar+=num
    print(f"Somando os valores pares de {numeros}, temos {vsumPar}")

sorteia(numeros)
somaPar(numeros)
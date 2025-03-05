from random import randint

tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print("Valores sorteados:", end=' ')
for num in tupla:
    print(num, end=' ')

print('\nO menor valor sorteado foi', min(tupla), 'e o maior foi', max(tupla))
from random import randint
from time import sleep

vals = {'jogador 1': randint(1, 10),
        'jogador 2': randint(1, 10),
        'jogador 3': randint(1, 10),
        'jogador 4': randint(1, 10) }

print("Valores Sorteados:")
for key, val in vals.items():
    sleep(1)
    print(f'      O {key} tirou {val}')

print("Ranking dos Jogadores:")

for n in range (1, 5):
   maiVal = 0
   maiJog = ''
   for key, val in vals.items():
       if val > maiVal:
           maiVal = val
           maiJog = key
   print(f'      {n}° Lugar: {maiJog} com {vals[maiJog]}')
   del(vals[maiJog])
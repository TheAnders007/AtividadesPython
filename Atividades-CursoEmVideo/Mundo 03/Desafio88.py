from random import randint

jogos = list()
palp = []

print(40*'-')
print('{:^40}'.format('JOGA NA MEGA SENA'))
print(40*'-')

qtdJog = int(input("Quantos jogos quer que eu sorteie? "))
print(f'-=-=-= SORTEANDO {qtdJog} JOGOS =-=-=-')

for v in range(1, qtdJog + 1):
    for num in range (0, 6):
        palp.append(randint(1, 60))
    palp.sort()
    jogos.append(palp)
    print(f'Jogo {v}: {jogos[v - 1]}')
    palp = []

print(f'-=-=-=-=-= BOA SORTE!! =-=-=-=-=-')
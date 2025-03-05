def ficha(nome='<desconhecido>', gols=0):
    return f'O jogador {nome} fez {gols} gol(s) no campeonato'

print(20 * '-')
jogador = input('Nome do Jogador: ').strip()
gols = input('Número de gols: ').strip()

if not gols.isnumeric() or gols == '':
    gols = 0
if jogador == '':
    print(ficha(gols=gols))
else:
    print(ficha(jogador, gols))




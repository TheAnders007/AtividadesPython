jogador = {'nome': input("Nome do Jogador: ")}
gols = list()

parts = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

for n in range(0, parts):
    gols.append(int(input(f'Quantos gols foram feitos na partida {n}? ')))

jogador['gols'] = gols
jogador['total'] = sum(gols)

print(30*'=-=')
print(jogador)
print(30*'=-=')

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

print(30*'=-=')
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])}')

for n in range (0, parts):
    print(f'     => Na partida {n}, fez {jogador["gols"][n]} gols.')
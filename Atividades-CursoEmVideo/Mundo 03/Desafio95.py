jogsList = list()

while True:
    print(30*'-')
    jogador = {'nome': input("Nome do Jogador: ")}
    gols = list()

    parts = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

    for n in range(0, parts):
        gols.append(int(input(f'Quantos gols foram feitos na partida {n}? ')))

    jogador['gols'] = gols
    jogador['total'] = sum(gols)
    
    jogsList.append(jogador)
    
    cont = input("Deseja continuar? (S/N) ")
    if cont in 'Nn':
        break

print(35*'=-=')
print(f"{'cod':^6}{'nome':^10}{'gols':^20}{'total':^16}")
print(50*'-')

for jogador in jogsList:
    print(f"{jogsList.index(jogador):^6}{jogador['nome']:^10}{str(jogador['gols']):^20}{jogador['total']:^16}")
    
while True:
    print(50*'-')
    codJog = int(input("Mostrar dados de qual jogador? (999 para parar) "))
    if codJog == 999:
        break
    elif codJog not in range(0, len(jogsList)):
        print(f"\nERRO! Não existe jogador com {codJog}. Tente novamente!")
    else:
      print(f"--- LEVANTAMENTO DO JOGADOR {jogsList[codJog]['nome']}:")
      for e, jogo in enumerate(jogsList[codJog]['gols']):
        print(f"    No jogo {e} fez {jogo} gols.")
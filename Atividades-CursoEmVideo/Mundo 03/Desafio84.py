pessoas = list()
maiPes = menPes = 0

while True:
    nome = input("Nome: ")
    peso = int(input("Peso: "))
    pessoas.append([nome, peso])
    cont = input("Quer continuar? (S/N) ")
    if cont in 'Nn':
        break

print(30*'=-=')
print("Ao todo, foram cadastradas", len(pessoas), "pessoas.")

for pes in pessoas:
    if (pes[1] > maiPes):
        maiPes = pes[1]
    elif (menPes == 0) or (pes[1] < menPes):
        menPes = pes[1]

print(f'O maior peso foi de {maiPes}Kg. Peso de ', end='')
for pes in pessoas:
    if(pes[1] == maiPes):
        print(f'[{pes[0]}]', end=' ')

print(f'\nO menor peso foi de {menPes}Kg. Peso de ', end='')
for pes in pessoas:
    if(pes[1] == menPes):
        print(f'[{pes[0]}]', end=' ')
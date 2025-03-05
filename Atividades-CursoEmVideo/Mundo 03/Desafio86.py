matriz = list()
linha = list()

for l in range (0, 3):
    for c in range (0, 3):
        val = int(input(f"Digite um valor para [{l}, {c}]: "))
        linha.append(val)
    matriz.append(linha)
    linha = []

print(30 * '=-=')

for l in matriz:
    for num in l:
        print(f'[  {num}  ]', end='')
    print()
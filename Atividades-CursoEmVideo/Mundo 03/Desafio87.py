matriz = list()
linha = list()

somaPar = sumCol3 = 0

for l in range (0, 3):
    for c in range (0, 3):
        val = int(input(f"Digite um valor para [{l}, {c}]: "))
        linha.append(val)
    matriz.append(linha)
    linha = []

print(30 * '=-=')

for l in matriz:
    sumCol3+= l[2]
    for num in l:
        print(f'[  {num}  ]', end='')
        if num % 2 == 0:
            somaPar+=num
    print()

print(30 * '=-=')
print("A soma dos valores pares é", somaPar)
print("A soma dos valores da terceira coluna é", sumCol3)
print("O maior valor da segunda linha é", max(matriz[1]))
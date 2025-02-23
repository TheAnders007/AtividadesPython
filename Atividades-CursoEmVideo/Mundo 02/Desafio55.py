lPesos = []

for x in range (1, 6):
  pes = float(input("Digite o peso (em Kg) da pessoa {}: ".format(x)))
  lPesos.append(pes)

print("O menor peso lido foi", min(lPesos), "Kg, enquanto o maior peso foi", max(lPesos), "Kg.")
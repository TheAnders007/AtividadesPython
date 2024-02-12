dist = int(input("Digite a distância em km de sua viagem: "))

if (dist <= 200):
    pas = 0.5 * dist
else:
    pas = 0.45 * dist

print("\nO preço da sua passagem será de R${:.2f}".format(pas))
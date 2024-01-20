num = input("Digite um número de 0 a 9999: ")
num = "000" + num

print("Unidade: " + num [len(num) - 1])
print("Dezena: "  + num [len(num) - 2])
print("Centena: "  + num [len(num) - 3])
print("Unidade de Milhar: " + num [len(num) - 4])
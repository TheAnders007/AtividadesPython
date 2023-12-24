qtdias = int(input("Quantos dias alugado? ")) 
qtdkm = int(input("Quantos Km rodados? "))

total = 60 * qtdias + 0.15 * qtdkm

print("\nO total a pagar é de R${:.2f}".format(total))
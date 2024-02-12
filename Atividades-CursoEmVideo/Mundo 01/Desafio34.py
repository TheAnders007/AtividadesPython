sal = int(input("Qual o salário do funcionário? R$"))
novosal = 0

if (sal > 1250):
    novosal = sal * 1.1
else:
    novosal = sal * 1.15

print("\nQuem ganhava R${:.2F} passa a receber R${:.2f} agora.".format(sal, novosal))    
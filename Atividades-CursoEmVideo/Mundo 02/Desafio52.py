num = int(input("Digite um número: "))
cont = 0

for x in range (1, num + 1):
    if ((num % x == 0)):
        cont += 1
        print('\033[31m', end='')
    else:
        print('\033[93m', end='')
    print(x, end=" ")

print('\033[0m')
if (cont == 2):
    print("\nO número", num, "foi divisível 2 vezes, então é primo.")
else:
    print("\nO número", num, "foi divisível", cont, ", então não é primo.")
num = int(input("Digite um número inteiro: "))

conv = int(input("\nEscolha a base de conversão\n1 - Binário\n2 - Octal\n3 - Hexadecimal\n"))

if (conv == 1):
    numConv = bin(num)
    print("\n{} em binário é {}!".format(num, numConv[2:]))
elif (conv == 2):
    numConv = oct(num)
    print("\n{} em octal é {}!".format(num, numConv[2:]))
elif (conv == 3):
    numConv = hex(num)
    print("\n{} em hexadecimal é {}!".format(num, numConv[2:]))
else:
    print("Escolha um número válido")

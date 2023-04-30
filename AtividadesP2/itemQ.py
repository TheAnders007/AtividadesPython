# Verificar se um número é Quadrado Perfeito

Num = int(input("Digite um número: "))

for x in range (1, Num + 1):
    if (x ** 2 == Num):
        print("Ele é um quadrado perfeito.")
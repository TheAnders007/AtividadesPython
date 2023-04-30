#divisores de K

K = int(input("Digite o valor de K: "))

for x in range(1, K + 1):
    if (K % x == 0):
        print (x)
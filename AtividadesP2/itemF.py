#múltiplos de 3 e 5 num intervalo [A, B]

#entrada de dados do usuário
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

for x in range (A, B + 1):
    if (x % 3 == 0 and x % 5 == 0):
        print (x)
        #foi chamada a estrutura de seleção IF para saber se a divisão de x tanto por 3 como por 5 dava resto 0.
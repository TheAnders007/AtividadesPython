soma = 0
cont = 0

for v in range(1, 7):
    n = int(input("Digite o {} valor inteiro: ".format(v)))
    if n % 2 == 0:
        cont+=1
        soma = soma + n

print ("\nO valor da soma dos", cont ,"números pares informados é", soma)
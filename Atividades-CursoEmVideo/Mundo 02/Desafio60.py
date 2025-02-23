n = int(input("Digite um número inteiro para ter fatorial calculado: "))
v = n
fat = 1

print ('Calculando {}! = '.format(n), end="")
while (v != 1):
    print (v, end= ' X ')
    fat = fat * v
    v-=1

print("1")
print("\nO fatorial de {} é igual a {}.".format(n, fat))
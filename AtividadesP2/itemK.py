K = int(input("Digite o valor de K: "))

somaDiv = 0
for x in range(1, K + 1):
    if (K % x == 0):
        somaDiv = somaDiv + x
        #toda vez que x for um divisor de K, o valor será armazenado na variável Somadiv que somará o número mais a soma dos outros divisores, sendo que no final resultará na soma de todos os divisores.
        
        
print (somaDiv)

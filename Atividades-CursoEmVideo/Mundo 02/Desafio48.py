soma = 0
qtd = 0

for n in range (1, 501):
    if (n % 2 == 1) and (n % 3 == 0):
        qtd = qtd + 1
        soma = soma + n

print('A soma de todos os', qtd, 'números é', soma)
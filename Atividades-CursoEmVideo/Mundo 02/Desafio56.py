listPessoas = []
somaIdade = 0
maiorIdadeH = 0
homvelho = ''
qtdmulnova = 0

for p in range (1, 5):
    nome = input("Diga o nome da pessoa {}: ".format(p))
    idade = int(input("Informe a idade da pessoa {}: ".format(p)))
    sexo = input("Informe o sexo (M ou F) da pessoa {}: ".format(p))
    listPessoas.append([nome, idade, sexo])
    print()

for el in listPessoas:
    somaIdade = somaIdade + el[1]
    if el[2] == 'M':
        if el[1] > maiorIdadeH:
            maiorIdadeH = el[1]
            homvelho = el[0]
    elif el[2] == 'F':
        if el[1] < 20:
            qtdmulnova += 1

print("A média das idades das 4 pessoas é {:.1f}".format(somaIdade/4))
print('O homem mais velho é o', homvelho, 'com', maiorIdadeH, 'anos')
print('A quantidade de mulheres menores de 20 anos é', qtdmulnova)

    


qtd = soma = 0

while True:
    num = int(input("Digite um número: "))
    if num == 999:
        break
    qtd += 1
    soma += num

print(f"Foram digitados {qtd} números, sendo o valor de sua soma {soma}.")
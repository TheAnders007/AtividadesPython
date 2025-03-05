listNum = []

while True:
    num = int(input("Digite um valor: "))
    if num not in listNum:
        listNum.append(num)
        print("Valor adicionado com sucesso...")
    elif num in listNum:
        print("Valor duplicado! Não irei adicionar!")
    
    cont = input("Deseja continuar? (S/N) ").upper().strip()
    if cont == 'N':
        break

print(30 * '-=-')
listNum.sort()
print('Você digitou os valores', listNum)
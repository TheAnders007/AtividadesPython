listNum = []

while True:
    num = int(input("Digite um valor: "))
    listNum.append(num)
    cont = input("Deseja continuar? (S/N) ").upper().strip()
    if cont == 'N':
        break

listNum.sort(reverse=True)

print(f"\nForam digitados {len(listNum)} números")
print(f"Lista de Números em ordem decrescente: {listNum}")
if 5 in listNum:
    print("O valor 5 está na lista!")
else:
    print("O valor 5 não está na lista!")
listNum = []
listPar = []
listImpar = []

while True:
    num = int(input("Digite um valor: "))
    listNum.append(num)
    if num % 2 == 0:
        listPar.append(num)
    else:
        listImpar.append(num)
    cont = input("Deseja continuar? (S/N) ").upper().strip()
    if cont == 'N':
        break

print("\nLista Completa:", listNum)
print("Lista de números pares:", listPar)
print("Lista de números ímpares:", listImpar)
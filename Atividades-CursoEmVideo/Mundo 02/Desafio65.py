cont = ''
listNum = []

while (cont.title() != "N"):
    num= int(input("Digite um número: "))
    cont = input("Deseja continuar [S/N]? ")
    listNum.append(num)

print("Você digitou {} números e a média foi {:.2f}".format(len(listNum), sum(listNum)/len(listNum)))
print("O maior valor foi", max(listNum), "e o menor foi", min(listNum))
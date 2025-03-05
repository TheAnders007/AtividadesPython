listNum = []

for x in range (0,5):
    val = int(input("Digite um valor: "))
    if (len(listNum) == 0) or (val >= max(listNum)):
        listNum.append(val)
    else:
        for y in range (0, len(listNum)):
            if val < listNum[y]:
                listNum.insert(listNum.index(listNum[y]), val)
                break
    print("Adicionado na posição", listNum.index(val), "da lista...")

print(listNum)
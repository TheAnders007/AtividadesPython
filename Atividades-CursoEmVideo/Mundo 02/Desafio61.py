a1 = int(input("Diga o primeiro termo da PA: "))
raz = int(input("Informe a razão da PA: "))

print("\nOS 10 PRIMEIROS ELEMENTOS DA PA SÃO:")
novoElem = a1

while (novoElem != (a1 + 10*raz)):
    print(novoElem, end=' -> ')
    novoElem = novoElem + raz

print('ACABOU')
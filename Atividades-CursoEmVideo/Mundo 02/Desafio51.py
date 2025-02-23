a1 = int(input("Diga o primeiro termo da PA: "))
raz = int(input("Informe a razão da PA: "))

print("\nOS 10 PRIMEIROS ELEMENTOS DA PA SÃO:")
novoElem = a1

for e in range(0, 10):
    print(novoElem, end=' -> ')
    novoElem = novoElem + raz

print('ACABOU')
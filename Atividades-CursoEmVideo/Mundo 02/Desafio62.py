print("Gerador de PA")
print(10*'==-')

a1 = int(input("Diga o primeiro termo da PA: "))
raz = int(input("Informe a razão da PA: "))
novoElem = a1

contad = 0
conti = 10
total = 0

while (conti != 0):
    contad = 0
    while (contad < conti):
      print(novoElem, end=' -> ')
      novoElem = novoElem + raz
      contad+= 1
      total+=1
    print('PAUSA')
    conti = int(input("\nQuantos termos a mais você deseja ver? "))

print("\nACABOU! Foram mostrados", total, "termos.")


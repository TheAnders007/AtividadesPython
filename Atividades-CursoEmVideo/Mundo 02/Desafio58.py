from random import randint

comp = randint(0, 10)
user = 11
tent = 0

while comp != user:
  user = int(input("Entre 0 e 10, adivinhe o número que eu pensei: "))
  tent+=1
  if (comp == user):
   print("\nParabéns! Você ganhou!! Foram necessárias", tent, "tentativas.")
  else:
   if (comp > user):
      print("\nMais... Tente Novamente!".format(comp))
   if (comp < user):
      print("\nMenos... Tente Novamente!".format(comp))
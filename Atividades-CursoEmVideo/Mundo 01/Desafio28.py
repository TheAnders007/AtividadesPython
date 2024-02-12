from random import randint

comp = randint(0, 5)

user = int(input("Entre 0 e 5, adivinhe o número que eu pensei: "))

if (comp == user):
   print("\nParabéns! Você ganhou!!")
else:
   print("\nGANHEI! Eu pensei no {}. Boa sorte na próxima!".format(comp))
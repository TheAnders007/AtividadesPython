import random
import time

print("Suas Opções\n [1] Pedra\n [2] Papel\n [3] Tesoura\n")

esc = int(input("Qual a sua escolha?"))
comp = random.randint(1, 3)

if esc == 1:
    esc = 'Pedra'
elif esc== 2:
    esc = 'Papel'
elif esc==3:
    esc = 'Tesoura'
else:
    print("Número Inválido!")


if (esc in ["Pedra", "Papel", "Tesoura"]):
   print("\nJO")
   time.sleep(1)
   print("KEN")
   time.sleep(1)
   print("PO!!!\n")
   print(8*'==-')

   if comp == 1:
      print("Computador jogou Pedra.")
      print("Jogador jogou {}.".format(esc))
      print(8*'==-')
      if esc == "Pedra":
          print("EMPATE")
      if esc == "Papel":
          print("JOGADOR VENCE")
      if esc == "Tesoura":
          print("JOGADOR PERDE")

   if comp == 2:
      print("Computador jogou Papel.")
      print("Jogador jogou {}.".format(esc))
      print(8*'==-')
      if esc == "Pedra":
          print("JOGADOR PERDE")
      if esc == "Papel":
          print("EMPATE")
      if esc == "Tesoura":
          print("JOGADOR VENCE")

   if comp == 3:
      print("Computador jogou Tesoura.")
      print("Jogador jogou {}.".format(esc))
      print(8*'==-')
      if esc == "Pedra":
          print("JOGADOR VENCE")
      if esc == "Papel":
          print("JOGADOR PERDE")
      if esc == "Tesoura":
          print("EMPATE")       
          

        
        
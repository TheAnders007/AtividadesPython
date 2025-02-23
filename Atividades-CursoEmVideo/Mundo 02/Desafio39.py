from datetime import date

anoNasc = int(input("Qual seu ano de nascimento? "))

idade = date.today().year - anoNasc

if idade < 18:
  print("Faltam {} anos para ele precisar se alistar".format(18 - idade))
elif idade == 18:
  print("Está na hora de se alistar!")
else:
  print("Já se passaram {} anos desde o tempo do alistamento".format(idade - 18))
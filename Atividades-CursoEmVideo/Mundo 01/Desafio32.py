import datetime

ano = int(input("Que ano quer analisar? Se quiser analisar o ano atual, coloque 0: "))

if (ano == 0):
   ano = datetime.date.today().year



if (ano % 4 == 0):
    if(ano % 100 == 0):
       if (ano % 400 == 0):
          print(ano, "é bissexto.")
       else:
          print(ano, "não é bissexto.")
    else:
     print(ano, "é bissexto.")
else:
   print(ano, "não é bissexto.")
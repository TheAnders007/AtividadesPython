from datetime import date

anoNasc = int(input("Informe seu ano de nascimento: "))
idade = date.today().year - anoNasc
categ = ""

if(idade <= 9):
    categ = "Mirim"
elif idade <= 14:
    categ = "Infantil"
elif idade <= 19:
    categ = "Junior"
elif idade <= 20:
    categ = "Sênior"
else:
    categ = "Master"

print("O atleta tem {} anos e sua categoria é {}.".format(idade, categ))


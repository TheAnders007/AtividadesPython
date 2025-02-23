import datetime

listID = []
qtdMen = 0
qtdMai = 0

for v in range (1, 8):
    id = int(input("Digite o ano de nascimento da pessoa {}: ".format(v)))
    listID.append(id)

for idade in listID:
    if (datetime.date.today().year - idade >= 18):
        qtdMai+=1
    else:
        qtdMen+=1

print("\nDas 7 pessoas, há {} pessoas de maiores de idade e {} pessoas de menor.".format(qtdMai, qtdMen))
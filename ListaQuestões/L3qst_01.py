salAtual = salInic = 1000
anoAtual = int(input("Digite o ano atual: "))

for x in range (0, (anoAtual - 1995)):
    salAtual = float(salAtual + 2**x * (15/1000) * salAtual)

print(salAtual)   
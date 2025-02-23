n = 0
soma = 0
qtd = 0

while (n != 999):
  soma+= n
  qtd+= 1
  n = int(input("Digite um número (999 para parar): "))

print("Você digitou {} números e a soma entre eles foi {}.".format(qtd - 1, soma))
valCasa = int(input("Informe o valor da casa: R$"))
salario = int(input("Informe o salário do comprador: "))
qtdAnos = int(input("Em quantos anos ele irá pagar: "))

qtdMeses = qtdAnos * 12

if (valCasa/qtdMeses <= (0.3 * salario)):
    print("O valor da prestação mensal é R${:.2f}".format(valCasa/qtdMeses))
else:
    print("Empréstimo Negado!")
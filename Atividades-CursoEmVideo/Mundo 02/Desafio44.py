precoN = float(input("Informe o preço do produto: R$"))
precoF = 0

print (20 * '==*', "\nOpções de Pagamento\n\n1 - À vista no dinheiro ou cheque\n2 - À vista no cartão\n3 - Em até 2x no cartão\n4 - 3x ou mais no cartão\n")

pag = int(input("Informe sua forma de pagamento: "))

if (pag == 1):
    precoF = 0.9 * precoN
elif (pag == 2):
    precoF = 0.95 * precoN
elif (pag == 3):
    precoF = precoN
    qtdParc = int(input("Quantas parcelas? "))
    parcela = precoF/qtdParc
    print("\nSerão {} parcela(s) de R${:.2f}".format(qtdParc, parcela))
elif (pag == 4):
    precoF = precoN * 1.2
    qtdParc = int(input("Quantas parcelas? "))
    parcela = precoF/qtdParc
    print("\nIrão ser {} parcelas de R${:.2f}".format(qtdParc, parcela))
else:
    print("\nOpção Inválida! Tente novamente.")

if (pag in [1, 2 ,3 , 4]):
   print("\nO preço a ser pago é de R${:.2f}.".format(precoF))
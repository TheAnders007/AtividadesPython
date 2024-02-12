vel = int(input("Digite a velocidade atual do carro (km/h): "))

if (vel > 80):
    print("MULTADO! Limite de 80 km/h excedido. \nVocê deve pagar uma multa de R${}".format(7 * (vel - 80)))

print ("\nTenha um bom dia! Digija com segurança! :D")    
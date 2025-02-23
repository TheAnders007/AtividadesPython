peso = float(input("Informe o seu peso (kg): "))
alt = float(input("Informe sua altura (m): "))

imc = peso/(alt ** 2)

print("O seu IMC é de {:.2f}".format(imc))

if (imc < 18.5):
    print("Abaixo do Peso!")
elif(imc < 25):
    print("Peso Ideal!")
elif(imc < 30):
    print("Sobrepeso!")
elif(imc < 40):
    print("Obesidade!")
else:
    print("Obesidade Mórbida!")
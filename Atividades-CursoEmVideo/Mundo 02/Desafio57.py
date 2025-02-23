sexo = input("Informe o sexo de uma pessoa (M ou F): ").strip().upper()

while (sexo not in ['M','F']):
    sexo = input("\nVocê digitou um valor fora do listado. Informe novamente: ").strip().upper()
print("Sexo", sexo, "cadastrado com sucesso!")
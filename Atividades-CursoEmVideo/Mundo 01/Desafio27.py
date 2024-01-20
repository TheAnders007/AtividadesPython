nome = input("Digite seu nome completo: ").strip().title()

print("\nSeja bem vindo,", nome)
print("Seu primeiro nome é", nome.split() [0])
print("Seu último nome é", nome.split() [len(nome.split()) - 1])
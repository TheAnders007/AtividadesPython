nome = input("Digite seu nome completo: ")
nome = nome.strip()
print("Analisando seu nome...")


print("Seu nome em letras maiúsculas é" + nome.upper())
print("Seu nome em letras maiúsculas é" + nome.lower())
print("Seu nome tem ao todo", (len(nome) - nome.count(" ")), "letras")
print("Seu primeiro nome é {} e ele tem {} letras".format(nome.split() [0], len(nome.split() [0])))

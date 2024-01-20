frase = input("Digite uma frase: ").lower().strip()

print("\nA letra a aparece {} vezes na frase".format(frase.count("a")))
print("A primeira letra A aparece na posição", (frase.find("a") + 1))
print("A última letra A aparece na posição", (frase.rfind("a") + 1))
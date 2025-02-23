frase = input("Digite uma frase: ").lower().split()
frase = "".join(frase)
contra = ''

for letra in range(len(frase) - 1, -1, -1):
   contra = contra + frase[letra]

print("\nO contrário de", frase, "é", contra)

if (frase == contra):
    print("\nA frase é um PALÍNDROMO!")
else:
    print("\nA frase não é palíndromo.")

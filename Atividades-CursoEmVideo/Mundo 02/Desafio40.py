n1 = int(input("Nota 1: "))
n2 = int(input("Nota 2: "))

media = (n1 + n2)/2
print("\nA média do aluno é {:.2f}. Sua situação final é:".format(media))

if media < 5:
    print("Reprovado")
elif media >= 7:
    print("Aprovado")
else:
    print("Recuperação") 
from random import choice

al1 = input("Digite o nome do primeiro aluno: ")
al2 = input("Digite o nome do segundo aluno: ")
al3 = input("Digite o nome do terceiro aluno: ")
al4 = input("Digite o nome do quarto aluno: ")

listAlun = [al1, al2, al3, al4]

escol = choice(listAlun)

print("\nO aluno escolhido para apagar o quadro foi {}.".format(escol))
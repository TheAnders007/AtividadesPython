aluno = dict()

aluno['nome'] = input("Digite o nome do aluno: ")
aluno['média'] = float(input(f"Digite a média de {aluno['nome']}: "))

if (aluno['média'] >= 6):
    aluno['situação'] = 'Aprovado'
elif (3 < aluno['média'] < 6):
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

print(f"\nNome é igual a {aluno['nome']}\nMédia é igual a {aluno['média']}\nSituação de {aluno['nome']} está como {aluno['situação']}")
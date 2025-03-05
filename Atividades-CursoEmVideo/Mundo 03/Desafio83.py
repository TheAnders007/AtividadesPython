exp = input("Digite a expressão: ")
parents = ''

for carac in exp:
    if carac in '()':
        parents+= carac

for x in range (0, len(parents)):
    if '()' in parents:
        parents = parents.replace('()', '')
if parents == '':
    print("A expressão é válida!")
else:
    print("A expressão é inválida!")



listNum = [int(input("Diga o primeiro valor: ")), int(input("Diga o segundo valor: ")), int(input("Diga o terceiro valor: ")), int(input("Diga o quarto valor: ")), int(input("Diga o quinto valor: ")) ]

print(f"O maior valor digitado foi {max(listNum)}, que está nas posições ", end='')
for ind, num in enumerate(listNum):
    if num == max(listNum):
        print(f'{ind}...')

print(f"O menor valor digitado foi {min(listNum)}, que está nas posições ", end='')
for ind, num in enumerate(listNum):
    if num == min(listNum):
        print(f'{ind}...', end='')

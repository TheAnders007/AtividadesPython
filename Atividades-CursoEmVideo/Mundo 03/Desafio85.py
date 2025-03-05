nums = [[], []]

for x in range(1, 8):
    val = int(input(f'Digite o {x}o valor: '))
    if val % 2 == 0:
        nums[0].append(val)
    else:
        nums[1].append(val)

nums[0].sort()
nums[1].sort()

print("\nValores Pares Digitados:", nums[0])
print("Valores Ímpares Digitados:", nums[1])
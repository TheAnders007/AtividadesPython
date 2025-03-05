nums = (int(input("Digite o primeiro valor: ")), int(input("Digite o segundo valor: ")), int(input("Digite o terceiro valor: ")), int(input("Digite o quarto valor: ")))
print()



print(f"O valor 9 apareceu {nums.count(9)} vez(es)")
if 3 in nums:
  print(f"A posição do primeiro valor 3 foi a {nums.index(3) + 1}°")
else:
   print("O número 3 não está entre os valores digitados.")
print("Números Pares:", end= ' ')
for num in nums:
    if num % 2 == 0:
        print(num, end=' ')
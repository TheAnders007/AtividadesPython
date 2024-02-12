v1 = int(input("Primeiro valor: "))
v2 = int(input("Segundo valor: "))
v3 = int(input("Terceiro valor: "))

print()

if(v1 < v2 and v1 < v3):
    print("O menor valor digitado foi", v1)
if(v2 < v1 and v2 < v3):
    print("O menor valor digitado foi", v2)
if(v3 < v1 and v3 < v2):
    print("O menor valor digitado foi", v3)

if(v1 > v2 and v1 > v3):
    print("O maior valor digitado foi", v1)
if(v2 > v1 and v2 > v3):
    print("O maior valor digitado foi", v2)
if(v3 > v1 and v3 > v2):
    print("O maior valor digitado foi", v3)

n = int(input("Diga o número de termos: "))
print(30 * '~')
contad = 0
val = 0
ultval = 0
penval = 0

while (contad != n):
    if contad == 1:
        val = 1
    if contad > 1:
        val = ultval + penval
    contad+=1
    penval = ultval
    ultval = val
    print(val, end=" -> ")
print("FIM")
print(30 * '~')
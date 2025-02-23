while True:
    num = int(input("Digite um valor para verificar sua tabuada: "))
    if num < 0:
        break
    for x in range (1, 11):
        print(f"{num} x {x} = {num * x}")
    print()

print("Programa de tabuada encerrado! Volte sempre!")

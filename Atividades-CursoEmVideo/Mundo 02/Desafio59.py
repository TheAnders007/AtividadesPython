from time import sleep

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
op = 0

while(op !=5):
    print("\nMENU\n\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos Números\n[5] Sair do Programa")

    op = int(input("Qual opção deseja? "))
    
    print()
    if op == 1:
        print("A soma dos números é", (num1 + num2))
    if op == 2:
        print("O produto dos números é", (num1 * num2))
    if op == 3:
        print("O maior valor é", max([num1, num2]))
    if op == 4: 
        num1 = int(input("Digite o primeiro valor: "))
        num2 = int(input("Digite o segundo valor: "))
    if op == 5:
        print("Saindo do programa...")
        sleep(2)
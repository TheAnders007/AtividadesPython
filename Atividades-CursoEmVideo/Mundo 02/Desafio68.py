from random import randint

qtdVic = 0
print("VAMOS JOGAR PAR OU ÍMPAR\n")

while True:
 num = int(input("Digite um valor: "))
 parid = input("Par ou ímpar [P/I] ").capitalize().strip()
 comp = randint(1, 10)

 print(20 * "-")
 print(f'Você jogou {num} e o computador {comp}. Total de {num + comp} ', end='')

 if (num + comp) % 2 == 0:
    print('DEU PAR')
 elif (num + comp) % 2 == 1:
    print('DEU ÍMPAR')

 print(20 * "-")

 if ((((num + comp) % 2 == 0) and (parid=='P')) or ((num + comp) % 2 == 1) and (parid=='I')):
    qtdVic+=1
    print('Você VENCEU!\nVamos jogar novamente...\n')
 else:
    print('Você PERDEU!')
    break
 
print(f"GAME OVER! Você venceu {qtdVic} vezes")
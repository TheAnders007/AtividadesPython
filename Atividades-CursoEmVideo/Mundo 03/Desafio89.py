boletim = list()

while True:
    nome = input("Nome: ")
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    boletim.append([nome, [n1, n2]])

    cont = input("Deseja continuar? [S/N] ")
    if cont in 'Nn':
        break

print(40*'-=-')

print('No. NOME         MÉDIA')
print(30 * '-')

for aluno in boletim:
    print(f'{boletim.index(aluno)}{(4 - len(str(boletim.index(aluno)))) * " "}{aluno[0]}{(14 - len(aluno[0])) * " "}{sum(aluno[1])/2}')

while True:
  print(40 * '-')
  esc = int(input("Mostrar as notas de qual aluno? (999 interrompe): "))
  if esc == 999:
     print("FINALIZANDO...")
     print("<<< VOLTE SEMPRE!! >>>")
     break
  for aluno in boletim:
    if esc == boletim.index(aluno):
        print(f'As notas de {aluno[0]} são {aluno[1]}')
    else:
       print("Aluno não encontrado!")
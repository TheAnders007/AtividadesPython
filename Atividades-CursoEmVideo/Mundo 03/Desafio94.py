grupo = list()

SumIdade = 0

while True:
    pessoa = dict()
    pessoa['nome'] = input('Nome: ')
    pessoa['sexo'] = input('Sexo [M/F]: ').upper()
    pessoa['idade'] = int(input('Idade: '))
    grupo.append(pessoa)
    while True:
      cont = input("Quer Continuar (S/N)? ")
      if cont not in 'SsNn':
         print('ERRO! Responda com S ou N')
      else:
          break
    if cont in 'Nn':
        break

print(grupo)

print(40*'=-=')
print(f'- O grupo tem {len(grupo)} pessoas.')

for pessoa in grupo:
    SumIdade += pessoa['idade']

print(f'- A média de idade é de {SumIdade/len(grupo)} anos.')

print(f'- As mulheres cadastradas foram: ', end='')

for pessoa in grupo:
    if pessoa['sexo'] == 'F':
        print(f"[{pessoa['nome']}]", end=' ')

print('\n- Lista das Pessoas acima da Média: ')

for pessoa in grupo:
    if (pessoa['idade'] > SumIdade/len(grupo)):
      print()
      for k, v in pessoa.items():
        print(f'{k} = {v};', end=' ')
    print()
    

from datetime import date

trab = {'nome': input('Nome: '),
        'idade': date.today().year - int(input('Ano de Nascimento: ')),
        'ctps': int(input('Carteira de Trabalho (0 não tem): '))
        }

if trab['ctps'] != 0:
    trab['contratação'] = int(input('Ano de Contratação: '))
    trab['salário'] =  float(input('Salário: R$'))
    trab['aposentadoria'] = 35 - date.today().year + trab['contratação'] + trab['idade']

print(40 * '=-=')
for k, v in trab.items():
    print(f'   - {k} tem o valor {v}')

prods = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9)

print(40 * '-')
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print(40 * '-')

for x in range(0, len(prods), 2):
    print(f'{prods[x]}{(30 - len(prods[x])) * "."}R$ {prods[x + 1]:.2f}')
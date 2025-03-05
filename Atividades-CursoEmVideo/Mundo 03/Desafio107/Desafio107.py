from moeda import metade, dobro, aumentar, diminuir

p = float(input("Digite um preço: R$"))
print(f'A metade de {p} é {metade(p)}')
print(f'O dobro de {p} é {dobro(p)}')
print(f'Aumentando 10%, temos {aumentar(p, 10):.2f}')
print(f'Reduzindo 20%, temos {diminuir(p, 20):.2f}')
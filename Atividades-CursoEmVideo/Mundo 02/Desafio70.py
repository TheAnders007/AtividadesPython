compratot = prodsCaro = 0
prodBar = ['', 0]


print("LOJINHA")

while True:
    nomeProd = input("\nNome do Produto: ")
    preco = float(input("Preço: R$"))
    
    compratot += preco
    if (preco > 1000):
        prodsCaro+=1
    if (preco < prodBar[1] or prodBar[1] == 0):
        prodBar = [nomeProd, preco]

    cont = input("Quer continuar? [S/N] ").capitalize()
    if cont == 'N':
        break

print('\nFIM DO PROGRAMA\n')
print(f"O total da compra foi R${compratot:.2f}")
print(f"Temos {prodsCaro} produto(s) com valor acima de 1000 reais.")
print(f"O produto mais barato foi {prodBar[0]} com o preço {prodBar[1]:.2f} reais.")

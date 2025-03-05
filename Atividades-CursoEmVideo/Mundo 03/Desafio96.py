def area(larg, comp):
    print(f"A área de um terreno {larg} x {comp} é de {(larg*comp):.2f} m2.")
    
print('{:^30}'.format("CONTROLE DE TERRENOS"))
print(30 * '-')
    
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))

area(l, c)
def metade(val, form=False):
    if form:
       return f'R${(val/2):.2f}'.replace('.', ',')
    else:
       return val/2

def dobro(val, form=False):
    if form:
        return f'R${(val * 2):.2f}'.replace('.', ',')
    else:
        return val * 2

def aumentar(val, perc, form=False):
    if form:
        return f'R${(val * (1 + perc/100)):.2f}'.replace('.', ',')
    else:    
        return val * (1 + perc/100)

def diminuir(val, perc, form=False):
    if form:
        return f'R${(val * (1 - perc/100)):.2f}'.replace('.', ',')
    else:    
        return val * (1 - perc/100)

def moeda(val):
    return f'R${val:.2f}'.replace('.', ',')

def resumo(val, aum, dec):
    print(40*'-')
    print('{:^40}'.format('RESUMO DO VALOR'))
    print(40*'-')

    print('{:<30}{}'.format('Preço Analisado:', moeda(val)))
    print('{:<30}{}'.format('Dobro do preço:', moeda(val * 2)))
    print('{:<30}{}'.format('Metade do preço:', moeda(val/2)))
    print('{:<30}{}'.format(f'{aum}% de aumento:', moeda(aumentar(val, aum))))
    print('{:<30}{}'.format(f'{dec}% de redução:', moeda(diminuir(val, dec))))
    print(40*'-')

def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO' 
    elif 18 > idade >= 16:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'

print(20*'-')
ano = int(input("Em que ano você nasceu? "))    
print(voto(ano))

def fatorial(num = 0, show=False):
    """
      -> Calcula o Fatorial de um número
      :param num: Refere-se ao número que se deseja ter o fatorial calculado
      :param show: Caso verdadeiro, irá ser mostrado o passo a passo do produto do fatorial
      :return fat: Retorno do valor do fatorial de num
    """
    fat = 1
    for n in range (num, 0, -1):
        if show:
            if n > 1:
              print(f'{n} x ',end='')
            if n == 1:
              print('1 = ', end='')
        fat *= n
    return fat

print(fatorial(7, True))

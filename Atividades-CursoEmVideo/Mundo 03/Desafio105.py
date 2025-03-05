def notas(* notas, sit=False):
    """
    -> Função para analisar um conjunto de notas
        :notas -> Notas que serão passadas para a função como parâmetro
        :sit -> Caso verdadeiro, mostrará se a situação da média das notas é boa ou ruim
        :return -> Retorna um dicionário com informações acerca das notas da turma
    """
    conjNot = {'total': len(notas), 'maior': max(notas), 'menor': min(notas),
               'media': sum(notas)/len(notas)}
    if sit:
      if conjNot['media'] > 6:
         conjNot['situação'] = 'BOA'
      else:
         conjNot['situação'] = 'RUIM'

    return conjNot

n = notas(7, 7, 6)
print(n)
def escreva(frase):
    print((4 + len(frase))*'~')
    print('{:^{}}'.format(frase, (4 + len(frase))))
    print((4 + len(frase))*'~')
    
escreva('OII!')
escreva('O RATO ROEU A ROUPA DO REI DE ROMA')
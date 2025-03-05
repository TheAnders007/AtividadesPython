palavras = ('coisa', 'porta', 'carol', 'letra', 'python', 'carão', 'mamãe')

for palav in palavras:
    print(f'As vogais da palavra {palav} são:', end=' ')
    for letra in palav:
        if letra.lower() in 'áãâaeêéiíoóõôuú':
            print(letra, end=' ')
    print()
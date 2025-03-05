from Menu.options.pessoascad import pessoascad
from cores import cor

def opc01():
    print(50*f'{cor["white"]}-')
    print('{:^50}'.format('PESSOAS CADASTRADAS'))
    print(50*'-')
    for pessoa in pessoascad:
        print ("{:<35}{:>10}".format(pessoa[0], str(pessoa[1]) + "  anos"))
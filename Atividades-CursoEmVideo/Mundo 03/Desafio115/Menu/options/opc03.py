from time import sleep
from cores import cor

def opc03():
    sleep(0.5)
    print(50*f'{cor["white"]}-')
    print('{:^50}'.format('Saindo do Sistema... Até logo!'))
    print(50*'-')
    sleep(1)
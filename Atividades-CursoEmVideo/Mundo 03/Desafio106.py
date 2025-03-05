from time import sleep

def pyhelp():
    print(30*'\033[32m~')
    print('{:^30}'.format('SISTEMA DE AJUDA PyHELP'))
    print(30*'~')
    while True:
        print('\033[0m')
        funbib = input('Função ou Biblioteca: ')
        if funbib.lower() == 'fim':
            print(30*'\033[33m~')
            print('{:^30}'.format('ATÉ LOGO!'))
            print(30*'~')
            print('\033[0m')
            break
        print()
        sleep(0.5)
        print(40*'\033[36m~')
        print('{:^40}'.format(f'Acessando manual do comando {funbib}'))
        print(40*'~')
        sleep(1)
        print('\033[35m')
        help(funbib)

pyhelp()
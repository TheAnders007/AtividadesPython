from time import sleep

def contador(i, f, p):
    print(20*'=-=')
    print(f"Contagem de {i} até {f} de {p} em {p}")
    if p == 0: p = 1
    if p < 0: p = p * (-1)
    if i < f:
      while i <= f:
        sleep(0.35)
        print(i, end=' ')
        i+= p
    else:
      while i >= f:
        sleep(0.35)
        print(i, end=' ')
        i-= p
    print('FIM!')
        
contador(1,10,1)
contador(10,0,2)

print("Agora é sua vez de personalizar a contagem!!")
inicio = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))

contador(inicio, fim, passo)
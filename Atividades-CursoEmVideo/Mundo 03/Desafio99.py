from time import sleep

def maior(* nums):
    numslist = list()

    print(20*'=-=')
    print("Analisando os valores passados...")
    sleep(1)

    for valor in nums:
        print(valor, end=' ')
        numslist.append(valor)
    
    print('Foram informados', len(numslist), 'valores ao todo.')
    if(len(numslist) > 0): print('O maior valor informado foi', max(numslist))
    else: print("Como não foram informados valores, não há maior!")
    sleep(1)



maior(1, 2, 3)
maior(3, 5, 1, 89, 14)
maior()
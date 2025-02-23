print(30*"=")
print('{:^30}'.format('BANCO CEV'))
print(30*"=")

val = int(input("Que valor deseja sacar? R$"))

for el in [50, 20, 10, 1]:
    if (val // el) > 0:
        print(f'Total de {val//el} cédulas de R${el},00')
        val = val - el * (val//el)
    if val == 0:
       break 

print(30*"=")
print("Volte sempre ao Banco CEV! Tenha um bom dia!")

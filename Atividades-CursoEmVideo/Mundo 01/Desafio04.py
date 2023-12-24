val = input("Digite algo: ")

print ("O tipo primitivo desse valor é {}".format(type(val)))
print ("Só tem espaços? {}".format(val.isspace()))
print ("É um número? {}".format(val.isnumeric()))
print ("É alfabético? {}".format(val.isalpha()))
print ("É alfanumérico? {}".format(val.isalnum()))
print ("Está totalmente em letras maiúsculas? {}".format(val.isupper()))
print ("Está totalmente em letras minúsculas? {}".format(val.islower()))
print ("Está capitalizado? {}".format(val.istitle()))



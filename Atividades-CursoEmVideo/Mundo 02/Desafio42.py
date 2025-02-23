print(20 * "=-=")
print("Analisador de triângulos")
print(20 * "=-=")

s1 = float(input("Primeiro Segmento: "))
s2 = float(input("Segundo Segmento: "))
s3 = float(input("Terceiro Segmento: "))

if ((s1 + s2 > s3) and (s1 + s3 > s2) and (s2 + s3 > s1)):
    print("\nOs segmentos acima podem formar um triângulo.\n4")
    if ((s1 == s2) and (s2 == s3)):
         print("O triângulo é equilátero.")
    elif(((s1 == s2) and (s2 != s3)) or ((s1 != s2) and (s2 == s3)) or ((s1 == s3) and (s2 != s3))):
         print("O triângulo é isósceles.")
    else:
         print("O triângulo é escaleno.")
else:
     print("\nOs segmentos acima nâo podem formar um triângulo.")
print(20 * "=-=")
print("Analisador de triângulos")
print(20 * "=-=")

s1 = float(input("Primeiro Segmento: "))
s2 = float(input("Segundo Segmento: "))
s3 = float(input("Terceiro Segmento: "))

if ((s1 + s2 > s3) and (s1 + s3 > s2) and (s2 + s3 > s1)):
    print("\nOs segmentos acima podem formar um triângulo.")
else:
     print("\nOs segmentos acima nâo podem formar um triângulo.")
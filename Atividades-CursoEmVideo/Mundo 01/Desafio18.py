import math

ang = float(input("Digite o valor de um ângulo em graus: "))

print("\nO seno de {}° é {:.2f}.".format(ang, math.sin(math.radians(ang))))
print("O cosseno de {}° é {:.2f}.".format(ang, math.cos(math.radians(ang))))
print("A tangente de {}° é {:.2f}.".format(ang, math.tan(math.radians(ang))))
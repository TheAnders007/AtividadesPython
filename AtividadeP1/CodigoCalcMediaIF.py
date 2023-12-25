a = float (input("Primeira nota da N1\n"))
b = float (input("Segunda nota da N1\n"))    
mn1 = a/2 + b/2

print ()


if (10 >= a >= 0) and (10 >= b >= 0) :
  print ("Sua média N1 é") 
  print ('{:.2f}\n'.format(mn1))
  
if (10 < a) or (a < 0) or (b < 0) or (10 < b) :
  print ("Não é possível executar com o(s) valor(es) digitado(s)")

print ()

if (10 >= a >= 0) and (10 >= b >= 0) :
 c = float (input("Primeira nota da N2\n"))
 d = float (input("Segunda nota da N2\n"))
 mn2 = c/2 + d/2

 print ()

 if (10 >= c >= 0) and (10 >= d >= 0) and (10 >= a >= 0) and (10 >= b >= 0) :
  print ("Sua média N2 é")
  print ('{:.2f}\n'.format(mn2))

 if (10 < c) or (c < 0) or (d < 0) or (10 < d) :
  print ("Não é possível executar com o(s) valor(es) digitado(s)")

 print ()

 p2n1 = mn1 * 2
 p3n2 = mn2 * 3
 mp = p2n1/5 + p3n2/5

 if (10 >= a >= 0) and (10 >= b >= 0) and (10 >= c >= 0) and (10 >= d >= 0) :
  print ("Sua média final é")
  print ('{:.1f}\n'.format(mp))


 print ()

 if (10 >= a >= 0) and (10 >= b >= 0) and (10 >= c >= 0) and (10 >= d >= 0) :
  if (mp >= 6) :
   print ("Você está aprovado")    
  if (3 > mp) :
   print ("Você está reprovado")

  if (6 > mp >= 3) :
   print ("Precisará fazer a Prova Final") 
   print ()
   af = float (input("Nota da Prova Final\n")) 
   print ()
   if (10 >= af >= 0) :
     if (mp/2 + af/2 >= 5) :
      print ("Sua média final é") 
      print ('{:.1f}\n'.format(mp/2 + af/2))
      print ()
      print ("Você está aprovado")
     if (mp/2 + af/2 < 5) :
      print ("Sua média final é")
      print ('{:.1f}\n'.format(mp/2 + af/2))
      print ()
      print ("Você está reprovado")
   if (af > 10) or (af < 0) :
    print ("Não é possível executar com o valor digitado") 

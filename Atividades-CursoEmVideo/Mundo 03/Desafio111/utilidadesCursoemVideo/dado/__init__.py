def leiaDinheiro(msg):
    while True:
      val = input(msg)
      if val.replace('.', '').isnumeric() or val.replace(',', '').isnumeric():
         val = float(val)
         break
      else:
         print(f'\033[31mERRO! {val} é um valor inválido!\033[0m')
    return val


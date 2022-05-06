op = 0
while True:
  print("########################")
  print("#     BEM VINDO        #")
  print("#                      #")
  print("#    1 - ENTRAR        #")
  print("#    2 -  SAIR         #")
  print("#                      #")
  print("########################")
  
  op = int(input('Digite uma opção: '))
  if op == 1:
    print()
  elif op == 2:
    quit()
  elif op > 2 or op < 0:
    print("Opção inválida.")

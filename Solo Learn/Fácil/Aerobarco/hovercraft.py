vendas = int(input())

#producao de 10 hovecraft
gastos = 2 * 10 ** 6 * 10 

#seguro
gastos += 1 * 10 ** 6 
lucro = vendas * 3 * 10 ** 6



if lucro == gastos:
   print("Broke Even")

elif lucro < gastos:
   print("Loss")

elif lucro > gastos:
   print("Profit")
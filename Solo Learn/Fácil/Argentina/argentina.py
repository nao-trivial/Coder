pesos = int(input())

dollars = int(input())

# 1 peso = 0.02 dollars

exchange = 0.02 * pesos 

if exchange > dollars:
    print("Dollars")
else:
    print("Pesos")
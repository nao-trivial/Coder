pesos = gets.chomp.to_i

dollars = gets.chomp.to_i

# 1 peso = 0.02 dollars

exchange = 0.02 * pesos 

if exchange > dollars
    print("Dollars")
else
    print("Pesos")
end
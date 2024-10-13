numero = gets.chomp.to_i
contador = 1
soma = 0

while contador < numero
    if contador % 3 == 0 or contador % 5 == 0
        soma += contador
    end
    contador += 1
end

puts soma

houses = gets.chomp.to_i

#your code goes here

resultado = (2.0 * 100)/houses

if resultado > resultado.round(half: :up)
   resultado += 1
   puts resultado.round(half: :up)
else
   puts resultado.round(half: :up)
end


frase = gets.chomp

palavras = frase.split(" ")
lista = []

palavras.each do |palavra|
  x = palavra[1..-1] # 1° letra
  y = palavra[0]    # resto da palavra
  
  x += y + "ay"
  lista << x
end

puts lista.join(" ")
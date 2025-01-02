def check_box(words)
  # Verificar se algum dos elementos do array é um palíndromo
  words.each do |word|
    if word == word.reverse
      return "Open"
    end
  end
  "Trash"
end

# Solicitar entrada do usuário
input = gets.chomp.upcase.split # Lê e separa as palavras por espaço, converte para maiúsculas

# Verificar o status da caixa
puts check_box(input)
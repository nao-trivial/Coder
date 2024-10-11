def check_sentence_flow(sentence)
  words = sentence.downcase.split  # Converte para minúsculas e divide a frase em palavras

  (1...words.length).each do |i|
    if words[i][0] != words[i - 1][-1]  # Verifica se a primeira letra da palavra atual corresponde à última letra da palavra anterior
      return 'false'
    end
  end

  'true'
end

# Entrada de exemplo
sentence = gets.chomp
# Saída de exemplo
puts check_sentence_flow(sentence)  # Saída: true
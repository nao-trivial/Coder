def poker_hand_rank(hand)
  # Mapeamento dos valores das cartas
  values_order = {'2' => 2, '3' => 3, '4' => 4, '5' => 5, '6' => 6, '7' => 7, '8' => 8, 
                  '9' => 9, '10' => 10, 'J' => 11, 'Q' => 12, 'K' => 13, 'A' => 14}
  
  cards = hand.split
  values = []
  suits = []
  
  # Extrai valores e naipes das cartas
  cards.each do |card|
    value_str = card[0..-2]  # Tudo exceto último caractere
    suit = card[-1]          # Último caractere
    values << values_order[value_str]
    suits << suit
  end
  
  # Ordena os valores
  values.sort!
  
  # Contagem de ocorrências de valores e naipes
  value_counts = values.each_with_object(Hash.new(0)) { |v, h| h[v] += 1 }
  suit_counts = suits.each_with_object(Hash.new(0)) { |s, h| h[s] += 1 }
  
  is_flush = suit_counts.size == 1
  is_straight = (values.size == 5) && (values.last - values.first == 4) && (value_counts.size == 5)
  is_royal = values == [10, 11, 12, 13, 14]
  
  # Determina o ranking da mão
  if is_flush && is_royal
    "Royal Flush"
  elsif is_flush && is_straight
    "Straight Flush"
  elsif value_counts.values.include?(4)
    "Four of a Kind"
  elsif value_counts.values.include?(3) && value_counts.values.include?(2)
    "Full House"
  elsif is_flush
    "Flush"
  elsif is_straight
    "Straight"
  elsif value_counts.values.include?(3)
    "Three of a Kind"
  elsif value_counts.values.count(2) == 2
    "Two Pairs"
  elsif value_counts.values.include?(2)
    "One Pair"
  else
    "High Card"
  end
end

# Exemplo de uso
hand = gets.chomp
puts poker_hand_rank(hand)
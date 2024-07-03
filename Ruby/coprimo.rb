def gcd(a, b)
  while b != 0
    a, b = b, a % b
  end
  a
end

def coprime?(num1, num2)
  gcd(num1, num2) == 1
end

def obter_numero_positivo(mensagem)
  print mensagem
  numero = gets.chomp.to_i

  until numero.positive?
    print "Por favor, insira um número inteiro positivo: "
    numero = gets.chomp.to_i
  end

  numero
end

# Obter entrada do usuário
numero1 = obter_numero_positivo("Insira o primeiro número inteiro positivo: ")
numero2 = obter_numero_positivo("Insira o segundo número inteiro positivo: ")

# Verificar se são coprimos
if coprime?(numero1, numero2)
  puts "#{numero1} e #{numero2} são coprimos."
else
  puts "#{numero1} e #{numero2} não são coprimos."
end

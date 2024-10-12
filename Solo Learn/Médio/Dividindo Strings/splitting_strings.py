def split_string(word, n):
    # Inicializando uma lista para armazenar as partes
    parts = [word[i:i+n] for i in range(0, len(word), n)]
    # Juntando as partes com hífen e retornando o resultado
    return '-'.join(parts)

# Entrada de dados
word = input()
n = int(input())

# Saída do resultado
result = split_string(word, n)
print(result)
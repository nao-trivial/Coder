# Realocar para pasta fácil

numero = int(input())

soma = 0
for i in range(0, numero):
    if i % 3 == 0 or i % 5 == 0:
        soma += i

print(soma)
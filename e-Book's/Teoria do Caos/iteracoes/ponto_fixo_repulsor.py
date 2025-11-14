# Ponto Repulsor - QUASE IMPOSSÍVEL observar
def F(x):
    return 2*x  # Ponto fixo repulsor em x=0

x = 0.0000001  # TENTANDO chegar perto
x += 1e-15     # ERRO DE ARREDONDAMENTO inevitável
for i in range(10):
    x = F(x)
print(x)  # DIVERGE - nunca vemos o ponto repulsor!
# Ponto Atrator - FÁCIL de observar
def F(x):
    return 0.5*x  # Ponto fixo atrator em x=0

x = 0.1  # Não precisa ser exato!
for i in range(10):
    x = F(x)
print(x)  # Converge para 0 mesmo com erro inicial
import numpy as np
import matplotlib.pyplot as plt

# Função quadrática do livro: Q_c(x) = x^2 + c
def Q(x, c):
    return x**2 + c

# Parâmetro do sistema (caso c < -2)
c = -2.36

# Domínio para o gráfico
x = np.linspace(-2.5, 2.5, 1000)

# Curvas principais
y_parabola = Q(x, c)
y_identity = x

# Condição inicial em A₁ (escapa em uma iteração)
x0 = 0.9    # ponto próximo do vértice (região crítica)
n_iter = 6   # poucas iterações já mostram a fuga

# Figura
plt.figure(figsize=(5, 5))

# Parábola Q_c
plt.plot(x, y_parabola, color="black", linewidth=2)

# Reta identidade
plt.plot(x, y_identity, color="black", linestyle="--")

# Cobweb (iteração gráfica)
x_n = x0
for _ in range(n_iter):
    y_n = Q(x_n, c)
    plt.plot([x_n, x_n], [x_n, y_n], color="black", linewidth=1)
    plt.plot([x_n, y_n], [y_n, y_n], color="black", linewidth=1)
    x_n = y_n

# Eixos centrais
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)

# Limites e estética "estilo livro"
plt.xlim(-2.5, 2.5)
plt.ylim(-2.5, 2.5)
plt.xticks([])
plt.yticks([])

plt.title(r"Órbita em $A_1$ escapa para o infinito ($c < -2$)")

plt.show()

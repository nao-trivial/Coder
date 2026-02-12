import matplotlib.pyplot as plt
import numpy as np

# Define o mapa logístico
def logistica(x, r):
    return r * x * (1 - x)

# Desenha o diagrama de bifurcação
def diagrama_bifurcacao(r_min=2.5, r_max=4.0, passos=10000, n_iter=1000, n_exibir=100):
    r_vals = np.linspace(r_min, r_max, passos)
    x0 = 0.5
    xs = []

    for r in r_vals:
        x = x0
        for i in range(n_iter - n_exibir):
            x = logistica(x, r)
        for i in range(n_exibir):
            x = logistica(x, r)
            xs.append((r, x))

    r_plot, x_plot = zip(*xs)
    plt.figure(figsize=(12, 6))
    plt.plot(r_plot, x_plot, ',k', alpha=0.25)
    plt.title("Diagrama de Bifurcação da Função Logística")
    plt.xlabel("r")
    plt.ylabel("x")
    plt.grid(True)
    plt.show()

diagrama_bifurcacao()
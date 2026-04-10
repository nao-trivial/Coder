import numpy as np
import matplotlib.pyplot as plt

# Mapa logístico: x_{n+1} = r * x_n * (1 - x_n)
def logistic_map(r, x0, n):
    xs = [x0]
    for _ in range(n):
        xs.append(r * xs[-1] * (1 - xs[-1]))
    return xs

r = 3.9          # parâmetro no regime caótico
n = 100          # número de iterações
x0 = 0.3         # condição inicial

# Trajetória
x = logistic_map(r, x0, n)

# Visualização simples: evolução temporal
plt.figure(figsize=(10, 4))
plt.plot(x, '.-', markersize=3, linewidth=0.8)
plt.xlabel('Passo')
plt.ylabel('x_n')
plt.title(f'Mapa Logístico (r = {r}) – sensível às condições iniciais')
plt.grid(alpha=0.3)

# Mostrar sensibilidade: segunda trajetória com diferença mínima
x0_2 = x0 + 1e-8
x2 = logistic_map(r, x0_2, n)
plt.plot(x2, '.-', markersize=3, linewidth=0.8, alpha=0.7)
plt.legend(['x0 = 0.3', 'x0 = 0.30000001'])
plt.show()
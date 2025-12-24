# Transformada Z na prática - Análise de estabilidade
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Sistema: x[n+1] = 1.2*x[n] - 0.5*x[n-1] + u[n]
b = [1]      # Coeficientes de entrada
a = [1, -1.2, 0.5]  # Coeficientes de saída

# Encontrar polos
poles = np.roots(a)

# Verificar estabilidade
stable = all(abs(pole) < 1 for pole in poles)

print(f"Polos: {poles}")
print(f"Sistema {'estável' if stable else 'instável'}")

# Visualizar no plano z
fig, ax = plt.subplots(figsize=(6,6))
circle = plt.Circle((0,0), 1, fill=False, color='r', linestyle='--')
ax.add_artist(circle)
ax.scatter(np.real(poles), np.imag(poles), s=100, marker='x', color='b')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.grid(True)
ax.set_title('Polos no Plano Z\n(Círculo unitário = estabilidade)')
plt.show()
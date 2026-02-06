import numpy as np
import matplotlib.pyplot as plt

# =========================
# Parâmetros do modelo
# =========================
alpha = 1.0    # crescimento da presa
beta  = 0.1    # taxa de predação
gamma = 1.5    # mortalidade do predador
delta = 0.075  # eficiência alimentar

# =========================
# Tempo
# =========================
dt = 0.01
T = 50
t = np.arange(0, T, dt)

# =========================
# Condições iniciais
# =========================
x = np.zeros(len(t))  # presas
y = np.zeros(len(t))  # predadores
x[0], y[0] = 10.0, 5.0

# =========================
# Integração (Euler)
# =========================
for i in range(len(t) - 1):
    x[i+1] = x[i] + dt * (alpha * x[i] - beta * x[i] * y[i])
    y[i+1] = y[i] + dt * (-gamma * y[i] + delta * x[i] * y[i])

# =========================
# Gráficos lado a lado
# =========================
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# Espaço de fase
axes[0].plot(x, y)
axes[0].set_xlabel("Presas (x)")
axes[0].set_ylabel("Predadores (y)")
axes[0].set_title("Espaço de Fase")
axes[0].grid(True)

# Presas vs tempo
axes[1].plot(t, x)
axes[1].set_xlabel("Tempo")
axes[1].set_ylabel("Presas (x)")
axes[1].set_title("Evolução das Presas")
axes[1].grid(True)

# Predadores vs tempo
axes[2].plot(t, y)
axes[2].set_xlabel("Tempo")
axes[2].set_ylabel("Predadores (y)")
axes[2].set_title("Evolução dos Predadores")
axes[2].grid(True)

plt.suptitle("Modelo Presa–Predador (Lotka–Volterra)", fontsize=14)
plt.tight_layout()
plt.show()
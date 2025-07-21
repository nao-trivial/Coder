import numpy as np
import matplotlib.pyplot as plt

# Parâmetros da simulação
N = 100  # Número de passos
x = [0]  # Posição inicial

# Simulação do andar do bêbado
for _ in range(N):
    passo = np.random.choice([-1, 1])  # Escolhe aleatoriamente -1 (trás) ou 1 (frente)
    x.append(x[-1] + passo)  # Adiciona a nova posição

# Plotando a caminhada
plt.figure(figsize=(10, 5))
plt.plot(range(N + 1), x, marker="o", linestyle="-", markersize=4)
plt.xlabel("Passos")
plt.ylabel("Posição")
plt.title("Simulação do Andar do Bêbado")
plt.grid(True)
plt.show()
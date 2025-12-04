import numpy as np
import matplotlib.pyplot as plt

# Matriz de transição
transicao = [[0.8, 0.2],
             [0.4, 0.6]]

estado = 0  # Começa com Sol
historico = [estado]

for dia in range(30):
    estado = np.random.choice([0, 1], p=transicao[estado])
    historico.append(estado)

plt.figure(figsize=(10, 4))
plt.plot(historico, 'o-', markersize=6)
plt.yticks([0, 1], ['Sol', 'Chuva'])
plt.xlabel('Dia')
plt.title('Clima Simulado - Cadeia de Markov')
plt.grid(True)
plt.show()
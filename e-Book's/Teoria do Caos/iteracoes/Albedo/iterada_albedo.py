import numpy as np
import matplotlib.pyplot as plt

# Parâmetros
Q = 340           # forçamento solar (W/m²)
T_fusao = 273     # ponto de fusão (K)
alpha = 0.02      # sensibilidade térmica

# Dois pontos fixos lineares (valores hipotéticos)
T_gelo_eq = 265   # equilíbrio gelado
T_agua_eq = 290   # equilíbrio sem gelo

# Iteração linear por partes
def iteracao_albedo(T, Q):
    if T <= T_fusao:
        return T + alpha * (Q - 320)   # parâmetro ajustado para ramo gelado
    else:
        return T + alpha * (Q - 360)   # ramo água

# Simulação
T = 270  # condição inicial (gelo)
historico = [T]
for _ in range(100):
    T = iteracao_albedo(T, Q)
    historico.append(T)

plt.plot(historico, 'b-')
plt.axhline(T_fusao, color='r', linestyle='--', label='Ponto de fusão')
plt.xlabel('Iteração')
plt.ylabel('Temperatura (K)')
plt.title(f'Q = {Q} W/m² – ' + ('Retorna ao gelo' if historico[-1] < T_fusao else 'Derrete irreversivelmente'))
plt.legend()
plt.show()
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parâmetros da simulação
N_passos = 100        # Número de passos de cada bêbado (limitado)
N_bebados = 1000     # Quantos bêbados (caminhadas) serão simulados

# Lista para armazenar as posições finais de cada bêbado
posicoes_finais = []

# Simulação de múltiplos bêbados
for _ in range(N_bebados):
    posicao = 0
    for _ in range(N_passos):
        passo = np.random.choice([-1, 1])  # -1 (trás) ou 1 (frente)
        posicao += passo
    posicoes_finais.append(posicao)

# Convertendo para array numpy
posicoes_finais = np.array(posicoes_finais)

# Parâmetros da Gaussiana teórica (Teorema Central do Limite)
# Média = 0, Variância = N_passos (pois cada passo tem variância 1)
media_teorica = 0
desvio_teorico = np.sqrt(N_passos)

# Plotando o histograma das posições finais
plt.figure(figsize=(10, 6))
count, bins, _ = plt.hist(posicoes_finais, bins=30, density=True, 
                          alpha=0.7, color='skyblue', edgecolor='black',
                          label='Distribuição simulada')

# Sobrepondo a curva gaussiana teórica
x_vals = np.linspace(-4*desvio_teorico, 4*desvio_teorico, 200)
gauss_teorica = norm.pdf(x_vals, media_teorica, desvio_teorico)
plt.plot(x_vals, gauss_teorica, 'r-', linewidth=2, label='Gaussiana teórica')

plt.xlabel('Posição final')
plt.ylabel('Densidade de probabilidade')
plt.title(f'Distribuição das posições finais de {N_bebados} bêbados\n'
          f'({N_passos} passos cada)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
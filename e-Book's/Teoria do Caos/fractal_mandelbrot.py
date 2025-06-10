import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import time

# Configurações do fractal
LARGURA, ALTURA = 800, 800  # Resolução da imagem
X_MIN, X_MAX = -2.0, 1.0    # Eixo X real
Y_MIN, Y_MAX = -1.5, 1.5    # Eixo Y imaginário
MAX_ITER = 100              # Máximo de iterações
COLORMAP = 'twilight_shifted'  # Mapa de cores (magma, viridis, plasma, etc)

# Início da medição de tempo
inicio = time.time()

# Cria a grade de números complexos
x = np.linspace(X_MIN, X_MAX, LARGURA)
y = np.linspace(Y_MIN, Y_MAX, ALTURA)
c = x[:, np.newaxis] + 1j * y[np.newaxis, :]

# Inicializa o array de iterações e z
iteracoes = np.zeros(c.shape, dtype=int)
z = np.zeros(c.shape, dtype=np.complex128)

# Algoritmo de Mandelbrot
for i in range(MAX_ITER):
    mask = (np.abs(z) < 10)  # Continua apenas onde |z| < 10
    z[mask] = z[mask]**2 + c[mask]
    iteracoes[mask] = i

# Cálculo do tempo de processamento
tempo_processamento = time.time() - inicio
print(f"Fractal gerado em {tempo_processamento:.2f} segundos")

# Configuração da figura
plt.figure(figsize=(12, 10), dpi=100)
plt.title(f"CONJUNTO DE MANDELBROT\nResolução: {LARGURA}x{ALTURA} | Iterações: {MAX_ITER}", 
          fontsize=16, pad=20)

# Plot do fractal com cores logarítmicas
norm = colors.LogNorm(vmin=iteracoes.min(), vmax=iteracoes.max())
plt.imshow(iteracoes.T, cmap=COLORMAP, norm=norm, 
           extent=[X_MIN, X_MAX, Y_MIN, Y_MAX])

# Anotações matemáticas
plt.text(-1.7, -1.3, r"$z_{n+1} = z_n^2 + c$", 
         fontsize=20, color='white', alpha=0.8)
plt.text(0.3, 1.3, "Caos Determinístico", 
         fontsize=14, color='yellow', ha='center')

# Elementos decorativos
plt.xlabel("Parte Real (Re)", fontsize=12)
plt.ylabel("Parte Imaginária (Im)", fontsize=12)
plt.grid(alpha=0.1, color='white')
plt.axhline(0, color='white', alpha=0.3, linestyle='--')
plt.axvline(0, color='white', alpha=0.3, linestyle='--')

# Salva e mostra o resultado
plt.savefig('mandelbrot_fractal.png', bbox_inches='tight')
plt.show()
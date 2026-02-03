import matplotlib.pyplot as plt
import numpy as np

# Parâmetros do sistema
a1, c, b1 = 0.6, 0.4, 1.0
a2, d, b2 = 0.3, 0.7, 2.0

# Condição inicial
x0, y0 = 5.0, -3.0

# Número de iterações
n_iter = 20

# Inicializar arrays
x = np.zeros(n_iter + 1)
y = np.zeros(n_iter + 1)
x[0], y[0] = x0, y0

# Iterar o sistema
for i in range(n_iter):
    x[i+1] = a1 * x[i] + c * y[i] + b1
    y[i+1] = a2 * y[i] + d * x[i] + b2

# Criar figura com 3 subplots
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 4))

# 1. Trajetória no espaço de fase
ax1.plot(x, y, 'b-', linewidth=2, alpha=0.7)
ax1.scatter(x[0], y[0], color='red', s=100, label='Início (n=0)', zorder=5)
ax1.scatter(x[-1], y[-1], color='green', s=100, marker='s', label='Fim', zorder=5)
ax1.set_xlabel('xₙ')
ax1.set_ylabel('yₙ')
ax1.set_title('Espaço de Fase (y vs x)')
ax1.grid(True, alpha=0.3)
ax1.legend()

# 2. Evolução de x_n
ax2.plot(range(n_iter+1), x, 'ro-', linewidth=2, markersize=6)
ax2.set_xlabel('Iteração n')
ax2.set_ylabel('xₙ')
ax2.set_title('Evolução de xₙ')
ax2.grid(True, alpha=0.3)
ax2.set_xticks(range(0, n_iter+1, max(1, n_iter//10)))

# 3. Evolução de y_n
ax3.plot(range(n_iter+1), y, 'go-', linewidth=2, markersize=6)
ax3.set_xlabel('Iteração n')
ax3.set_ylabel('yₙ')
ax3.set_title('Evolução de yₙ')
ax3.grid(True, alpha=0.3)
ax3.set_xticks(range(0, n_iter+1, max(1, n_iter//10)))

plt.suptitle(f'Sistema: xₙ₊₁ = {a1}xₙ + {c}yₙ + {b1},   yₙ₊₁ = {a2}yₙ + {d}xₙ + {b2}', fontsize=14)
plt.tight_layout()
plt.show()

# Imprimir valores
print("="*60)
print("SISTEMA DINÂMICO BIDIMENSIONAL")
print("="*60)
print(f"xₙ₊₁ = {a1}·xₙ + {c}·yₙ + {b1}")
print(f"yₙ₊₁ = {a2}·yₙ + {d}·xₙ + {b2}")
print(f"\nCondição inicial: x₀ = {x0}, y₀ = {y0}")
print(f"Número de iterações: {n_iter}")
print("\nValores calculados:")
print("n      xₙ        yₙ")
print("-"*25)
for i in range(min(11, n_iter+1)):
    print(f"{i:2}   {x[i]:7.4f}   {y[i]:7.4f}")

if n_iter > 10:
    print("...")
    print(f"{n_iter:2}   {x[n_iter]:7.4f}   {y[n_iter]:7.4f}")

# Cálculo do ponto fixo (se existir)
A = np.array([[a1, c], [d, a2]])
b = np.array([b1, b2])
I = np.identity(2)

try:
    M = I - A
    ponto_fixo = np.linalg.solve(M, b)
    print(f"\nPonto fixo: x* = {ponto_fixo[0]:.4f}, y* = {ponto_fixo[1]:.4f}")
    
    # Verificar estabilidade
    autovalores = np.linalg.eigvals(A)
    raio_espectral = np.max(np.abs(autovalores))
    print(f"Autovalores: {autovalores[0]:.4f}, {autovalores[1]:.4f}")
    print(f"Raio espectral: {raio_espectral:.4f}")
    
    if raio_espectral < 1:
        print("Sistema ESTÁVEL (converge para ponto fixo)")
    elif raio_espectral > 1:
        print("Sistema INSTÁVEL (diverge do ponto fixo)")
    else:
        print("Sistema no limite da estabilidade")
        
except np.linalg.LinAlgError:
    print("\nNão foi possível encontrar ponto fixo único")
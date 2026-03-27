import numpy as np
import matplotlib.pyplot as plt

def F(x, y):
    """
    Calcula as componentes do campo vetorial F(x,y).
    Evita divisão por zero somando um pequeno valor ao denominador.
    """
    r2 = x**2 + y**2
    # Evita divisão exata por zero; onde r2 é zero, substitui por um valor pequeno
    r2 = np.where(r2 == 0, np.inf, r2)  # ou use r2 = np.maximum(r2, 1e-10)
    u = -y / r2
    v =  x / r2
    return u, v

# ----------------------------------------------------------------------
# 1. Configuração da malha para o gráfico de setas (quiver)
# ----------------------------------------------------------------------
x = np.linspace(-2, 2, 20)   # pontos na direção x
y = np.linspace(-2, 2, 20)   # pontos na direção y
X, Y = np.meshgrid(x, y)     # malha 2D
U, V = F(X, Y)               # componentes do campo

plt.figure(figsize=(12, 5))

# Gráfico com setas
plt.subplot(1, 2, 1)
plt.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=15, color='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Campo vetorial (setas)')
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.gca().set_aspect('equal')

# ----------------------------------------------------------------------
# 2. Malha mais fina para as linhas de corrente (streamplot)
# ----------------------------------------------------------------------
x_fine = np.linspace(-2, 2, 100)
y_fine = np.linspace(-2, 2, 100)
X_fine, Y_fine = np.meshgrid(x_fine, y_fine)
U_fine, V_fine = F(X_fine, Y_fine)

plt.subplot(1, 2, 2)
plt.streamplot(X_fine, Y_fine, U_fine, V_fine, density=1.5, color='red', linewidth=1)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linhas de corrente')
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.gca().set_aspect('equal')

plt.tight_layout()
plt.show()
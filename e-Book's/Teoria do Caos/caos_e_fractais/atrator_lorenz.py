import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parâmetros do sistema de Lorenz
sigma = 10.0
rho = 28.0
beta = 8.0 / 3.0

# Equações diferenciais do sistema
def lorenz(x, y, z):
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return dx, dy, dz

# Condições iniciais
x0, y0, z0 = (1.0, 1.0, 1.0)

# Configuração da integração
t_max = 40.0      # tempo total de simulação
dt = 0.01         # passo de integração
n_steps = int(t_max / dt)

# Alocação das trajetórias
xs = np.zeros(n_steps)
ys = np.zeros(n_steps)
zs = np.zeros(n_steps)
xs[0], ys[0], zs[0] = x0, y0, z0

# Integração numérica (Runge-Kutta 4ª ordem)
for i in range(n_steps - 1):
    x, y, z = xs[i], ys[i], zs[i]
    
    k1x, k1y, k1z = lorenz(x, y, z)
    k2x, k2y, k2z = lorenz(x + 0.5 * dt * k1x,
                           y + 0.5 * dt * k1y,
                           z + 0.5 * dt * k1z)
    k3x, k3y, k3z = lorenz(x + 0.5 * dt * k2x,
                           y + 0.5 * dt * k2y,
                           z + 0.5 * dt * k2z)
    k4x, k4y, k4z = lorenz(x + dt * k3x,
                           y + dt * k3y,
                           z + dt * k3z)
    
    xs[i+1] = x + dt * (k1x + 2*k2x + 2*k3x + k4x) / 6
    ys[i+1] = y + dt * (k1y + 2*k2y + 2*k3y + k4y) / 6
    zs[i+1] = z + dt * (k1z + 2*k2z + 2*k3z + k4z) / 6

# Plotagem em 3D
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot(xs, ys, zs, lw=0.5, color='b')
ax.set_title("Atrator de Lorenz")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parâmetros do pêndulo
m1 = 1.0   # Massa do primeiro pêndulo (kg)
m2 = 1.0   # Massa do segundo pêndulo (kg)
L1 = 1.0   # Comprimento do primeiro pêndulo (m)
L2 = 1.0   # Comprimento do segundo pêndulo (m)
g = 9.81   # Aceleração gravitacional (m/s²)

# Condições iniciais [θ1, ω1, θ2, ω2]
theta1_0 = np.pi / 2  # 90 graus
theta2_0 = np.pi / 2  # 90 graus
omega1_0 = 0.0
omega2_0 = 0.0
initial_state = [theta1_0, omega1_0, theta2_0, omega2_0]

# Configuração da simulação
dt = 0.01      # Passo de tempo (s)
t_max = 30.0   # Tempo total de simulação (s)
t = np.arange(0, t_max, dt)

# Sistema de EDOs CORRIGIDO do pêndulo duplo
def derivatives(state, t, m1, m2, L1, L2, g):
    theta1, omega1, theta2, omega2 = state
    
    # Diferença entre ângulos
    delta = theta2 - theta1
    
    # Denominadores para resolver o sistema de equações
    den1 = (m1 + m2) * L1 - m2 * L1 * np.cos(delta) * np.cos(delta)
    den2 = (L2 / L1) * den1
    
    # Acelerações angulares - CORRIGIDAS
    alpha1 = (m2 * L1 * omega1**2 * np.sin(delta) * np.cos(delta) +
              m2 * g * np.sin(theta2) * np.cos(delta) +
              m2 * L2 * omega2**2 * np.sin(delta) -
              (m1 + m2) * g * np.sin(theta1)) / (L1 * den1)
    
    alpha2 = (-m2 * L2 * omega2**2 * np.sin(delta) * np.cos(delta) +
              (m1 + m2) * (g * np.sin(theta1) * np.cos(delta) -
                          L1 * omega1**2 * np.sin(delta) -
                          g * np.sin(theta2))) / (L2 * den2)
    
    return [omega1, alpha1, omega2, alpha2]

# Método de Runge-Kutta de 4ª ordem
def runge_kutta(state, t, dt, deriv_func, *args):
    k1 = deriv_func(state, t, *args)
    k2 = deriv_func([s + 0.5 * dt * k for s, k in zip(state, k1)], t + 0.5 * dt, *args)
    k3 = deriv_func([s + 0.5 * dt * k for s, k in zip(state, k2)], t + 0.5 * dt, *args)
    k4 = deriv_func([s + dt * k for s, k in zip(state, k3)], t + dt, *args)
    
    return [s + (dt / 6.0) * (k1[i] + 2*k2[i] + 2*k3[i] + k4[i]) for i, s in enumerate(state)]

# Simulação
states = []
current_state = initial_state.copy()

for time_step in t:
    states.append(current_state.copy())
    current_state = runge_kutta(current_state, time_step, dt, derivatives, m1, m2, L1, L2, g)

states = np.array(states)

# Conversão para coordenadas cartesianas
x1 = L1 * np.sin(states[:, 0])
y1 = -L1 * np.cos(states[:, 0])
x2 = x1 + L2 * np.sin(states[:, 2])
y2 = y1 - L2 * np.cos(states[:, 2])

# Configuração da figura para animação
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-(L1 + L2 + 0.5), L1 + L2 + 0.5)
ax.set_ylim(-(L1 + L2 + 0.5), L1 + L2 + 0.5)
ax.set_aspect('equal')
ax.grid(True)
ax.set_title('Pêndulo Duplo - Animação')
ax.set_xlabel('Posição X (m)')
ax.set_ylabel('Posição Y (m)')

# Elementos da animação
line, = ax.plot([], [], 'o-', lw=2, color='blue', markersize=8)
trace, = ax.plot([], [], '-', lw=1, color='red', alpha=0.7)
pivot, = ax.plot([0], [0], 'ko', markersize=10)

# Rastreio da trajetória da segunda massa
trace_x = []
trace_y = []

# Inicialização
def init():
    line.set_data([], [])
    trace.set_data([], [])
    return line, trace, pivot

# Atualização do frame
def update(frame):
    # Pêndulo
    x_points = [0, x1[frame], x2[frame]]
    y_points = [0, y1[frame], y2[frame]]
    
    line.set_data(x_points, y_points)
    
    # Trajetória (últimos 500 pontos)
    trace_x.append(x2[frame])
    trace_y.append(y2[frame])
    
    # Limita o tamanho da trajetória para melhor performance
    if len(trace_x) > 800:
        trace_x.pop(0)
        trace_y.pop(0)
    
    trace.set_data(trace_x, trace_y)
    
    return line, trace, pivot

# Criação da animação
ani = FuncAnimation(fig, update, frames=len(t),
                    init_func=init, blit=True, interval=20)

plt.tight_layout()
plt.show()
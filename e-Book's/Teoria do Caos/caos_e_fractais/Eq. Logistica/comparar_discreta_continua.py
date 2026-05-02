import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Modelo contínuo: dN/dt = μ * N * (1 - N)
def verhulst(t, N, mu):
    return mu * N * (1 - N)

# Parâmetros comuns
N0 = 0.1          # condição inicial
t_max = 20        # tempo máximo de simulação
t_eval = np.linspace(0, t_max, 200)  # pontos para a solução contínua

# Lista de valores pequenos de μ para comparar
mu_list = [0.8, 1.2, 1.8, 2.5]

# Criação dos subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.flatten()

for idx, mu in enumerate(mu_list):
    # ---- Solução contínua (Verhulst) ----
    sol = solve_ivp(verhulst, [0, t_max], [N0], args=(mu,), t_eval=t_eval)
    t_cont = sol.t
    N_cont = sol.y[0]
    
    # ---- Mapa discreto (logístico) ----
    n_steps = int(t_max) + 1  # passos inteiros (Δt = 1)
    N_disc = np.zeros(n_steps)
    N_disc[0] = N0
    for i in range(n_steps - 1):
        N_disc[i+1] = mu * N_disc[i] * (1 - N_disc[i])
    t_disc = np.arange(n_steps)
    
    # ---- Gráfico ----
    ax = axes[idx]
    ax.plot(t_cont, N_cont, 'b-', linewidth=2, label='Contínuo (Verhulst)')
    ax.plot(t_disc, N_disc, 'ro-', markersize=4, label='Discreto (Logístico)')
    ax.set_title(f'μ = {mu}')
    ax.set_xlabel('Tempo t')
    ax.set_ylabel('População N(t)')
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.6)
    
    # Exibe o ponto fixo positivo (quando existe) para referência
    if mu > 1:
        eq_cont = 1.0
        eq_disc = (mu - 1) / mu
        ax.axhline(y=eq_cont, color='b', linestyle=':', alpha=0.5, label=f'Equilíbrio contínuo = {eq_cont}')
        ax.axhline(y=eq_disc, color='r', linestyle=':', alpha=0.5, label=f'Equilíbrio discreto = {eq_disc:.3f}')
        # Ajusta legenda
        handles, labels = ax.get_legend_handles_labels()
        ax.legend(handles, labels, loc='best')

plt.tight_layout()
plt.suptitle('Comparação entre os modelos contínuo (Verhulst) e discreto (logístico)\npara diferentes valores pequenos de μ', y=1.02)
plt.show()

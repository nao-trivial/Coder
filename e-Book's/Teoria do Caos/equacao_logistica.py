import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Configurações iniciais
plt.style.use('dark_background')  # Fundo escuro para realçar cores

# Parâmetros da equação logística: x_{n+1} = r * x_n * (1 - x_n)
r = 3.8  # Taxa de crescimento (0 a 4)
populacao_inicial = 0.1  # População inicial normalizada (0 a 1)
geracoes = 100  # Número de gerações

# Simulação
populacoes = [populacao_inicial]
for _ in range(geracoes):
    ultima_pop = populacoes[-1]
    nova_pop = r * ultima_pop * (1 - ultima_pop)  # Equação logística
    populacoes.append(nova_pop)

# Configuração do gráfico
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), gridspec_kw={'width_ratios': [2, 3]})

# Gráfico 1: Evolução temporal
ax1.set_title(f"CRESCIMENTO DE POPULAÇÃO\n(r = {r})", fontsize=14, color='cyan')
ax1.set_xlabel('Geração', fontsize=12)
ax1.set_ylabel('População Normalizada', fontsize=12)
ax1.set_ylim(0, 1)
ax1.grid(alpha=0.3)
line, = ax1.plot([], [], 'o-', color='#FF69B4', markersize=4, linewidth=1)

# Gráfico 2: Diagrama de teia de aranha (cobweb plot)
ax2.set_title("DIAGRAMA DE TEIA - COMPORTAMENTO CAÓTICO", fontsize=14, color='yellow')
ax2.set_xlabel('População (n)', fontsize=12)
ax2.set_ylabel('População (n+1)', fontsize=12)
ax2.plot([0, 1], [0, 1], '--', color='white', alpha=0.5)

# Função logística
x = np.linspace(0, 1, 100)
y = r * x * (1 - x)
ax2.plot(x, y, color='#00FFFF', linewidth=2)

# Elementos de animação
cobweb_line, = ax2.plot([], [], 'o-', color='#FF69B4', lw=1, markersize=3)
ax2.set_xlim(0, 1)
ax2.set_ylim(0, 1)

# Animação
def animate(i):
    # Atualiza gráfico temporal
    line.set_data(range(i), populacoes[:i])
    
    # Atualiza diagrama de teia
    if i > 1:
        cobweb_x = []
        cobweb_y = []
        for j in range(1, min(i, 30)):  # Mostra apenas últimos 30 passos
            cobweb_x.extend([populacoes[j-1], populacoes[j]])
            cobweb_y.extend([populacoes[j], populacoes[j]])
        cobweb_line.set_data(cobweb_x, cobweb_y)
    
    return line, cobweb_line

ani = FuncAnimation(fig, animate, frames=geracoes+1, interval=100, blit=True)

plt.tight_layout()
plt.savefig('caos_logistico.png', dpi=300)
plt.show()
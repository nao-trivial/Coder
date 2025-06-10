import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

def analise_iteracao_linear(f, x0, n_iteracoes=20, x_range=(-5, 5)):
    """
    Analisa uma iteração linear genérica x_{n+1} = f(x_n), com:
    - Gráfico da sequência temporal.
    - Diagrama de teia de aranha (cobweb plot).
    
    Parâmetros:
        f (função): Função de iteração (ex: lambda x: 0.5*x + 2).
        x0 (float): Condição inicial.
        n_iteracoes (int): Número de iterações.
        x_range (tuple): Intervalo para plotar a função.
    """
    # Configuração da figura
    fig = plt.figure(figsize=(12, 6))
    gs = GridSpec(2, 2, figure=fig)
    
    # --- Gráfico da Sequência Temporal ---
    ax1 = fig.add_subplot(gs[0, :])
    sequencia = [x0]
    for _ in range(n_iteracoes):
        sequencia.append(f(sequencia[-1]))
    
    ax1.plot(sequencia, 'ro-', label=f'$x_n$ (começando em $x_0 = {x0}$)')
    ax1.set_xlabel('Iteração (n)')
    ax1.set_ylabel('$x_n$')
    ax1.set_title('Evolução Temporal da Sequência')
    ax1.grid(True)
    ax1.legend()

    # --- Diagrama de Teia de Aranha ---
    ax2 = fig.add_subplot(gs[1, 0])
    x_values = np.linspace(x_range[0], x_range[1], 400)
    ax2.plot(x_values, [f(x) for x in x_values], 'b-', label='$x_{n+1} = f(x_n)$')
    ax2.plot(x_values, x_values, 'k--', label='$y = x$')
    
    # Simula a teia de aranha
    x = x0
    for _ in range(n_iteracoes):
        y = f(x)
        ax2.plot([x, x], [x, y], 'r-', alpha=0.5, linewidth=1)
        ax2.plot([x, y], [y, y], 'r-', alpha=0.5, linewidth=1)
        x = y
    
    ax2.set_xlabel('$x_n$')
    ax2.set_ylabel('$x_{n+1}$')
    ax2.set_title('Diagrama de Teia de Aranha')
    ax2.legend()
    ax2.grid(True)

    # --- Histórico dos Valores ---
    ax3 = fig.add_subplot(gs[1, 1])
    ax3.axis('off')
    ax3.text(0.1, 0.1, 
             f'Últimos 5 valores:\n' + '\n'.join([f'$x_{i} = {val:.4f}$' for i, val in enumerate(sequencia[-5:])]),
             fontfamily='monospace', fontsize=10, va='top')
    
    plt.tight_layout()
    plt.show()

# Exemplo de uso:
f = lambda x: 0.5 * x + 2  # Mapeamento afim (substitua por qualquer função!)
x0 = 0.0
analise_iteracao_linear(f, x0, n_iteracoes=10, x_range=(-1, 5))
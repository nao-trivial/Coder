import matplotlib.pyplot as plt
import numpy as np

def plot_evolucao_multipla(funcoes, x0s, n=10, titulo="Evolução Temporal", legendas=None):
    """
    Versão aprimorada para análise de múltiplas sequências
    """
    if not isinstance(funcoes, list):
        funcoes = [funcoes]
    if not isinstance(x0s, list):
        x0s = [x0s]
    
    # Calcular sequências para cada função/condição inicial
    sequencias = []
    for f, x0 in zip(funcoes, x0s):
        sequencia = [x0]
        for i in range(n):
            sequencia.append(f(sequencia[-1]))
        sequencias.append(sequencia)
    
    # Plotar todas as sequências no mesmo gráfico
    plt.figure(figsize=(10, 6))
    
    # Cores e marcadores diferentes para cada sequência
    cores = ['blue', 'red', 'green', 'orange', 'purple']
    marcadores = ['o', 's', '^', 'D', 'v']
    estilos = ['-', '--', '-.', ':', '-']
    
    for i, sequencia in enumerate(sequencias):
        cor = cores[i % len(cores)]
        marcador = marcadores[i % len(marcadores)]
        estilo = estilos[i % len(estilos)]
        
        # Criar legenda
        legenda = legendas[i] if legendas and i < len(legendas) else f"Sequência {i+1}"
        
        plt.plot(range(len(sequencia)), sequencia, 
                marker=marcador, linestyle=estilo, color=cor, 
                linewidth=2, markersize=6, label=legenda)
    
    plt.xlabel('Iteração (n)', fontsize=12)
    plt.ylabel('xₙ', fontsize=12)
    plt.title(titulo, fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.legend(loc='best', fontsize=10)
    
    # Adicionar grade secundária
    plt.minorticks_on()
    plt.grid(which='minor', alpha=0.2, linestyle=':')
    
    # Ajustar limites dos eixos
    plt.xlim(-0.5, n + 0.5)
    
    plt.tight_layout()
    plt.show()
    
    # Mostrar valores das sequências
    print(f"\nValores calculados (primeiros 5 iterações de cada sequência):")
    for i, sequencia in enumerate(sequencias):
        legenda = legendas[i] if legendas and i < len(legendas) else f"Sequência {i+1}"
        print(f"\n{legenda}:")
        for j, valor in enumerate(sequencia[:5]):
            print(f"  x_{j} = {valor:.4f}")
    
    return sequencias

# Exemplo 2: Duas funções diferentes com a mesma condição inicial
print("Exemplo 2: Duas funções diferentes com a mesma condição inicial")
f1 = lambda x: x * 0.9 + 7.5
f2 = lambda x: x * 0.2 + 7.3  # Função diferente

sequencias2 = plot_evolucao_multipla(
    funcoes=[f1, f2],  # Funções diferentes
    x0s=[4, 4],        # Mesma condição inicial
    n=15,
    titulo="Comparação de duas funções diferentes",
    legendas=["f(x) = 0.9x + 7.5", "g(x) = 0.2x + 7.3"]
)

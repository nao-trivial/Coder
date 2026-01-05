import matplotlib.pyplot as plt

def plot_evolucao_simples(f, x0, n=10, titulo="Evolução Temporal"):
    """
    Versão simplificada para análise básica
    """
    # Calcular sequência
    sequencia = [x0]
    for i in range(n):
        sequencia.append(f(sequencia[-1]))
    
    # Plotar
    plt.figure(figsize=(8, 5))
    plt.plot(range(len(sequencia)), sequencia, 'bo-')
    plt.xlabel('Iteração (n)')
    plt.ylabel('xₙ')
    plt.title(titulo)
    plt.grid(True)
    plt.show()
    
    # Mostrar valores
    print(f"\nValores calculados (primeiros 5):")
    for i, valor in enumerate(sequencia[:5]):
        print(f"  x_{i} = {valor:.4f}")
    
    return sequencia

# Exemplo de uso:
# f = lambda x: x**2 - 2
# plot_evolucao_simples(f, 1.5, 8, "Exemplo: xₙ₊₁ = xₙ² - 2")

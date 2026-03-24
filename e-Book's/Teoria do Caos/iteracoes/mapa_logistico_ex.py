import matplotlib.pyplot as plt
import numpy as np

def mapa_logistico(x, r):
    return r * x * (1 - x)

def ciclo_logistico(r, ciclo):
    derivada_total = 1
    for x in ciclo:
        derivada_total *= r * (1 - 2*x)
    return derivada_total

def plot_teia_simples(r, ciclo, iteracoes=50):
    """Versão simples do diagrama de teia de aranha"""
    
    plt.figure(figsize=(8, 6))
    
    # Curva do mapa logístico
    x = np.linspace(0, 1, 100)
    y = mapa_logistico(x, r)
    plt.plot(x, y, 'b-', linewidth=2, label='f(x)')
    plt.plot(x, x, 'k--', linewidth=1, label='y = x')
    
    # Trajetória da teia
    x_atual = ciclo[0] + 0.02  # Começa perto do ciclo
    trajetoria_x = [x_atual]
    trajetoria_y = [0]
    
    for _ in range(iteracoes):
        # Linha vertical
        trajetoria_x.append(x_atual)
        trajetoria_y.append(mapa_logistico(x_atual, r))
        # Linha horizontal
        trajetoria_y.append(trajetoria_y[-1])
        trajetoria_x.append(trajetoria_y[-1])
        x_atual = trajetoria_y[-1]
    
    plt.plot(trajetoria_x, trajetoria_y, 'r-', alpha=0.7, linewidth=1, label='Trajetória')
    
    # Pontos do ciclo
    for ponto in ciclo:
        plt.plot(ponto, ponto, 'ro', markersize=8, label=f'x = {ponto:.3f}')
    
    plt.xlabel('xₙ')
    plt.ylabel('xₙ₊₁')
    plt.title(f'Teia de Aranha - r = {r}')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()

# Exemplo 1: Ciclo estável
print("=== CICLO ESTÁVEL ===")
r = 3.2
ciclo = [0.513, 0.799]
derivada = ciclo_logistico(r, ciclo)

print(f"r = {r}")
print(f"Ciclo: {ciclo}")
print(f"Derivada: {derivada:.3f}")
print(f"Estável? {abs(derivada) < 1}")

plot_teia_simples(r, ciclo)

# Exemplo 2: Ponto fixo
print("\n=== PONTO FIXO ===")
r2 = 2.8
ciclo2 = [0.642]
derivada2 = ciclo_logistico(r2, ciclo2)

print(f"r = {r2}")
print(f"Ponto fixo: {ciclo2}")
print(f"Derivada: {derivada2:.3f}")
print(f"Estável? {abs(derivada2) < 1}")

plot_teia_simples(r2, ciclo2)
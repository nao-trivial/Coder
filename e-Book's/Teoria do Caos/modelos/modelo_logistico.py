import matplotlib.pyplot as plt

def simular_insetos(r, populacao_inicial=0.1, semanas=50):
    """Versão simplificada para ensino"""
    
    populacao = [populacao_inicial]
    
    for semana in range(semanas):
        nova_pop = r * populacao[-1] * (1 - populacao[-1])
        populacao.append(nova_pop)
    
    # Plot simples
    plt.figure(figsize=(10, 4))
    
    plt.subplot(1, 2, 1)
    plt.plot(populacao, 'ro-', markersize=3)
    plt.title(f'População de Insetos (r={r})')
    plt.xlabel('Semanas'); plt.ylabel('População')
    plt.grid(True)
    
    plt.subplot(1, 2, 2)
    x = [i/100 for i in range(100)]
    y = [r * xi * (1 - xi) for xi in x]
    plt.plot(x, y, 'b-')
    plt.plot(x, x, 'k--')
    plt.title('Modelo Logístico')
    plt.xlabel('Pop. semana n'); plt.ylabel('Pop. semana n+1')
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()
    
    return populacao

# Testar diferentes cenários
print("🔍 Simulando crescimento de insetos...")

print("\n📗 Caso 1: População controlada")
simular_insetos(2.5)

print("\n📘 Caso 2: Oscilações regulares")  
simular_insetos(3.4)

print("\n📕 Caso 3: Comportamento caótico")
simular_insetos(3.8)
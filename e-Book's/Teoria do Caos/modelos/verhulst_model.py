import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def modelo_verhulst(P, t, r, K):
    """
    Equação diferencial do modelo de Verhulst (crescimento logístico).
    
    Parâmetros:
        P : população no instante t
        t : tempo (não usado explicitamente na equação, mas necessário para odeint)
        r : taxa de crescimento intrínseca
        K : capacidade de suporte (carrying capacity)
    
    Retorna:
        dPdt : derivada da população em relação ao tempo
    """
    dPdt = r * P * (1 - P / K)
    return dPdt

# Parâmetros do modelo
r = 0.5          # taxa de crescimento (por unidade de tempo)
K = 1000.0       # capacidade de suporte
P0 = 10.0        # população inicial

# Intervalo de tempo
t_inicial = 0.0
t_final = 20.0
num_pontos = 200
t = np.linspace(t_inicial, t_final, num_pontos)

# Resolve a equação diferencial
solucao = odeint(modelo_verhulst, P0, t, args=(r, K))
populacao = solucao[:, 0]  # extrai o vetor população

# Cria o gráfico
plt.figure(figsize=(10, 6))
plt.plot(t, populacao, 'b-', linewidth=2, label='População')
plt.axhline(y=K, color='r', linestyle='--', label=f'Capacidade de suporte (K = {K})')
plt.xlabel('Tempo')
plt.ylabel('População')
plt.title('Modelo de Verhulst (Crescimento Logístico)')
plt.legend()
plt.grid(True)
plt.show()
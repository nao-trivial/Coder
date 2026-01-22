import numpy as np
import matplotlib.pyplot as plt

# Parâmetros
T0 = 90
T_amb = 25
k = 0.85
n_passos = 15

# Simulação
temperaturas = [T0]
T = T0
for i in range(n_passos):
    T = k*T + (1-k)*T_amb
    temperaturas.append(T)

# Gráfico
plt.figure(figsize=(10, 6))
plt.plot(range(n_passos+1), temperaturas, 'bo-', 
         linewidth=2, markersize=8, 
         label='Temperatura do Corpo')
plt.axhline(y=T_amb, color='r', linestyle='--', 
           linewidth=2, label='Temperatura Ambiente')
plt.xlabel('Tempo (intervalos de 1 min)', fontsize=12)
plt.ylabel('Temperatura (°C)', fontsize=12)
plt.title('Lei do Resfriamento de Newton\nIteração Linear: $T_{t+1} = 0.85T_t + 0.15×25$', 
          fontsize=14)
plt.grid(True, alpha=0.3, linestyle='--')
plt.legend(fontsize=11)
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)
plt.tight_layout()
plt.savefig('resfriamento_simples.png', dpi=300, bbox_inches='tight')
plt.show()

# Tabela de resultados
print("Tabela de Resfriamento:")
print("Minuto | Temperatura")
print("-" * 23)
for i, temp in enumerate(temperaturas[:6]):
    print(f"{i:6d} | {temp:7.2f}°C")
print("...")
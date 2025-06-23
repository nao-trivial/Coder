import matplotlib.pyplot as plt
import numpy as np

# Valores
fatores_congestionamento = np.linspace(1.0, 3.0, 100)  # de 1.0 a 3.0
atrasos_iniciais = [0.5, 1, 2, 3]  # minutos

# Plot
plt.figure(figsize=(10, 6))
for A0 in atrasos_iniciais:
    atrasos_finais = A0 * np.exp(fatores_congestionamento)
    plt.plot(fatores_congestionamento, atrasos_finais, label=f'A₀ = {A0} min')

# Personalização
plt.title("🦋 Amplificação do Atraso Inicial pelo Fator de Congestionamento", fontsize=14)
plt.xlabel("Fator de Congestionamento (k)", fontsize=12)
plt.ylabel("Atraso Estimado Final (min)", fontsize=12)
plt.axhline(30, color='red', linestyle='--', label='⚠️ Limite crítico: 30 min')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Exibir
plt.show()
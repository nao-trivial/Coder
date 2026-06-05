import numpy as np
import matplotlib.pyplot as plt

# Configuração da figura
plt.figure(figsize=(8, 5))

# 1. Curva contínua – senoide amortecida (MHS subcrítico)
t = np.linspace(0, 8, 1000)
# Parâmetros: decaimento beta = 0.4, frequência angular ~1.2
y_cont = np.exp(-0.4 * t) * np.cos(2.5 * t)

# 2. Pontos discretos – amostragem da iteração (modelo com a negativo)
n = np.arange(0, 9)  # 9 iterações
# Simula uma sequência discreta típica de a = -0.6, b = 0.5 (apenas para ilustrar)
x0 = 1.2
a, b = -0.6, 0.5
x_disc = np.zeros_like(n, dtype=float)
x_disc[0] = x0
for i in range(1, len(n)):
    x_disc[i] = a * x_disc[i-1] + b

# 3. Plotagem
plt.plot(t, y_cont, 'b-', linewidth=2, alpha=0.8, label='Senoide amortecida (contínua)')
plt.scatter(n, x_disc, color='red', s=80, zorder=5, label='Iterações discretas')
plt.axhline(y=0, color='gray', linestyle='--', linewidth=0.8, alpha=0.5)

# 4. Título, subtítulo e rótulos
plt.title('Quando a é negativo: o ritmo da oscilação emocional', fontsize=14, weight='bold')
plt.suptitle('0 > a > -1 – o caso subcrítico do relacionamento', fontsize=11, style='italic', y=0.96)
plt.xlabel('Tempo (n / iteração)')
plt.ylabel('Estado emocional')
plt.legend(loc='upper right')
plt.grid(True, alpha=0.3)
plt.ylim(-1.2, 1.5)

# Exibir ou salvar (descomente a linha abaixo para salvar como arquivo)
# plt.savefig('slide1_grafico.png', dpi=150, bbox_inches='tight')
plt.show()

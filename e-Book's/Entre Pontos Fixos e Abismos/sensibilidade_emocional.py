import matplotlib.pyplot as plt
import numpy as np

# Definição dos dois cenários
cenarios = ['Cenário 1\n(a = 1,2 , b = 5)', 
            'Cenário 2\n(a = 0,9 , b = 2)']
pontos_fixos = [-25, 20]

# Cores para destacar a diferença
cores = ['#d62728', '#2ca02c']  # vermelho e verde

# Criar figura
fig, ax = plt.subplots(figsize=(8, 5))

# Barras verticais representando o valor do ponto fixo
bars = ax.bar(cenarios, pontos_fixos, color=cores, alpha=0.7, edgecolor='black', linewidth=1.5)

# Adicionar anotações acima das barras
for bar, valor in zip(bars, pontos_fixos):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
            f'{valor}', ha='center', va='bottom', fontsize=14, fontweight='bold')

# Destacar a grande variação com uma seta dupla
ax.annotate('', xy=(0.8, 15), xytext=(0.2, -20),
            arrowprops=dict(arrowstyle='<->', lw=2, color='gray', alpha=0.6))
ax.text(0.5, -2, 'Salto de –25 para +20\ncom pequenas mudanças em a e b',
        ha='center', fontsize=12, color='gray', style='italic',
        bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))

# Configurar eixos
ax.axhline(0, color='black', linewidth=0.8)  # linha de referência no zero
ax.set_ylabel('Ponto Fixo (x*)', fontsize=12)
ax.set_title('Sensibilidade à alteração dos parâmetros\n"Caos emocional"', fontsize=14, pad=20)
ax.set_ylim(-30, 30)
ax.grid(axis='y', linestyle='--', alpha=0.4)

# Explicação adicional
ax.text(0.5, -27, '⬅  Cenário original (a=1,2 , b=5) → x* = –25\n'
        '➡  Nova condição (a=0,9 , b=2) → x* = +20',
        transform=ax.transAxes, ha='center', fontsize=10,
        bbox=dict(facecolor='#f0f0f0', edgecolor='none', alpha=0.8))

plt.tight_layout()
plt.show()
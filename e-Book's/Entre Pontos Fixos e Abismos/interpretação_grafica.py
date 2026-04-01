import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# =============================================================================
# 1. Configuração da curva emocional E(t)
# =============================================================================
# Definimos um polinômio cúbico: E(t) = a*t^3 + b*t^2 + c*t + d
# Escolhemos coeficientes que gerem uma curva com:
#   - Parte inicial com concavidade para baixo (E'' < 0)
#   - Um ponto de inflexão (E'' = 0)
#   - Parte final com concavidade para cima (E'' > 0)
# Além disso, a curva deve ser positiva para representar bem-estar.

t = np.linspace(0, 10, 300)
# Coeficientes: E = -0.1*(t-5)^3 + 4  -> forma cúbica simples
# Vamos usar: E = -0.05*(t-5)**3 + 3
E = -0.05 * (t - 5)**3 + 3

# Garantir que não fique negativa (para o exemplo)
E = np.maximum(E, 0.2)

# =============================================================================
# 2. Criar a figura e os eixos
# =============================================================================
fig, ax = plt.subplots(figsize=(12, 6))
ax.set_facecolor('#fef9f0')  # fundo suave
fig.patch.set_facecolor('#fef9f0')

# Plot da curva principal
ax.plot(t, E, color='#2c3e50', linewidth=3, label=r'$E(t)$ – Estado emocional')

# =============================================================================
# 3. Integral (área sob a curva) - de t=2 a t=8
# =============================================================================
t_integral = np.linspace(2, 8, 150)
E_integral = -0.05 * (t_integral - 5)**3 + 3
E_integral = np.maximum(E_integral, 0.2)

# Preencher a área
ax.fill_between(t_integral, 0, E_integral, color='#3498db', alpha=0.25,
                 label=r'Área = $\int_{t_1}^{t_2} E(t)\,dt$ (bem-estar acumulado)')

# =============================================================================
# 4. Derivada (reta tangente) em t = 3.5
# =============================================================================
t0 = 3.5
E0 = -0.05 * (t0 - 5)**3 + 3
# Derivada analítica: E'(t) = -0.15*(t-5)^2
deriv = -0.15 * (t0 - 5)**2
# Reta tangente: y = E0 + deriv*(t - t0)
t_tan = np.array([t0 - 1.5, t0 + 1.5])
E_tan = E0 + deriv * (t_tan - t0)
ax.plot(t_tan, E_tan, '--', color='#e67e22', linewidth=2.5,
        label=f'Derivada $E\'({t0})$ = inclinação (velocidade emocional)')

# Marcar ponto de tangência
ax.plot(t0, E0, 'o', color='#e67e22', markersize=8, zorder=5)

# =============================================================================
# 5. Segunda derivada: mostrar concavidade através de setas e texto
# =============================================================================
# Ponto de inflexão: t=5 (pois E''(t)= -0.3*(t-5), zera em t=5)
t_inflexao = 5
E_inflexao = -0.05 * (t_inflexao - 5)**3 + 3

# Adicionar setas curvas para indicar concavidade
# Concavidade para baixo (E'' < 0) antes de t=5
ax.annotate('', xy=(3, 2.2), xytext=(2.5, 2.8),
            arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=2))
ax.text(2.2, 2.9, r'$E''(t) < 0$', fontsize=10, color='#e74c3c',
        bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.7))

# Concavidade para cima (E'' > 0) depois de t=5
ax.annotate('', xy=(7, 3.2), xytext=(6.5, 2.5),
            arrowprops=dict(arrowstyle='->', color='#27ae60', lw=2))
ax.text(7.2, 3.3, r'$E''(t) > 0$', fontsize=10, color='#27ae60',
        bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.7))

# Marcar ponto de inflexão
ax.plot(t_inflexao, E_inflexao, 's', color='#8e44ad', markersize=8, zorder=5,
        label=f'Ponto de inflexão ($E\'\'(t)=0$) – mudança na aceleração emocional')

# =============================================================================
# 6. Ajustes estéticos e anotações conceituais
# =============================================================================
ax.set_xlabel('Tempo $t$', fontsize=12)
ax.set_ylabel('Estado emocional $E(t)$', fontsize=12)
ax.set_title('A matemática da experiência emocional\nDerivada · Integral · Segunda derivada',
             fontsize=16, pad=20)

# Legenda
ax.legend(loc='upper left', framealpha=0.9, fontsize=9)

# Adicionar uma caixa de texto com a filosofia
filosofia = (
    "O que importa não é apenas o pico (derivada),\n"
    "nem só a área total (integral), mas também\n"
    "como a mudança está mudando (2ª derivada).\n"
    "Aceleração emocional indica inflexão –\n"
    "você está prestes a mudar de direção?"
)
ax.text(0.98, 0.02, filosofia, transform=ax.transAxes,
        fontsize=9, verticalalignment='bottom', horizontalalignment='right',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#ecf0f1', alpha=0.8),
        family='monospace')

# Remover bordas desnecessárias
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(True, linestyle=':', alpha=0.6)

# Ajustar limites
ax.set_ylim(0, 4.5)
ax.set_xlim(0, 10)

# =============================================================================
# 7. Salvar a imagem
# =============================================================================
plt.tight_layout()
plt.savefig('integral_emocional.png', dpi=200, bbox_inches='tight')
plt.show()

print("✅ Imagem salva como 'integral_emocional.png'")
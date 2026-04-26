import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# Função para gerar a sequência da iteração linear
def iteracao_linear(a, b, x0, n):
    """Gera sequência da iteração linear x_{n+1} = a*x_n + b"""
    x = np.zeros(n)
    x[0] = x0
    for i in range(1, n):
        x[i] = a * x[i-1] + b
    return x

# Função para calcular ponto fixo
def ponto_fixo(a, b):
    """Calcula ponto fixo da iteração (se |a| < 1)"""
    if abs(a) < 1:
        return b / (1 - a)
    return None

# Configuração dos parâmetros para diferentes cenários
cenarios = [
    # a, b, x0, nome, cor
    (1.1, 0.2, 5, "Ansiedade: a > 1 (explosivo)", "red"),
    (1.1, -0.5, 5, "Depressão: a > 1 mas b negativo", "darkred"),
    (0.9, 0.1, 50, "AMORTECIMENTO a < 1", "blue"),
    (0.9, 2.0, 50, "a < 1 mas b positivo salva!", "green"),
    (0.5, 10, 0, "b alto = cuidado constante", "purple"),
    (-0.7, 5, 20, "OSCILAÇÃO: a negativo", "orange"),
    (1.0, 1.0, 0, "CRESCIMENTO LINEAR: a = 1", "brown"),
    (-1.0, 5, 10, "CICLO PERIÓDICO: a = -1", "pink")
]

# Criar figura com layout mais organizado
fig = plt.figure(figsize=(15, 12))
fig.suptitle('DINÂMICA DE RELACIONAMENTOS: Xₙ₊₁ = a·Xₙ + b', 
             fontsize=18, fontweight='bold', y=0.98)

# Grid de subplots
n_cenarios = len(cenarios)
n_cols = 2
n_rows = (n_cenarios + 1) // n_cols

gs = gridspec.GridSpec(n_rows, n_cols, hspace=0.4, wspace=0.3)

for idx, (a, b, x0, titulo, cor) in enumerate(cenarios):
    ax = plt.subplot(gs[idx])
    
    # Gerar dados
    n_iteracoes = 20
    x = iteracao_linear(a, b, x0, n_iteracoes)
    
    # Plotar a evolução
    ax.plot(range(n_iteracoes), x, 'o-', color=cor, linewidth=2, markersize=4, 
            label=f'X₀={x0}')
    
    # Adicionar linha do ponto fixo se convergir
    p_fixo = ponto_fixo(a, b)
    if p_fixo is not None:
        ax.axhline(y=p_fixo, color='gray', linestyle='--', alpha=0.5, 
                   label=f'Ponto fixo = {p_fixo:.1f}')
    
    # Linha y = x para referência
    ax.axhline(y=x0, color='black', linestyle=':', alpha=0.3, linewidth=0.5)
    
    # Configurações do gráfico
    ax.set_title(f'{titulo}\na = {a}, b = {b}', fontsize=11, pad=10)
    ax.set_xlabel('Tempo (interações)', fontsize=9)
    ax.set_ylabel('Estado do Relacionamento (Xₙ)', fontsize=9)
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.legend(fontsize=8, loc='best')
    
    # Adicionar setas indicando tendência
    if len(x) >= 2:
        ultimo_valor = x[-1]
        penultimo_valor = x[-2]
        if ultimo_valor > penultimo_valor:
            ax.text(0.7, 0.9, '↗ Crescendo', transform=ax.transAxes, 
                   fontsize=8, color='darkgreen', fontweight='bold')
        elif ultimo_valor < penultimo_valor:
            ax.text(0.7, 0.9, '↘ Decaindo', transform=ax.transAxes, 
                   fontsize=8, color='darkred', fontweight='bold')
    
    # Destacar área crítica (valores muito baixos)
    lim_inf = min(x) * 0.8 if min(x) < 0 else 0
    if lim_inf < 0:
        ax.axhspan(lim_inf, 0, alpha=0.1, color='red', 
                  label='Zona de risco')
    
    # Adicionar anotação sobre o papel de b
    if abs(a) < 1 and b != 0:
        ax.text(0.05, 0.05, f'b mantém em {p_fixo:.1f}', 
               transform=ax.transAxes, fontsize=8, 
               bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.5))

# Adicionar gráfico comparativo especial
ax_comp = plt.subplot(gs[-1])
ax_comp.set_title('COMPARAÇÃO: O PODER DO PARÂMETRO b', fontsize=12, fontweight='bold')

# Dois cenários com mesmo 'a' ruim, mas 'b' diferente
a_ruim = 1.2  # > 1, tende a explodir
b1 = 0.1      # b pequeno
b2 = -0.8     # b negativo significativo

x1 = iteracao_linear(a_ruim, b1, 5, 15)
x2 = iteracao_linear(a_ruim, b2, 5, 15)

ax_comp.plot(range(15), x1, 's-', color='red', linewidth=2, 
            label=f'a={a_ruim}, b={b1} (explode!)', markersize=5)
ax_comp.plot(range(15), x2, 'o-', color='green', linewidth=2, 
            label=f'a={a_ruim}, b={b2} (contido)', markersize=5)

ax_comp.set_xlabel('Tempo (interações)', fontsize=10)
ax_comp.set_ylabel('Estado do Relacionamento', fontsize=10)
ax_comp.grid(True, alpha=0.3)
ax_comp.legend(fontsize=9)
ax_comp.text(0.5, 0.95, 'Mesmo "a" RUIM, mas "b" controla a explosão!', 
            transform=ax_comp.transAxes, fontsize=10, ha='center',
            bbox=dict(boxstyle="round,pad=0.5", facecolor="lightblue", alpha=0.8))

# Adicionar texto explicativo geral
texto_explicativo = """
ANÁLISE DOS PARÂMETROS:
• a = MULTIPLICADOR EMOCIONAL: Como reagem aos acontecimentos
  |a| > 1: Explosões emocionais (crises)
  |a| < 1: Dissipação natural dos problemas
  a negativo: Oscilações entre altos e baixos
  
• b = ENTRADA CONSTANTE: Gestos diários de afeto
  b positivo: Carinho, atenção, cuidado
  b negativo: Críticas, negligência, desinteresse
  
O SEGREDO: Mesmo com 'a' ruim, um 'b' bem ajustado
pode manter o sistema estável através do cuidado constante!
"""
fig.text(0.02, 0.02, texto_explicativo, fontsize=9, 
         bbox=dict(boxstyle="round,pad=0.5", facecolor="lightyellow", alpha=0.7))

plt.tight_layout(rect=[0, 0.05, 1, 0.96])
plt.show()

# Função para simulação interativa (opcional - pode rodar separadamente)
def simulador_interativo():
    """Permite ao usuário testar diferentes parâmetros"""
    print("\n" + "="*60)
    print("🎮 SIMULADOR DE RELACIONAMENTO - ITERAÇÃO LINEAR")
    print("="*60)
    
    while True:
        try:
            print("\nDigite os parâmetros (ou 'sair' para encerrar):")
            a = float(input("Multiplicador emocional (a) [ex: 0.8]: "))
            b = float(input("Cuidado constante (b) [ex: 2.0]: "))
            x0 = float(input("Estado inicial [ex: 10.0]: "))
            n = int(input("Número de iterações [ex: 20]: "))
            
            # Gerar simulação
            x = iteracao_linear(a, b, x0, n)
            p_fixo = ponto_fixo(a, b)
            
            # Plotar simulação individual
            fig2, ax2 = plt.subplots(figsize=(10, 6))
            ax2.plot(range(n), x, 'o-', color='darkblue', linewidth=2)
            
            if p_fixo:
                ax2.axhline(y=p_fixo, color='red', linestyle='--', 
                          label=f'Ponto fixo = {p_fixo:.2f}')
            
            ax2.set_title(f'Simulação: Xₙ₊₁ = {a}·Xₙ + {b}', fontsize=14)
            ax2.set_xlabel('Tempo (interações)')
            ax2.set_ylabel('Estado do Relacionamento')
            ax2.grid(True, alpha=0.3)
            ax2.legend()
            
            # Adicionar diagnóstico
            diagnostico = "\n".join([
                f"DIAGNÓSTICO:",
                f"• Multiplicador emocional (a) = {a}",
                f"• Cuidado constante (b) = {b}",
                f"• Estado inicial = {x0}",
                f"• Estado final = {x[-1]:.2f}",
                f"• Variação total = {x[-1] - x0:.2f}"
            ])
            
            if abs(a) > 1:
                diagnostico += "\n⚠️ ALERTA: Sistema INSTÁVEL (|a| > 1)"
            elif abs(a) < 1 and p_fixo:
                diagnostico += f"\nSistema CONVERGE para {p_fixo:.2f}"
            
            fig2.text(0.02, 0.02, diagnostico, fontsize=9,
                     bbox=dict(boxstyle="round,pad=0.5", facecolor="lightgreen", alpha=0.7))
            
            plt.tight_layout(rect=[0, 0.15, 1, 0.95])
            plt.show()
            
            # Perguntar se quer continuar
            continuar = input("\nNova simulação? (s/n): ").lower()
            if continuar != 's':
                break
                
        except ValueError:
            print("Entrada inválida! Use números.")
        except KeyboardInterrupt:
            break

# Perguntar se quer usar o simulador interativo
print("\n" + "="*60)
print("Gráficos gerados! Deseja usar o simulador interativo?")
usar_simulador = input("Digite 's' para simular ou qualquer tecla para sair: ")

if usar_simulador.lower() == 's':
    simulador_interativo()

print("\nAnálise completa! Lembre-se:")
print("   • 'a' define a REATIVIDADE emocional")
print("   • 'b' representa os GESTOS CONSTANTES de afeto")
print("   • O equilíbrio vem do ajuste cuidadoso de ambos!")
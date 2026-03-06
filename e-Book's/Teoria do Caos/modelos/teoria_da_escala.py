import matplotlib.pyplot as plt
import numpy as np

# Configuração de estilo
plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['figure.figsize'] = [12, 8]
plt.rcParams['font.size'] = 12

def fibonacci(n):
    """Gera os primeiros n números da sequência de Fibonacci"""
    fib = [1, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib[:n]

def exponencial(n, taxa=1.618):
    """Crescimento exponencial com base na taxa áurea para comparação"""
    return [taxa**i for i in range(n)]

def exponencial_malthus(n, r=0.5, P0=1):
    """Modelo exponencial clássico: P(t) = P0 * e^(r*t)"""
    t = np.arange(n)
    return P0 * np.exp(r * t)

# Parâmetros
n_termos = 15  # Número de termos para comparar
t = np.arange(n_termos)

# Gerando os dados
fib = fibonacci(n_termos)
exp_ouro = exponencial(n_termos)  # Crescimento com razão áurea
exp_malthus = exponencial_malthus(n_termos, r=0.5)  # Crescimento malthusiano suave

# Criação da figura com subplots
fig = plt.figure(figsize=(16, 10))

# Plot 1: Comparação direta (escala linear)
ax1 = plt.subplot(2, 2, 1)
ax1.plot(t, fib, 'o-', linewidth=2.5, markersize=8, label='Fibonacci', color='#2E86AB')
ax1.plot(t, exp_ouro, 's-', linewidth=2, markersize=6, label='Exponencial (φ = 1.618)', color='#A23B72', alpha=0.8)
ax1.plot(t, exp_malthus, '^-', linewidth=2, markersize=6, label='Exponencial Malthus (r=0.5)', color='#F18F01', alpha=0.8)
ax1.set_xlabel('Tempo (t)', fontsize=12)
ax1.set_ylabel('Valor', fontsize=12)
ax1.set_title('Comparação: Fibonacci vs Crescimento Exponencial', fontsize=14, fontweight='bold')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Plot 2: Escala logarítmica (revela a natureza exponencial)
ax2 = plt.subplot(2, 2, 2)
ax2.semilogy(t, fib, 'o-', linewidth=2.5, markersize=8, label='Fibonacci', color='#2E86AB')
ax2.semilogy(t, exp_ouro, 's-', linewidth=2, markersize=6, label='Exponencial (φ = 1.618)', color='#A23B72', alpha=0.8)
ax2.semilogy(t, exp_malthus, '^-', linewidth=2, markersize=6, label='Exponencial Malthus (r=0.5)', color='#F18F01', alpha=0.8)
ax2.set_xlabel('Tempo (t)', fontsize=12)
ax2.set_ylabel('Valor (escala log)', fontsize=12)
ax2.set_title('Escala Logarítmica: Fibonacci é aproximadamente exponencial', fontsize=14, fontweight='bold')
ax2.legend()
ax2.grid(True, alpha=0.3)

# Plot 3: Razão entre termos consecutivos
ax3 = plt.subplot(2, 2, 3)
razao_fib = [fib[i+1]/fib[i] for i in range(len(fib)-1)]
razao_ouro = [exp_ouro[i+1]/exp_ouro[i] for i in range(len(exp_ouro)-1)]
razao_malthus = [exp_malthus[i+1]/exp_malthus[i] for i in range(len(exp_malthus)-1)]

t_razao = t[1:]

ax3.axhline(y=1.618, color='gray', linestyle='--', linewidth=1, alpha=0.7, label='Número de Ouro (φ)')
ax3.plot(t_razao, razao_fib, 'o-', linewidth=2.5, markersize=8, label='Razão Fibonacci', color='#2E86AB')
ax3.plot(t_razao, razao_ouro, 's-', linewidth=2, markersize=6, label='Razão Exponencial φ', color='#A23B72', alpha=0.8)
ax3.plot(t_razao, razao_malthus, '^-', linewidth=2, markersize=6, label='Razão Exponencial Malthus', color='#F18F01', alpha=0.8)
ax3.set_xlabel('Tempo (t)', fontsize=12)
ax3.set_ylabel('Razão (P(t+1)/P(t))', fontsize=12)
ax3.set_title('Convergência da Razão de Fibonacci para φ', fontsize=14, fontweight='bold')
ax3.legend()
ax3.grid(True, alpha=0.3)

# Plot 4: Comparação percentual do desvio
ax4 = plt.subplot(2, 2, 4)
# Ajustando exponencial para mesma base no tempo 0
fib_normalizado = [f/fib[0] for f in fib]
exp_ajustado = [exp_ouro[0]/fib[0]] + [exp_ouro[i]/fib[0] for i in range(1, len(exp_ouro))]

desvio = [(fib_normalizado[i] - exp_ajustado[i])/exp_ajustado[i] * 100 for i in range(n_termos)]

ax4.bar(t, desvio, color='#2E86AB', alpha=0.7, edgecolor='black', linewidth=1)
ax4.axhline(y=0, color='red', linestyle='--', linewidth=1, label='Exponencial perfeito')
ax4.set_xlabel('Tempo (t)', fontsize=12)
ax4.set_ylabel('Desvio percentual (%)', fontsize=12)
ax4.set_title('Desvio de Fibonacci em relação ao crescimento exponencial', fontsize=14, fontweight='bold')
ax4.legend()
ax4.grid(True, alpha=0.3, axis='y')

plt.suptitle('Fibonacci: Exponencial Disfarçado de Harmonia', fontsize=18, fontweight='bold', y=1.02)
plt.tight_layout()
plt.show()

# Análise adicional: tabela comparativa
print("\n" + "="*80)
print("TABELA COMPARATIVA: FIBONACCI vs EXPONENCIAL")
print("="*80)
print(f"{'t':<5} {'Fibonacci':<12} {'Exponencial φ':<15} {'Malthus (r=0.5)':<18} {'Razão Fib':<12}")
print("-"*80)

for i in range(n_termos):
    fib_val = fib[i]
    exp_ouro_val = exp_ouro[i]
    exp_malthus_val = exp_malthus[i]
    razao = fib_val/fib[i-1] if i > 0 else 0
    
    if i == 0:
        print(f"{i:<5} {fib_val:<12.0f} {exp_ouro_val:<15.2f} {exp_malthus_val:<18.2f} {'---':<12}")
    else:
        print(f"{i:<5} {fib_val:<12.0f} {exp_ouro_val:<15.2f} {exp_malthus_val:<18.2f} {razao:<12.4f}")

print("="*80)
print(f"\n📊 ANÁLISE:")
print(f"   • Razão Fibonacci converge para: {razao_fib[-1]:.6f} (φ ≈ 1.618034)")
print(f"   • Após {n_termos} termos, Fibonacci é {fib[-1]:.0f} × maior que o termo inicial")
print(f"   • Malthus (r=0.5) cresce {exp_malthus[-1]:.2f} × em {n_termos} unidades de tempo")
print("="*80)

# Demonstração da relação com o modelo logístico
print("\n" + "="*80)
print("🔬 CONEXÃO COM O MODELO LOGÍSTICO (VERHULST):")
print("="*80)
print("""
A diferença fundamental:

• FIBONACCI / EXPONENCIAL: P(t+1) = r·P(t)    (crescimento sem limites)
• LOGÍSTICO: dP/dt = rP(1 - P/K)              (crescimento com limite K)

Enquanto Fibonacci acelera infinitamente, o modelo logístico:
- Cresce exponencialmente no início
- Desacelera ao se aproximar da capacidade K
- Estabiliza em equilíbrio dinâmico

O número de ouro (φ) é a taxa de crescimento apenas no regime inicial.
O mundo real sempre impõe um K.
""")
print("="*80)
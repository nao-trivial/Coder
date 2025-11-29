import matplotlib.pyplot as plt
import numpy as np

# Configuração do gráfico 3D
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

# Definindo os vetores
u = np.array([4, 3, 2])
v = np.array([1, 2, 2])
v_oposto = -v  # Vetor oposto a v
soma_u_menos_v = u + v_oposto  # u + (-v)

# Origem dos vetores
origem = np.array([0, 0, 0])

# Plot do vetor u
ax.quiver(*origem, *u, color='r', arrow_length_ratio=0.1, 
          label=f'Vetor u ({u[0]},{u[1]},{u[2]})', linewidth=3, alpha=0.8)

# Plot do vetor v
ax.quiver(*origem, *v, color='b', arrow_length_ratio=0.1, 
          label=f'Vetor v ({v[0]},{v[1]},{v[2]})', linewidth=3, alpha=0.8)

# Plot do vetor -v (oposto de v)
ax.quiver(*origem, *v_oposto, color='orange', arrow_length_ratio=0.1, 
          label=f'Vetor -v ({v_oposto[0]},{v_oposto[1]},{v_oposto[2]})', 
          linewidth=3, alpha=0.8, linestyle='--')

# Plot da soma u + (-v) - PRINCIPAL
ax.quiver(*origem, *soma_u_menos_v, color='green', arrow_length_ratio=0.1, 
          label=f'Soma u + (-v) = ({soma_u_menos_v[0]},{soma_u_menos_v[1]},{soma_u_menos_v[2]})', 
          linewidth=4)

# Destacar o processo de soma: primeiro u, depois a partir de u somamos -v
ax.quiver(*u, *v_oposto, color='purple', arrow_length_ratio=0.1, 
          label='Componente -v adicionado a u', linewidth=2, alpha=0.6, linestyle=':')

# Configurações do gráfico
lim = 6
ax.set_xlim([-lim, lim])
ax.set_ylim([-lim, lim])
ax.set_zlim([-lim, lim])
ax.set_xlabel('Eixo X', fontsize=12)
ax.set_ylabel('Eixo Y', fontsize=12)
ax.set_zlabel('Eixo Z', fontsize=12)
ax.set_title('Soma Vetorial: u + (-v) no R³', fontsize=14, fontweight='bold')

# Grade para melhor visualização
ax.grid(True, alpha=0.3)

# Legendas
ax.legend(loc='upper left', bbox_to_anchor=(0, 1))

# Ângulo de visualização
ax.view_init(elev=20, azim=30)

plt.tight_layout()
plt.show()

# Criação de um segundo gráfico que mostra o processo passo a passo
fig2 = plt.figure(figsize=(14, 10))
ax2 = fig2.add_subplot(111, projection='3d')

# PASSO 1: Mostrar apenas u
ax2.quiver(*origem, *u, color='r', arrow_length_ratio=0.1, 
           label=f'1. Vetor u ({u[0]},{u[1]},{u[2]})', linewidth=4)

# PASSO 2: Mostrar -v partindo da origem (linha tracejada)
ax2.quiver(*origem, *v_oposto, color='orange', arrow_length_ratio=0.1, 
           label=f'2. Vetor -v ({v_oposto[0]},{v_oposto[1]},{v_oposto[2]})', 
           linewidth=3, alpha=0.7, linestyle='--')

# PASSO 3: Mostrar -v transladado para a ponta de u (método do paralelogramo)
ax2.quiver(*u, *v_oposto, color='orange', arrow_length_ratio=0.1, 
           linewidth=3, alpha=0.7, linestyle='--')

# PASSO 4: Mostrar a soma resultante
ax2.quiver(*origem, *soma_u_menos_v, color='green', arrow_length_ratio=0.1, 
           label=f'3. Soma u + (-v) = ({soma_u_menos_v[0]},{soma_u_menos_v[1]},{soma_u_menos_v[2]})', 
           linewidth=5)

# Linha pontilhada conectando u à soma (completando o paralelogramo)
ax2.plot([u[0], soma_u_menos_v[0]], [u[1], soma_u_menos_v[1]], [u[2], soma_u_menos_v[2]], 
         'k:', alpha=0.5, label='Linhas do paralelogramo')
ax2.plot([v_oposto[0], soma_u_menos_v[0]], [v_oposto[1], soma_u_menos_v[1]], [v_oposto[2], soma_u_menos_v[2]], 
         'k:', alpha=0.5)

# Configurações do segundo gráfico
ax2.set_xlim([-lim, lim])
ax2.set_ylim([-lim, lim])
ax2.set_zlim([-lim, lim])
ax2.set_xlabel('Eixo X', fontsize=12)
ax2.set_ylabel('Eixo Y', fontsize=12)
ax2.set_zlabel('Eixo Z', fontsize=12)
ax2.set_title('Processo da Soma: u + (-v) - Método do Paralelogramo', fontsize=14, fontweight='bold')
ax2.grid(True, alpha=0.3)
ax2.legend(loc='upper left', bbox_to_anchor=(0, 1))
ax2.view_init(elev=20, azim=30)

plt.tight_layout()
plt.show()

# Exibir informações detalhadas no console
print("=" * 70)
print("ANÁLISE DA SOMA VETORIAL: u + (-v)")
print("=" * 70)
print(f"Vetor u: {u}")
print(f"Vetor v: {v}")
print(f"Vetor -v: {v_oposto}")
print(f"Componente a componente:")
print(f"  u_x + (-v_x) = {u[0]} + {v_oposto[0]} = {soma_u_menos_v[0]}")
print(f"  u_y + (-v_y) = {u[1]} + {v_oposto[1]} = {soma_u_menos_v[1]}")
print(f"  u_z + (-v_z) = {u[2]} + {v_oposto[2]} = {soma_u_menos_v[2]}")
print(f"Resultado final: u + (-v) = {soma_u_menos_v}")
print("=" * 70)

# Verificação alternativa: u - v
print("VERIFICAÇÃO: u - v = u + (-v)")
print(f"u - v = {u - v}")
print(f"u + (-v) = {u + (-v)}")
print(f"Resultados iguais? {np.array_equal(u - v, u + (-v))}")
print("=" * 70)
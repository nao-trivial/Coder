import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

# ============================================================
# 1. DEFINIÇÃO DA REDE CRISTALINA (2D)
# ============================================================
# Vetores primitivos da rede (rede quadrada)
a1 = np.array([1.0, 0.0])   # vetor ao longo do eixo x
a2 = np.array([0.0, 1.0])   # vetor ao longo do eixo y

# Número de células em cada direção
n_cells = 4  # cria uma grade de 4x4 células

# Gera as posições dos "átomos" nos nós da rede
atoms = []
for i in range(-n_cells, n_cells+1):
    for j in range(-n_cells, n_cells+1):
        pos = i*a1 + j*a2
        atoms.append(pos)
atoms = np.array(atoms)

# ============================================================
# 2. FUNÇÃO PARA CAMPOS VETORIAIS PERIÓDICOS
# ============================================================
# Em vez do campo central (com singularidade), criamos um campo
# periódico com a mesma periodicidade da rede.
# Exemplo: F(x,y) = ( sin(2π x), cos(2π y) )  - periódico com período 1
def campo_periodico(x, y):
    u = np.sin(2 * np.pi * x)
    v = np.cos(2 * np.pi * y)
    return u, v

# Malha para visualizar o campo vetorial
x_vals = np.linspace(-n_cells, n_cells, 20)
y_vals = np.linspace(-n_cells, n_cells, 20)
X, Y = np.meshgrid(x_vals, y_vals)
U, V = campo_periodico(X, Y)

# ============================================================
# 3. VISUALIZAÇÃO
# ============================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# ---- Subplot 1: Rede cristalina e vetores de translação ----
ax1.scatter(atoms[:,0], atoms[:,1], s=30, c='blue', alpha=0.6, label='Átomos')

# Desenha os vetores primitivos a1 e a2 partindo da origem
origem = np.array([0, 0])
ax1.arrow(origem[0], origem[1], a1[0], a1[1], 
          head_width=0.1, head_length=0.1, fc='red', ec='red', label=r'$\vec{a}_1$')
ax1.arrow(origem[0], origem[1], a2[0], a2[1], 
          head_width=0.1, head_length=0.1, fc='green', ec='green', label=r'$\vec{a}_2$')

# Exemplo de translação: escolhe um átomo e mostra seu transladado
atom_exemplo = np.array([1, 1])   # átomo na posição (1,1)
transladado = atom_exemplo + a1   # translada por a1
ax1.scatter(atom_exemplo[0], atom_exemplo[1], s=100, c='orange', marker='s', label='Átomo original')
ax1.scatter(transladado[0], transladado[1], s=100, c='purple', marker='^', label='Transladado por a1')
ax1.plot([atom_exemplo[0], transladado[0]], [atom_exemplo[1], transladado[1]], 'k--', alpha=0.7)

ax1.set_title('Rede Cristalina e Simetria Translacional')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_aspect('equal')
ax1.grid(True, alpha=0.3)
ax1.legend()
ax1.set_xlim(-n_cells-0.5, n_cells+0.5)
ax1.set_ylim(-n_cells-0.5, n_cells+0.5)

# ---- Subplot 2: Campo vetorial periódico (conexão com a ideia de vetores) ----
ax2.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=10, color='darkred', alpha=0.7)
ax2.set_title('Campo Vetorial Periódico (mesma periodicidade da rede)')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_aspect('equal')
ax2.grid(True, alpha=0.3)

# Sobreposição da rede para mostrar a periodicidade
for atom in atoms:
    ax2.scatter(atom[0], atom[1], s=10, c='blue', alpha=0.3)

ax2.set_xlim(-n_cells-0.5, n_cells+0.5)
ax2.set_ylim(-n_cells-0.5, n_cells+0.5)

plt.tight_layout()
plt.show()

# ============================================================
# 4. EXPLICAÇÃO DOS CONCEITOS (impressa no console)
# ============================================================
print("""
=== CONCEITOS IMPORTANTES ===

1. Simetria de translação: Um cristal é invariante quando transladado por um vetor da rede.
   Ou seja: a disposição dos átomos se repete periodicamente.

2. Vetores primitivos (a1, a2): São os menores vetores que geram toda a rede.
   Qualquer vetor de translação da rede é combinação linear inteira de a1 e a2.

3. Importância vetorial: Os vetores descrevem matematicamente a operação de translação.
   Eles formam o espaço recíproco, essencial para difração de raios X e propriedades eletrônicas.

4. Campo vetorial periódico: Muitas propriedades físicas (campo elétrico, densidade de corrente, etc.)
   em um cristal também são periódicas. O exemplo mostra um campo artificial com a mesma periodicidade
   da rede, ilustrando como a simetria se manifesta em grandezas vetoriais.
""")
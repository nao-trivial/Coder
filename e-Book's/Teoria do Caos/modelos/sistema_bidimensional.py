import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec
import warnings
warnings.filterwarnings('ignore')

class SistemaDinamicoBidimensional:
    """
    Classe para analisar o sistema dinâmico bidimensional:
    xₙ₊₁ = a₁·xₙ + c·yₙ + b₁
    yₙ₊₁ = a₂·yₙ + d·xₙ + b₂
    """
    
    def __init__(self, a1, c, b1, a2, d, b2):
        """
        Inicializa o sistema com os parâmetros dados.
        
        Parâmetros:
        -----------
        a1, c, b1: parâmetros da primeira equação
        a2, d, b2: parâmetros da segunda equação
        """
        self.a1 = a1
        self.c = c
        self.b1 = b1
        self.a2 = a2
        self.d = d
        self.b2 = b2
        
        # Matriz do sistema linear
        self.A = np.array([[a1, c], [d, a2]])
        self.b = np.array([b1, b2])
    
    def iterar(self, x0, y0, n=100):
        """
        Itera o sistema a partir das condições iniciais (x0, y0).
        
        Retorna:
        --------
        x_vals, y_vals: arrays com as trajetórias
        """
        x_vals = np.zeros(n+1)
        y_vals = np.zeros(n+1)
        x_vals[0] = x0
        y_vals[0] = y0
        
        for i in range(n):
            x_vals[i+1] = self.a1 * x_vals[i] + self.c * y_vals[i] + self.b1
            y_vals[i+1] = self.a2 * y_vals[i] + self.d * x_vals[i] + self.b2
        
        return x_vals, y_vals
    
    def ponto_fixo(self):
        """
        Calcula o ponto fixo do sistema (se existir).
        
        O ponto fixo satisfaz: x = a1*x + c*y + b1
                               y = a2*y + d*x + b2
                               
        Ou em forma matricial: (I - A)X = b
        """
        I = np.identity(2)
        M = I - self.A
        
        try:
            # Tenta resolver o sistema linear
            det = np.linalg.det(M)
            if abs(det) < 1e-10:
                return None, "Sistema singular ou indeterminado"
            
            ponto_fixo = np.linalg.solve(M, self.b)
            return ponto_fixo, "Ponto fixo encontrado"
            
        except np.linalg.LinAlgError:
            return None, "Não foi possível encontrar ponto fixo"
    
    def autovalores(self):
        """
        Calcula os autovalores da matriz do sistema.
        
        Retorna:
        --------
        autovalores: autovalores da matriz A
        raio_espectral: maior valor absoluto dos autovalores
        """
        autovalores = np.linalg.eigvals(self.A)
        raio_espectral = np.max(np.abs(autovalores))
        
        return autovalores, raio_espectral
    
    def analisar_estabilidade(self):
        """
        Analisa a estabilidade do sistema baseada nos autovalores.
        """
        autovalores, raio_espectral = self.autovalores()
        
        if raio_espectral < 1:
            estabilidade = "ESTÁVEL (raio espectral < 1)"
        elif raio_espectral > 1:
            estabilidade = "INSTÁVEL (raio espectral > 1)"
        else:
            estabilidade = "LIMÍTROFE (raio espectral = 1)"
        
        return autovalores, raio_espectral, estabilidade


def plot_sistema_completo(sistema, condicoes_iniciais, n_iteracoes=50, titulo="Sistema Dinâmico Bidimensional"):
    """
    Plota análise completa do sistema bidimensional.
    
    Parâmetros:
    -----------
    sistema: instância de SistemaDinamicoBidimensional
    condicoes_iniciais: lista de tuplas [(x0, y0), ...]
    n_iteracoes: número de iterações
    titulo: título do gráfico
    """
    
    # Configurar figura com subplots
    fig = plt.figure(figsize=(16, 10))
    gs = GridSpec(3, 3, figure=fig)
    
    # Cores para diferentes condições iniciais
    cores = ['blue', 'red', 'green', 'orange', 'purple', 'brown', 'pink', 'gray']
    marcadores = ['o', 's', '^', 'D', 'v', '>', '<', 'p']
    
    # 1. Trajetórias no espaço de fase (y vs x)
    ax1 = fig.add_subplot(gs[0:2, 0:2])
    
    # 2. Evolução temporal de x_n
    ax2 = fig.add_subplot(gs[0, 2])
    
    # 3. Evolução temporal de y_n
    ax3 = fig.add_subplot(gs[1, 2])
    
    # 4. Espaço de parâmetros (se aplicável)
    ax4 = fig.add_subplot(gs[2, :])
    
    # Armazenar todas as trajetórias
    todas_trajetorias = []
    
    # Plotar para cada condição inicial
    for idx, (x0, y0) in enumerate(condicoes_iniciais):
        cor = cores[idx % len(cores)]
        marcador = marcadores[idx % len(marcadores)]
        
        # Calcular trajetória
        x_vals, y_vals = sistema.iterar(x0, y0, n_iteracoes)
        todas_trajetorias.append((x_vals, y_vals))
        
        # Plotar no espaço de fase
        ax1.plot(x_vals, y_vals, color=cor, linewidth=1.5, alpha=0.7, 
                label=f'(x₀={x0}, y₀={y0})')
        ax1.scatter(x_vals[0], y_vals[0], color=cor, s=100, marker=marcador, 
                   edgecolor='black', zorder=5)
        ax1.scatter(x_vals[-1], y_vals[-1], color=cor, s=150, marker='*', 
                   edgecolor='black', zorder=5)
        
        # Plotar evolução temporal de x
        ax2.plot(range(n_iteracoes+1), x_vals, color=cor, linewidth=1.5, 
                alpha=0.7, label=f'x₀={x0}')
        ax2.scatter(0, x_vals[0], color=cor, s=50, marker=marcador, 
                   edgecolor='black', zorder=5)
        
        # Plotar evolução temporal de y
        ax3.plot(range(n_iteracoes+1), y_vals, color=cor, linewidth=1.5, 
                alpha=0.7, label=f'y₀={y0}')
        ax3.scatter(0, y_vals[0], color=cor, s=50, marker=marcador, 
                   edgecolor='black', zorder=5)
    
    # Configurar gráfico do espaço de fase
    ax1.set_xlabel('xₙ', fontsize=12)
    ax1.set_ylabel('yₙ', fontsize=12)
    ax1.set_title('Espaço de Fase (Trajetórias)', fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    ax1.legend(loc='best', fontsize=9)
    ax1.axhline(0, color='black', linewidth=0.5, alpha=0.5)
    ax1.axvline(0, color='black', linewidth=0.5, alpha=0.5)
    
    # Marcar ponto fixo (se existir)
    ponto_fixo, mensagem = sistema.ponto_fixo()
    if ponto_fixo is not None:
        ax1.scatter(ponto_fixo[0], ponto_fixo[1], color='black', s=200, 
                   marker='X', label='Ponto Fixo', zorder=6)
        ax1.text(ponto_fixo[0], ponto_fixo[1], ' PF', fontsize=11, 
                fontweight='bold', verticalalignment='center')
    
    # Configurar gráfico da evolução de x
    ax2.set_xlabel('Iteração (n)', fontsize=10)
    ax2.set_ylabel('xₙ', fontsize=10)
    ax2.set_title('Evolução Temporal de x', fontsize=12, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.legend(loc='best', fontsize=8)
    
    # Configurar gráfico da evolução de y
    ax3.set_xlabel('Iteração (n)', fontsize=10)
    ax3.set_ylabel('yₙ', fontsize=10)
    ax3.set_title('Evolução Temporal de y', fontsize=12, fontweight='bold')
    ax3.grid(True, alpha=0.3)
    ax3.legend(loc='best', fontsize=8)
    
    # Análise de estabilidade no quarto subplot
    ax4.axis('off')
    
    # Informações do sistema
    info_text = f"PARÂMETROS DO SISTEMA:\n"
    info_text += f"xₙ₊₁ = {sistema.a1:.3f}·xₙ + {sistema.c:.3f}·yₙ + {sistema.b1:.3f}\n"
    info_text += f"yₙ₊₁ = {sistema.a2:.3f}·yₙ + {sistema.d:.3f}·xₙ + {sistema.b2:.3f}\n\n"
    
    info_text += f"ANÁLISE DE ESTABILIDADE:\n"
    autovalores, raio_espectral, estabilidade = sistema.analisar_estabilidade()
    info_text += f"Autovalores: {autovalores[0]:.4f}, {autovalores[1]:.4f}\n"
    info_text += f"Raio Espectral (ρ): {raio_espectral:.4f}\n"
    info_text += f"Estabilidade: {estabilidade}\n\n"
    
    info_text += f"PONTO FIXO:\n"
    if ponto_fixo is not None:
        info_text += f"x* = {ponto_fixo[0]:.4f}, y* = {ponto_fixo[1]:.4f}\n"
    else:
        info_text += f"{mensagem}\n"
    
    info_text += f"\nCONDIÇÕES INICIAIS ANALISADAS:\n"
    for idx, (x0, y0) in enumerate(condicoes_iniciais):
        info_text += f"{idx+1}. (x₀={x0}, y₀={y0})\n"
    
    ax4.text(0.05, 0.95, info_text, transform=ax4.transAxes, fontsize=10,
             verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    
    plt.suptitle(titulo, fontsize=16, fontweight='bold', y=0.98)
    plt.tight_layout()
    plt.show()
    
    # Imprimir informações adicionais no console
    print("="*70)
    print("ANÁLISE COMPLETA DO SISTEMA")
    print("="*70)
    print(f"\nEquações do sistema:")
    print(f"  xₙ₊₁ = {sistema.a1}·xₙ + {sistema.c}·yₙ + {sistema.b1}")
    print(f"  yₙ₊₁ = {sistema.a2}·yₙ + {sistema.d}·xₙ + {sistema.b2}")
    
    print(f"\nMatriz do sistema A = [[{sistema.a1}, {sistema.c}], [{sistema.d}, {sistema.a2}]]")
    print(f"Vetor de constantes b = [{sistema.b1}, {sistema.b2}]")
    
    print(f"\nAutovalores: λ₁ = {autovalores[0]:.6f}, λ₂ = {autovalores[1]:.6f}")
    print(f"Raio espectral ρ(A) = {raio_espectral:.6f}")
    print(f"Conclusão: {estabilidade}")
    
    if ponto_fixo is not None:
        print(f"\nPonto fixo encontrado:")
        print(f"  x* = {ponto_fixo[0]:.6f}")
        print(f"  y* = {ponto_fixo[1]:.6f}")
    
    print(f"\nPrimeiras 5 iterações para cada condição inicial:")
    for idx, (x0, y0) in enumerate(condicoes_iniciais):
        print(f"\nCondição inicial {idx+1}: (x₀={x0}, y₀={y0})")
        x_vals, y_vals = sistema.iterar(x0, y0, 5)
        for i in range(6):
            print(f"  n={i}: x_{i} = {x_vals[i]:.4f}, y_{i} = {y_vals[i]:.4f}")
    
    return todas_trajetorias


def criar_analise_interativa():
    """
    Cria uma análise interativa com diferentes cenários de sistema.
    """
    print("ANÁLISE INTERATIVA DE SISTEMAS DINÂMICOS BIDIMENSIONAIS")
    print("="*70)
    
    # Cenário 1: Sistema estável com ponto fixo atrator
    print("\n1. SISTEMA ESTÁVEL (Ponto Fixo Atrator)")
    print("-"*50)
    sistema1 = SistemaDinamicoBidimensional(
        a1=0.5, c=0.3, b1=1,
        a2=0.4, d=0.2, b2=2
    )
    
    condicoes1 = [
        (0, 0),   # Origem
        (10, -5), # Ponto distante
        (-5, 8),  # Outro ponto
        (15, 15)  # Ponto no quadrante positivo
    ]
    
    plot_sistema_completo(sistema1, condicoes1, 
                         titulo="Sistema Estável: Todos os pontos convergem para o ponto fixo")
    
    # Cenário 2: Sistema instável (divergente)
    print("\n\n2. SISTEMA INSTÁVEL (Divergente)")
    print("-"*50)
    sistema2 = SistemaDinamicoBidimensional(
        a1=1.2, c=0.1, b1=0.5,
        a2=0.1, d=1.3, b2=0.5
    )
    
    condicoes2 = [
        (0.5, 0.5),
        (2, 1),
        (-1, -1)
    ]
    
    plot_sistema_completo(sistema2, condicoes2, n_iteracoes=30,
                         titulo="Sistema Instável: Pontos divergem do ponto fixo")
    
    # Cenário 3: Sistema oscilante (autovalores complexos)
    print("\n\n3. SISTEMA OSCILANTE (Autovalores Complexos)")
    print("-"*50)
    sistema3 = SistemaDinamicoBidimensional(
        a1=0.7, c=-0.6, b1=0,
        a2=0.6, d=0.7, b2=0
    )
    
    condicoes3 = [
        (1, 0),
        (3, 2),
        (-2, 1)
    ]
    
    plot_sistema_completo(sistema3, condicoes3, n_iteracoes=100,
                         titulo="Sistema Oscilante: Espirais em torno do ponto fixo")
    
    # Cenário 4: Sistema acoplado forte
    print("\n\n4. SISTEMA FORTEMENTE ACOPLADO")
    print("-"*50)
    sistema4 = SistemaDinamicoBidimensional(
        a1=0.3, c=0.8, b1=0,
        a2=0.8, d=0.3, b2=0
    )
    
    condicoes4 = [
        (5, 0),
        (0, 5),
        (2, 3)
    ]
    
    plot_sistema_completo(sistema4, condicoes4,
                         titulo="Sistema Fortemente Acoplado: Alta interação entre x e y")


# Função para análise personalizada
def analise_personalizada():
    """
    Permite ao usuário definir seus próprios parâmetros.
    """
    print("\nANÁLISE PERSONALIZADA")
    print("="*70)
    
    print("\nDefina os parâmetros do sistema:")
    a1 = float(input("a1 (coeficiente de xₙ na primeira equação): ") or "0.5")
    c = float(input("c (coeficiente de yₙ na primeira equação): ") or "0.3")
    b1 = float(input("b1 (termo constante da primeira equação): ") or "1")
    
    a2 = float(input("\na2 (coeficiente de yₙ na segunda equação): ") or "0.4")
    d = float(input("d (coeficiente de xₙ na segunda equação): ") or "0.2")
    b2 = float(input("b2 (termo constante da segunda equação): ") or "2")
    
    sistema = SistemaDinamicoBidimensional(a1, c, b1, a2, d, b2)
    
    print("\nDefina as condições iniciais (digite 'fim' para terminar):")
    condicoes = []
    i = 1
    while True:
        print(f"\nCondição inicial {i}:")
        entrada = input("Digite x0 y0 (separados por espaço): ")
        if entrada.lower() == 'fim':
            break
        
        try:
            x0, y0 = map(float, entrada.split())
            condicoes.append((x0, y0))
            i += 1
        except:
            print("Entrada inválida. Use o formato: x0 y0")
    
    if not condicoes:
        condicoes = [(0, 0), (5, 5), (-3, 2)]
        print(f"Usando condições iniciais padrão: {condicoes}")
    
    n_iter = int(input("\nNúmero de iterações (padrão 50): ") or "50")
    
    titulo = input("\nTítulo do gráfico (opcional): ") or "Sistema Dinâmico Personalizado"
    
    plot_sistema_completo(sistema, condicoes, n_iter, titulo)


# Executar análise
if __name__ == "__main__":
    print("ANÁLISE DE SISTEMAS DINÂMICOS BIDIMENSIONAIS")
    print("="*70)
    print("Modelo: xₙ₊₁ = a₁·xₙ + c·yₙ + b₁")
    print("        yₙ₊₁ = a₂·yₙ + d·xₙ + b₂")
    print("="*70)
    
    print("\nOpções:")
    print("1. Executar análise interativa com exemplos pré-definidos")
    print("2. Definir parâmetros personalizados")
    print("3. Usar exemplo rápido")
    
    opcao = input("\nEscolha uma opção (1, 2 ou 3): ") or "3"
    
    if opcao == "1":
        criar_analise_interativa()
    elif opcao == "2":
        analise_personalizada()
    else:
        # Exemplo rápido
        print("\nExecutando exemplo rápido...")
        sistema_exemplo = SistemaDinamicoBidimensional(
            a1=0.6, c=0.4, b1=1,
            a2=0.3, d=0.7, b2=2
        )
        
        condicoes_exemplo = [
            (0, 0),
            (10, -5),
            (-3, 7),
            (8, 8)
        ]
        
        trajetorias = plot_sistema_completo(
            sistema_exemplo, 
            condicoes_exemplo,
            titulo="Exemplo Rápido: Sistema Dinâmico Bidimensional"
        )
        
        # Análise adicional: mapa de calor da convergência
        fig, ax = plt.subplots(figsize=(10, 8))
        
        # Criar grid de condições iniciais
        x_grid = np.linspace(-10, 10, 20)
        y_grid = np.linspace(-10, 10, 20)
        X, Y = np.meshgrid(x_grid, y_grid)
        
        # Calcular velocidade de convergência para cada ponto
        Z = np.zeros_like(X)
        for i in range(X.shape[0]):
            for j in range(X.shape[1]):
                x_vals, y_vals = sistema_exemplo.iterar(X[i, j], Y[i, j], 20)
                # Distância final ao ponto fixo
                pf, _ = sistema_exemplo.ponto_fixo()
                if pf is not None:
                    dist_final = np.sqrt((x_vals[-1] - pf[0])**2 + (y_vals[-1] - pf[1])**2)
                    Z[i, j] = dist_final
        
        # Plotar mapa de calor
        contour = ax.contourf(X, Y, Z, levels=20, cmap='RdYlBu_r', alpha=0.7)
        plt.colorbar(contour, ax=ax, label='Distância ao ponto fixo após 20 iterações')
        
        # Adicionar algumas trajetórias
        cores = ['red', 'blue', 'green', 'purple']
        for idx, (x_vals, y_vals) in enumerate(trajetorias[:4]):
            ax.plot(x_vals, y_vals, color=cores[idx], linewidth=2, alpha=0.8)
            ax.scatter(x_vals[0], y_vals[0], color=cores[idx], s=100, 
                      edgecolor='black', zorder=5)
        
        # Marcar ponto fixo
        pf, _ = sistema_exemplo.ponto_fixo()
        if pf is not None:
            ax.scatter(pf[0], pf[1], color='black', s=200, marker='X', 
                      label='Ponto Fixo', zorder=6)
        
        ax.set_xlabel('x₀', fontsize=12)
        ax.set_ylabel('y₀', fontsize=12)
        ax.set_title('Mapa de Convergência', fontsize=14, fontweight='bold')
        ax.grid(True, alpha=0.3)
        ax.axhline(0, color='black', linewidth=0.5, alpha=0.5)
        ax.axvline(0, color='black', linewidth=0.5, alpha=0.5)
        ax.legend()
        
        plt.tight_layout()
        plt.show()
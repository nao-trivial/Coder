import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def koch_segment(p1, p2, level):
    """Gera pontos do fractal de Koch recursivamente"""
    if level == 0:
        return [p1, p2]
    
    # Divide o segmento em 4 partes
    x1, y1 = p1
    x2, y2 = p2
    
    # Pontos de divisão
    dx = (x2 - x1) / 3
    dy = (y2 - y1) / 3
    
    a = (x1, y1)
    b = (x1 + dx, y1 + dy)
    c = (x1 + 1.5*dx - np.sqrt(3)/2*dy, y1 + 1.5*dy + np.sqrt(3)/2*dx)
    d = (x1 + 2*dx, y1 + 2*dy)
    e = (x2, y2)
    
    # Recursão
    pontos = []
    pontos.extend(koch_segment(a, b, level-1))
    pontos.extend(koch_segment(b, c, level-1)[1:])
    pontos.extend(koch_segment(c, d, level-1)[1:])
    pontos.extend(koch_segment(d, e, level-1)[1:])
    
    return pontos

def update(frame):
    """Atualiza a animação para cada frame"""
    ax.clear()
    
    # Configurações do gráfico
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_xlim(-0.1, 1.1)
    ax.set_ylim(-0.2, 0.6)
    ax.set_title(f'Fractal de Koch - Iteração {frame}')
    
    # Pontos iniciais (triângulo equilátero)
    vertices = [
        (0, 0),
        (0.5, np.sqrt(3)/2),
        (1, 0),
        (0, 0)
    ]
    
    # Desenha o fractal
    for i in range(len(vertices)-1):
        pontos = koch_segment(vertices[i], vertices[i+1], frame)
        x = [p[0] for p in pontos]
        y = [p[1] for p in pontos]
        ax.plot(x, y, 'b-', linewidth=1)

# Configuração da figura
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_aspect('equal')
ax.axis('off')

# Cria a animação
num_iteracoes = 5  # Número máximo de iterações
ani = FuncAnimation(fig, update, frames=num_iteracoes+1, 
                    interval=1000, repeat=True)

# Para salvar a animação (descomente se quiser)
# ani.save('koch_fractal.gif', writer='pillow', fps=1)

plt.show()

# Versão alternativa mais simples (apenas último estágio)
print("\nCódigo alternativo para visualizar apenas o fractal completo:")
print("""
import numpy as np
import matplotlib.pyplot as plt

def koch_curve(level):
    # Pontos iniciais
    pontos = [(0, 0), (1, 0)]
    
    for _ in range(level):
        novos_pontos = []
        for i in range(len(pontos)-1):
            x1, y1 = pontos[i]
            x2, y2 = pontos[i+1]
            
            dx = (x2 - x1) / 3
            dy = (y2 - y1) / 3
            
            novos_pontos.append((x1, y1))
            novos_pontos.append((x1 + dx, y1 + dy))
            novos_pontos.append((x1 + 1.5*dx - np.sqrt(3)/2*dy, 
                                 y1 + 1.5*dy + np.sqrt(3)/2*dx))
            novos_pontos.append((x1 + 2*dx, y1 + 2*dy))
        
        novos_pontos.append(pontos[-1])
        pontos = novos_pontos
    
    return pontos

# Plot do fractal completo
nivel = 5
pontos = koch_curve(nivel)
x = [p[0] for p in pontos]
y = [p[1] for p in pontos]

plt.figure(figsize=(10, 4))
plt.plot(x, y, 'b-', linewidth=0.5)
plt.axis('equal')
plt.axis('off')
plt.title(f'Fractal de Koch - Nível {nivel}')
plt.show()
""")
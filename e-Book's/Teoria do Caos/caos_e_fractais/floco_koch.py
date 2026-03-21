
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
nivel = 7
pontos = koch_curve(nivel)
x = [p[0] for p in pontos]
y = [p[1] for p in pontos]

plt.figure(figsize=(10, 4))
plt.plot(x, y, 'b-', linewidth=0.5)
plt.axis('equal')
plt.axis('off')
plt.title(f'Fractal de Koch - Nível {nivel}')
plt.show()
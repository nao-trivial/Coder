import matplotlib.pyplot as plt
import numpy as np

class TeiaAranha:
    """Cria o diagrama de teia de aranha para um mapa logístico."""
    
    def __init__(self, mapa, x0, iteracoes=50):
        self.mapa = mapa
        self.x0 = x0
        self.iteracoes = iteracoes
    
    def gerar_trajetoria(self):
        """Gera os pontos (x, f(x)) para desenhar a teia."""
        x_atual = self.x0
        traj_x = [x_atual]
        traj_y = [0]
        
        for _ in range(self.iteracoes):
            # Vertical
            traj_x.append(x_atual)
            traj_y.append(self.mapa.iterar(x_atual))
            # Horizontal
            traj_y.append(traj_y[-1])
            traj_x.append(traj_y[-1])
            x_atual = traj_y[-1]
        
        return traj_x, traj_y
    
    def plotar(self, ciclo=None, titulo=None):
        """Plota a teia, a curva e a reta y=x. Se ciclo for dado, destaca os pontos."""
        fig, ax = plt.subplots(figsize=(8, 6))
        
        # Curva do mapa
        x_vals = np.linspace(0, 1, 200)
        y_vals = [self.mapa.iterar(x) for x in x_vals]
        ax.plot(x_vals, y_vals, 'b-', lw=2, label='f(x)')
        ax.plot(x_vals, x_vals, 'k--', lw=1, label='y = x')
        
        # Trajetória da teia
        tx, ty = self.gerar_trajetoria()
        ax.plot(tx, ty, 'r-', alpha=0.7, lw=1, label='Trajetória')
        
        # Pontos do ciclo (se fornecidos)
        if ciclo:
            for ponto in ciclo:
                ax.plot(ponto, ponto, 'ro', markersize=8, label=f'x = {ponto:.3f}')
        
        ax.set_xlabel('xₙ')
        ax.set_ylabel('xₙ₊₁')
        titulo = titulo or f'Teia de Aranha - r = {self.mapa.r:.2f}'
        ax.set_title(titulo)
        ax.grid(True, alpha=0.3)
        ax.legend()
        plt.show()
class MapaLogistico:
    """Representa o mapa logístico x_{n+1} = r * x_n * (1 - x_n)."""
    
    def __init__(self, r):
        self.r = r
    
    def iterar(self, x):
        """Aplica o mapa uma vez."""
        return self.r * x * (1 - x)
    
    def orbita(self, x0, n):
        """Gera uma órbita de n passos a partir de x0."""
        orb = [x0]
        for _ in range(n):
            orb.append(self.iterar(orb[-1]))
        return orb
    
    def derivada(self, x):
        """Derivada do mapa: r * (1 - 2x)."""
        return self.r * (1 - 2 * x)
    
    def derivada_ciclo(self, ciclo):
        """Produto das derivadas nos pontos do ciclo."""
        prod = 1
        for x in ciclo:
            prod *= self.derivada(x)
        return prod
    
    def estabilidade_ciclo(self, ciclo):
        """Retorna (derivada, estável?) para um ciclo."""
        d = self.derivada_ciclo(ciclo)
        return d, abs(d) < 1
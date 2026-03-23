"""
Módulo que implementa o mapa logístico e análises de estabilidade.
"""
class MapaLogistico:
    """
    Representa o mapa logístico: x_{n+1} = r * x_n * (1 - x_n).

    Atributos:
        r (float): parâmetro de controle (entre 0 e 4).
    """
    def __init__(self, r: float):
        """
        Inicializa o mapa com um valor de r.

        Args:
            r: parâmetro do mapa logístico (0 ≤ r ≤ 4).
        """
        self.r = r

    def iterar(self, x: float) -> float:
        """Aplica o mapa uma vez."""
        return self.r * x * (1 - x)

    def derivada(self, x: float) -> float:
        """Calcula a derivada f'(x) = r * (1 - 2x)."""
        return self.r * (1 - 2 * x)

    def derivada_ciclo(self, ciclo: list) -> float:
        """
        Produto das derivadas nos pontos do ciclo.

        Args:
            ciclo: lista de pontos (x) que formam um ciclo.

        Returns:
            Produto das derivadas.
        """
        produto = 1.0
        for x in ciclo:
            produto *= self.derivada(x)
        return produto

    def estabilidade_ciclo(self, ciclo: list) -> tuple:
        """
        Retorna a derivada do ciclo e um booleano indicando estabilidade.

        Returns:
            (derivada, estável)
        """
        d = self.derivada_ciclo(ciclo)
        return d, abs(d) < 1
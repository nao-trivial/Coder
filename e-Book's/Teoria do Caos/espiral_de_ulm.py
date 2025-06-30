import numpy as np
import matplotlib.pyplot as plt

# Função para gerar a espiral
def ulm_spiral(n_lines, step_angle, radius_step):
    theta = 0  # Ângulo inicial
    r = 0      # Raio inicial
    x, y = [0], [0]  # Coordenadas iniciais

    for i in range(n_lines):
        # Calcular as coordenadas polares
        r += radius_step
        theta += step_angle

        # Converter para coordenadas cartesianas
        x_new = r * np.cos(theta)
        y_new = r * np.sin(theta)

        x.append(x_new)
        y.append(y_new)

    return x, y

# Parâmetros para a espiral
n_lines = 500  # Número de linhas da espiral
step_angle = np.pi / 12  # Ângulo de rotação em radianos
radius_step = 0.5  # Aumento do raio por iteração

# Gerar as coordenadas da espiral
x, y = ulm_spiral(n_lines, step_angle, radius_step)

# Plotar a espiral
plt.figure(figsize=(8, 8))
plt.plot(x, y, linewidth=2, color="black")
plt.axis('equal')  # Manter a proporção dos eixos
plt.axis('off')    # Remover os eixos
plt.title('Espiral de Ulm')
plt.show()
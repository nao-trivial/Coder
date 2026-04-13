import numpy as np
import matplotlib.pyplot as plt

def lyapunov_logistic(r, N=1000, transiente=200):
    x = 0.5  # condição inicial arbitrária
    soma = 0.0
    for i in range(transiente + N):
        x = r * x * (1 - x)
        if i >= transiente:
            derivada = r * (1 - 2*x)
            soma += np.log(abs(derivada))
    return soma / N

# Vamos calcular para vários valores de r
r_values = np.linspace(2.5, 4.0, 500)
lyap = [lyapunov_logistic(r) for r in r_values]

plt.figure(figsize=(10, 5))
plt.plot(r_values, lyap, 'b-', linewidth=1)
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel('r')
plt.ylabel('Expoente de Lyapunov')
plt.title('Expoente de Lyapunov para a Equação Logística')
plt.grid(alpha=0.3)
plt.show()

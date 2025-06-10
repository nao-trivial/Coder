def collatz(n):
    sequencia = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequencia.append(n)
    return sequencia

# Testando com diferentes valores
numero = 13  # Pode alterar para qualquer número positivo
seq = collatz(numero)

# Resultado
print(f"Sequência de Collatz para {numero}:")
print(seq)

# Plotagem (opcional)
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 5))
plt.plot(seq, 'r-o')
plt.xlabel('Passo')
plt.ylabel('Valor')
plt.title(f'Sequência de Collatz para {numero}')
plt.grid(True)
plt.savefig(f'collatz_{numero}.png')
plt.show()
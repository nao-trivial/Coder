# Simulação emocional
def simular_relacionamento(x0, a, b, dias=20):
    trajetoria = [x0]
    x = x0
    for _ in range(dias):
        x = a * x + b
        trajetoria.append(x)
    return trajetoria

# Teste: relacionamento estável
trajetoria = simular_relacionamento(x0=10, a=0.8, b=2, dias=15)
print(trajetoria)
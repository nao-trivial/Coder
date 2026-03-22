def analisar_ponto_fixo(a, b, x0, iteracoes=10):
    resultados = [x0]
    for _ in range(iteracoes):
        xn = a * resultados[-1] + b
        resultados.append(xn)
    return resultados

# Exemplo de uso:
a_valor = 0.9
b_valor = 50
x_inicial = 100
iteracoes = 20

resultado = analisar_ponto_fixo(a_valor, b_valor, x_inicial, iteracoes)

print(f"Evolução do sistema com A={a_valor}, B={b_valor}:")
for i, val in enumerate(resultado):
    print(f"Iteração {i}: {val:.4f}")
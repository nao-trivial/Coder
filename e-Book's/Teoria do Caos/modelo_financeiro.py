# Parâmetros do modelo
saldo_inicial = 1000  # Valor inicial em reais
meses = 20            # Número de meses para simular
historico = [saldo_inicial]  # Lista para guardar o histórico

# Simulação do investimento
saldo = saldo_inicial
for mes in range(meses):
    saldo = 0.7 * saldo + 50  # Perde 30% e recebe R$ 50 de aporte
    historico.append(saldo)

# Resultado final
print(f"EVOLUÇÃO DO SALDO:")
for mes, valor in enumerate(historico):
    print(f"Mês {mes}: R$ {valor:.2f}")

print(f"\nSaldo final após {meses} meses: R$ {historico[-1]:.2f}")

# Plotando a evolução (opcional)
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 5))
plt.plot(range(meses + 1), historico, 'b-o')
plt.xlabel('Mês')
plt.ylabel('Saldo (R$)')
plt.title('Evolução do Investimento com Perda e Aporte Fixo')
plt.grid(True)
plt.savefig('evolucao_financeira.png')  # Salva o gráfico
plt.show()
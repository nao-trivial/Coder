import math

def exibir_tabela_congestionamento():
    print("\n TABELA DE REFERÊNCIA – Fator de Congestionamento")
    print("---------------------------------------------")
    print("|  Fator  | Situação típica                  |")
    print("|---------|----------------------------------|")
    print("|   1.0   | Trânsito livre                   |")
    print("|   1.3   | Trânsito leve, com poucos sinais|")
    print("|   1.5   | Fluxo urbano moderado           |")
    print("|   1.8   | Trânsito intenso (horário pico) |")
    print("|   2.2   | Altamente congestionado          |")
    print("|   2.8+  | Engarrafamento severo            |")
    print("---------------------------------------------")
    print("Dica: Use um valor coerente com a sua experiência diária.\n")


def calcular_risco_de_atraso():
    print("Calculadora de Risco de Atraso (Baseada na Teoria do Caos)")
    exibir_tabela_congestionamento()

    # Entrada do usuário
    try:
        n_paradas = int(input("Nº de pontos de parada: "))
        tempo_por_parada = float(input("Tempo médio por parada (em segundos): "))
        fator_congestionamento = float(input("Fator de congestionamento (ex: 1.8): "))
        atraso_inicial = float(input("Atraso inicial (em minutos): "))
    except ValueError:
        print("Entrada inválida! Tente novamente com números válidos.")
        return

    # Cálculos
    risco_base = (n_paradas * tempo_por_parada * fator_congestionamento) / 60  # em minutos
    efeito_borboleta = atraso_inicial * math.exp(fator_congestionamento)  # amplificação exponencial
    risco_total = min(risco_base + efeito_borboleta, 120)  # cap em 120 min

    # Classificação do risco
    if risco_total < 15:
        nivel_risco = "BAIXO"
    elif risco_total < 30:
        nivel_risco = "MÉDIO"
    else:
        nivel_risco = "ALTO"

    # Resultados
    print("\n--- RESULTADOS ---")
    print(f"Risco Base: {risco_base:.2f} min")
    print(f"Efeito Borboleta: {efeito_borboleta:.2f} min")
    print(f"Risco Total Estimado: {risco_total:.2f} min")
    print(f"Nível de Risco: {nivel_risco}")
    print(f"Tempo Estimado: {int(risco_total)} min")

if __name__ == "__main__":
    calcular_risco_de_atraso()
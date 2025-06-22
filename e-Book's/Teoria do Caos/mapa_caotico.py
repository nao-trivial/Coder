import random
import time

# Listas de opções personalizáveis
disciplinas = ["Biologia", "Química", "Física", "Matemática", "Redação"]
tecnicas = ["Pomodoro", "Mapa mental", "Flashcards", "Ensinar alguém", "Estudo em pé", "Estudo com aroma de lavanda"]
perturbacoes = ["Simulado surpresa", "Estudo na varanda", "Estudo com som de floresta", "Estudo em dupla", "Estudar debaixo de uma árvore"]
recompensas = ["1h de Netflix", "1 fruta do pomar", "Caminhada ao pôr do sol", "10 minutos de dança livre", "Ver um vídeo divertido"]

# Histórico de sucesso para recompensas escaláveis
gene_resistencia = 0

def sortear_tarefa():
    foco = random.choice(disciplinas)
    print(f"\n🌱 Disciplina sorteada como atrator do dia: **{foco}**")

    tecnica1, tecnica2 = random.sample(tecnicas, 2)
    print(f"🔁 Técnicas sorteadas (mutação): {tecnica1} + {tecnica2}")

    print(f"\n🔀 Regra: Você só pode estudar {foco} se revisar pelo menos uma base (ex: Biologia ou Química).")

def perturbar_rotina():
    evento = random.choice(perturbacoes)
    print(f"\n🔥 Perturbação do dia (caos criativo): {evento}")

def recompensa():
    global gene_resistencia
    print("\n🧪 Meta atingida? [s/n]")
    resposta = input("→ ").lower()

    if resposta == 's':
        gene_resistencia += 1
        premio = random.choice(recompensas)
        print(f"\n🎁 Recompensa ativada (gene #{gene_resistencia}): {premio}")

        if gene_resistencia % 5 == 0:
            print("🌊 Recompensa MAIOR desbloqueada: Dia livre! Vá à praia, museu ou natureza 🌴")
    else:
        gene_resistencia = max(0, gene_resistencia - 1)
        print("💤 Tudo bem. Recomece amanhã com mais força.")

def menu():
    while True:
        print("\n=== 🌪️ M.A.P.A. — Sistema Caótico Controlado ===")
        print("1. Sortear Tarefa + Técnicas")
        print("2. Aplicar Perturbação Criativa")
        print("3. Verificar Recompensa")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            sortear_tarefa()
        elif opcao == '2':
            perturbar_rotina()
        elif opcao == '3':
            recompensa()
        elif opcao == '4':
            print("Encerrando sistema... Até logo, mutante caótico!")
            break
        else:
            print("Opção inválida.")

# Executar app
menu()
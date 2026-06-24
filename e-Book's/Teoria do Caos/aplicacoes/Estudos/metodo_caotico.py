import random
import sqlite3
import os
from datetime import datetime, timedelta

# Conexão com o mesmo banco do CRM
DB_NAME = "crm_nao_trivial.db"

# ========== PARÂMETROS PERSONALIZÁVEIS ==========
disciplinas = ["Biologia", "Química", "Física", "Matemática", "Redação"]
tecnicas = ["Pomodoro", "Mapa mental", "Flashcards", "Ensinar alguém", "Estudo em pé", "Estudo com aroma de lavanda"]
perturbacoes = ["Simulado surpresa", "Estudo na varanda", "Estudo com som de floresta", "Estudo em dupla", "Estudar debaixo de uma árvore"]
recompensas = ["1h de Netflix", "1 fruta do pomar", "Caminhada ao pôr do sol", "10 minutos de dança livre", "Ver um vídeo divertido"]

# ========== INICIALIZAÇÃO DO BANCO (TABELA DE SESSÕES) ==========
def init_mapa_db():
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS sessoes_estudo (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data TEXT NOT NULL,
                disciplina TEXT,
                tecnicas TEXT,
                perturbacao TEXT,
                meta_atingida INTEGER DEFAULT 0,
                recompensa TEXT,
                gene_resistencia INTEGER DEFAULT 0
            )
        ''')
        conn.commit()

# ========== FUNÇÕES PRINCIPAIS (COM PERSISTÊNCIA) ==========
gene_resistencia = 0  # mantido em memória, mas também salvo na sessão

def sortear_tarefa():
    global gene_resistencia
    foco = random.choice(disciplinas)
    print(f"\n🌱 Disciplina sorteada como atrator do dia: **{foco}**")

    tecnica1, tecnica2 = random.sample(tecnicas, 2)
    print(f"🔁 Técnicas sorteadas (mutação): {tecnica1} + {tecnica2}")

    print(f"\n🔀 Regra: Você só pode estudar {foco} se revisar pelo menos uma base (ex: Biologia ou Química).")

    # Salva a sessão atual (ainda sem resultado)
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute('''
            INSERT INTO sessoes_estudo (data, disciplina, tecnicas, perturbacao, gene_resistencia)
            VALUES (?, ?, ?, ?, ?)
        ''', (datetime.today().strftime("%Y-%m-%d %H:%M"), foco, f"{tecnica1} + {tecnica2}", None, gene_resistencia))
        conn.commit()
        print("📝 Sessão registrada no CRM (pendente de resultado).")

def perturbar_rotina():
    global gene_resistencia
    evento = random.choice(perturbacoes)
    print(f"\n🔥 Perturbação do dia (caos criativo): {evento}")

    # Atualiza a última sessão do dia com a perturbação
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        hoje = datetime.today().strftime("%Y-%m-%d")
        c.execute('''
            UPDATE sessoes_estudo 
            SET perturbacao = ? 
            WHERE id = (SELECT MAX(id) FROM sessoes_estudo WHERE data LIKE ?)
        ''', (evento, f"{hoje}%"))
        conn.commit()
        print("🌀 Perturbação anotada na sessão de hoje.")

def recompensa():
    global gene_resistencia
    print("\n🧪 Meta atingida? [s/n]")
    resposta = input("→ ").lower()

    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        hoje = datetime.today().strftime("%Y-%m-%d")

        if resposta == 's':
            gene_resistencia += 1
            premio = random.choice(recompensas)
            print(f"\n🎁 Recompensa ativada (gene #{gene_resistencia}): {premio}")

            if gene_resistencia % 5 == 0:
                print("🌊 Recompensa MAIOR desbloqueada: Dia livre! Vá à praia, museu ou natureza 🌴")
                # Dica de conteúdo: sugerir e-book
                print("📘 Dica: consulte o E-book 1 para entender como pequenas iterações levam a grandes mudanças!")

            # Atualiza a última sessão do dia com sucesso
            c.execute('''
                UPDATE sessoes_estudo 
                SET meta_atingida = 1, recompensa = ?, gene_resistencia = ?
                WHERE id = (SELECT MAX(id) FROM sessoes_estudo WHERE data LIKE ?)
            ''', (premio, gene_resistencia, f"{hoje}%"))
            conn.commit()
            print("✅ Meta registrada.")

        else:
            gene_resistencia = max(0, gene_resistencia - 1)
            print("💤 Tudo bem. Recomece amanhã com mais força.")
            c.execute('''
                UPDATE sessoes_estudo 
                SET meta_atingida = 0, gene_resistencia = ?
                WHERE id = (SELECT MAX(id) FROM sessoes_estudo WHERE data LIKE ?)
            ''', (gene_resistencia, f"{hoje}%"))
            conn.commit()

def mostrar_historico():
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute('''
            SELECT data, disciplina, tecnicas, perturbacao, meta_atingida, recompensa, gene_resistencia
            FROM sessoes_estudo
            ORDER BY data DESC
            LIMIT 10
        ''')
        rows = c.fetchall()
    if not rows:
        print("Nenhuma sessão registrada ainda.")
        return
    print("\n📜 ÚLTIMAS 10 SESSÕES:")
    for r in rows:
        status = "🏆" if r[4] else "⏳"
        print(f"{r[0][:16]} | {r[1]:10} | {r[2]:25} | Pert: {r[3] or '-':20} | {status} | Gene: {r[6]}")

def relatorio_mensal():
    """Gera um resumo que pode ser usado como post (printa no terminal)."""
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        mes_atual = datetime.today().strftime("%Y-%m")
        c.execute('''
            SELECT COUNT(*), SUM(meta_atingida)
            FROM sessoes_estudo
            WHERE data LIKE ?
        ''', (f"{mes_atual}%",))
        total, metas = c.fetchone()
        if total == 0:
            print("Nenhuma sessão este mês.")
            return
        pct = (metas / total * 100) if total else 0
        # Disciplina mais estudada
        c.execute('''
            SELECT disciplina, COUNT(*) as cnt
            FROM sessoes_estudo
            WHERE data LIKE ?
            GROUP BY disciplina
            ORDER BY cnt DESC
            LIMIT 1
        ''', (f"{mes_atual}%",))
        top_disc = c.fetchone()
        nome_disc = top_disc[0] if top_disc else "Nenhuma"

    print(f"\n📊 RELATÓRIO DE {mes_atual}")
    print(f"Sessões: {total} | Metas batidas: {metas} ({pct:.0f}%)")
    print(f"Disciplina foco: {nome_disc}")
    print(f"Gene de resistência atual: {gene_resistencia}")
    print("\n💡 Use esse resumo para criar um post motivacional no Instagram/LinkedIn!")

# ========== MENU PRINCIPAL (MANTENDO A ESSÊNCIA) ==========
def menu():
    init_mapa_db()
    global gene_resistencia
    # Recupera o último gene_resistencia do banco
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute("SELECT gene_resistencia FROM sessoes_estudo ORDER BY id DESC LIMIT 1")
        row = c.fetchone()
        if row:
            gene_resistencia = row[0]
        else:
            gene_resistencia = 0

    while True:
        print("\n=== 🌪️ M.A.P.A. — Sistema Caótico Controlado (v.2.0) ===")
        print("1. Sortear Tarefa + Técnicas")
        print("2. Aplicar Perturbação Criativa")
        print("3. Verificar Recompensa")
        print("4. Mostrar Histórico")
        print("5. Relatório Mensal (pauta para redes)")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            sortear_tarefa()
        elif opcao == '2':
            perturbar_rotina()
        elif opcao == '3':
            recompensa()
        elif opcao == '4':
            mostrar_historico()
        elif opcao == '5':
            relatorio_mensal()
        elif opcao == '6':
            print("Encerrando sistema... Até logo, mutante caótico!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import warnings
warnings.filterwarnings('ignore')

class RelacionamentoLinear:
    """
    Modelo de dinâmica de relacionamento baseado em iteração linear.
    
    Equação: R_n = a * R_{n-1} + b
    
    Onde:
    - R_n: Estado do relacionamento no mês n
    - a: Coeficiente emocional (múltiplo emocional)
    - b: Força externa (fatores externos ao casal)
    """
    
    def __init__(self):
        """Inicializa o modelo de relacionamento."""
        self.historico = []
        self.meses = []
        self.a = 0.0  # Coeficiente emocional
        self.b = 0.0  # Força externa
        self.R0 = 0.0  # Estado inicial do relacionamento
        
    def questionario_coeficiente_a(self):
        """
        Questionário para determinar o coeficiente emocional 'a'.
        
        O coeficiente 'a' representa:
        - a = 0: Desinteresse total (relacionamento não evolui, apenas responde a fatores externos)
        - 0 < |a| < 1: Estabilidade emocional (sentimentos moderados)
        - |a| = 1: Sensibilidade emocional equilibrada
        - |a| > 1: Sensibilidade emocional intensa (pode levar a colapso ou crescimento explosivo)
        - a < 0: Padrão emocional negativo (ciclos de reação inversa)
        """
        print("=" * 60)
        print("QUESTIONÁRIO - COEFICIENTE EMOCIONAL (a)")
        print("=" * 60)
        print("\nResponda com valores de 0 a 10, onde:")
        print("0 = Nunca / Nada")
        print("5 = Às vezes / Moderado")
        print("10 = Sempre / Totalmente")
        
        perguntas_a = [
            ("Quando seu parceiro está feliz, isso te afeta positivamente?", 1.0),
            ("Quando há um desentendimento, vocês conseguem resolver rapidamente?", 0.8),
            ("Você sente que o interesse mútuo permanece constante?", 0.9),
            ("As emoções positivas de um influenciam as do outro?", 1.0),
            ("Há reciprocidade nas demonstrações de afeto?", 0.9),
            ("Vocês conseguem perdoar falhas e seguir em frente?", 0.7),
            ("Existe empatia nas situações difíceis?", 0.8),
            ("O humor de um afeta o do outro?", 1.2),  # Maior peso - emocionalmente carregado
        ]
        
        soma_ponderada = 0
        soma_pesos = 0
        
        for pergunta, peso in perguntas_a:
            while True:
                try:
                    resposta = float(input(f"\n{pergunta}\nResposta (0-10): "))
                    if 0 <= resposta <= 10:
                        # Normaliza para escala -1 a 1
                        normalizado = (resposta - 5) / 5
                        soma_ponderada += normalizado * peso
                        soma_pesos += peso
                        break
                    else:
                        print("Por favor, digite um valor entre 0 e 10.")
                except ValueError:
                    print("Entrada inválida. Digite um número.")
        
        # Calcula 'a' baseado nas respostas
        self.a = soma_ponderada / soma_pesos if soma_pesos > 0 else 0
        
        print(f"\nCoeficiente emocional (a) calculado: {self.a:.3f}")
        self.interpretar_coeficiente_a()
        
        return self.a
    
    def questionario_coeficiente_b(self):
        """
        Questionário para determinar a força externa 'b'.
        
        O coeficiente 'b' representa:
        - b > 0: Fatores externos positivos (apoio familiar, amigos, estabilidade financeira)
        - b < 0: Fatores externos negativos (estresse no trabalho, interferência familiar, problemas financeiros)
        - b = 0: Fatores externos neutros
        """
        print("\n" + "=" * 60)
        print("QUESTIONÁRIO - FORÇA EXTERNA (b)")
        print("=" * 60)
        print("\nResponda com valores de -5 a +5, onde:")
        print("-5 = Muito negativo / Prejudica muito")
        print(" 0 = Neutro / Não afeta")
        print("+5 = Muito positivo / Ajuda muito")
        
        perguntas_b = [
            ("O apoio de familiares e amigos:", 1.0),
            ("A situação financeira do casal:", 1.2),
            ("O estresse relacionado ao trabalho:", 1.0),
            ("Atividades e hobbies compartilhados:", 0.8),
            ("Interferência de terceiros no relacionamento:", 1.0),
            ("Suporte emocional externo (terapia, aconselhamento):", 0.7),
            ("Pressões sociais e culturais:", 0.9),
            ("Qualidade do tempo a sós:", 1.1),
        ]
        
        soma_ponderada = 0
        soma_pesos = 0
        
        for pergunta, peso in perguntas_b:
            while True:
                try:
                    resposta = float(input(f"\n{pergunta}\nResposta (-5 a +5): "))
                    if -5 <= resposta <= 5:
                        # Normaliza para escala -1 a 1
                        normalizado = resposta / 5
                        soma_ponderada += normalizado * peso
                        soma_pesos += peso
                        break
                    else:
                        print("Por favor, digite um valor entre -5 e +5.")
                except ValueError:
                    print("Entrada inválida. Digite um número.")
        
        # Calcula 'b' baseado nas respostas
        self.b = soma_ponderada / soma_pesos if soma_pesos > 0 else 0
        
        print(f"\nForça externa (b) calculada: {self.b:.3f}")
        self.interpretar_coeficiente_b()
        
        return self.b
    
    def interpretar_coeficiente_a(self):
        """Interpreta o significado do coeficiente emocional 'a'."""
        print("\n" + "-" * 40)
        print("INTERPRETAÇÃO DO COEFICIENTE EMOCIONAL (a)")
        print("-" * 40)
        
        if self.a == 0:
            print("⚠️  a = 0: DESINTERESSE")
            print("   O relacionamento não tem memória emocional.")
            print("   Cada mês começa do zero, sem conexão com o passado.")
            print("   Risco: Fracasso por falta de continuidade emocional.")
            
        elif abs(self.a) < 0.3:
            print("📉 |a| < 0.3: BAIXA CONEXÃO EMOCIONAL")
            print("   As emoções têm pouco impacto no relacionamento.")
            print("   Pouca memória emocional entre os meses.")
            
        elif 0.3 <= abs(self.a) < 0.7:
            print("📊 0.3 ≤ |a| < 0.7: CONEXÃO EMOCIONAL MODERADA")
            print("   Emoções moderadas, com alguma continuidade.")
            print("   Relacionamento estável, com memória emocional controlada.")
            
        elif 0.7 <= abs(self.a) < 1.0:
            print("📈 0.7 ≤ |a| < 1.0: ALTA CONEXÃO EMOCIONAL")
            print("   Forte memória emocional entre os meses.")
            print("   Emoções passadas influenciam significativamente o presente.")
            
        elif abs(self.a) == 1.0:
            print("⚖️  |a| = 1.0: EQUILÍBRIO EMOCIONAL CRÍTICO")
            print("   Total memória emocional sem amortecimento.")
            print("   O relacionamento pode crescer ou decair linearmente.")
            
        elif 1.0 < abs(self.a) < 1.5:
            print("⚠️  1.0 < |a| < 1.5: AMPLIFICAÇÃO EMOCIONAL")
            print("   Emoções se intensificam com o tempo.")
            print("   Risco de ciclos de retroalimentação emocional.")
            
        elif abs(self.a) >= 1.5:
            print("🚨 |a| ≥ 1.5: RISCO DE COLAPSO EMOCIONAL")
            print("   Emoções se amplificam rapidamente.")
            print("   Relacionamento pode se tornar instável e imprevisível.")
            print("   Alto risco de colapso emocional.")
        
        if self.a < 0:
            print("\n🔁 a NEGATIVO: PADRÃO DE REAÇÃO INVERSA")
            print("   Emoções positivas de um podem gerar respostas negativas.")
            print("   Padrão emocional oscilante e potencialmente destrutivo.")
    
    def interpretar_coeficiente_b(self):
        """Interpreta o significado da força externa 'b'."""
        print("\n" + "-" * 40)
        print("INTERPRETAÇÃO DA FORÇA EXTERNA (b)")
        print("-" * 40)
        
        if self.b > 0.5:
            print("✅ b > 0.5: FORTALE EXTERNA MUITO POSITIVA")
            print("   Fatores externos fortalecem significativamente o relacionamento.")
            print("   Bom suporte familiar, financeiro e social.")
            
        elif 0 < self.b <= 0.5:
            print("👍 0 < b ≤ 0.5: FORÇA EXTERNA POSITIVA")
            print("   Fatores externos contribuem positivamente.")
            print("   Ambiente favorável ao relacionamento.")
            
        elif self.b == 0:
            print("➖ b = 0: FORÇAS EXTERNAS NEUTRAS")
            print("   Fatores externos não impactam significativamente.")
            print("   Relacionamento depende principalmente dos fatores internos.")
            
        elif -0.5 <= self.b < 0:
            print("👎 -0.5 ≤ b < 0: FORÇA EXTERNA NEGATIVA")
            print("   Fatores externos prejudicam o relacionamento.")
            print("   Possíveis fontes de estresse externo.")
            
        elif self.b < -0.5:
            print("❌ b < -0.5: FORÇA EXTERNA MUITO NEGATIVA")
            print("   Fatores externos prejudicam gravemente o relacionamento.")
            print("   Alto estresse externo, possivelmente insustentável.")
    
    def simular_meses(self, num_meses=12, estado_inicial=None):
        """
        Simula a evolução do relacionamento ao longo dos meses.
        
        Args:
            num_meses: Número de meses para simular
            estado_inicial: Estado inicial do relacionamento (padrão: neutro)
        """
        if estado_inicial is not None:
            self.R0 = estado_inicial
        
        # Reinicia o histórico
        self.historico = [self.R0]
        self.meses = list(range(num_meses + 1))
        
        # Aplica a iteração linear
        for mes in range(1, num_meses + 1):
            R_n = self.a * self.historico[-1] + self.b
            self.historico.append(R_n)
        
        return self.historico
    
    def analisar_tendencia(self):
        """Analisa a tendência do relacionamento com base na simulação."""
        if not self.historico:
            return "Nenhuma simulação executada."
        
        # Calcula estatísticas
        valores = np.array(self.historico)
        crescimento = valores[-1] - valores[0]
        media = np.mean(valores)
        desvio = np.std(valores)
        max_val = np.max(valores)
        min_val = np.min(valores)
        
        print("\n" + "=" * 60)
        print("ANÁLISE DA TENDÊNCIA DO RELACIONAMENTO")
        print("=" * 60)
        
        print(f"\n📊 ESTATÍSTICAS:")
        print(f"   Valor inicial: {valores[0]:.3f}")
        print(f"   Valor final: {valores[-1]:.3f}")
        print(f"   Crescimento total: {crescimento:+.3f}")
        print(f"   Média: {media:.3f}")
        print(f"   Desvio padrão: {desvio:.3f}")
        print(f"   Valor máximo: {max_val:.3f}")
        print(f"   Valor mínimo: {min_val:.3f}")
        
        print(f"\n🔍 TENDÊNCIA:")
        if crescimento > 1.0:
            print("   ✅ FORTE CRESCIMENTO: Relacionamento melhorando significativamente.")
        elif crescimento > 0.1:
            print("   📈 CRESCIMENTO MODERADO: Relacionamento em melhora.")
        elif abs(crescimento) <= 0.1:
            print("   ➡️  ESTÁVEL: Relacionamento mantém nível similar.")
        elif crescimento < -0.1:
            print("   📉 DECLÍNIO MODERADO: Relacionamento em declínio.")
        elif crescimento < -1.0:
            print("   ❌ FORTE DECLÍNIO: Relacionamento piorando significativamente.")
        
        # Análise de estabilidade
        if desvio < 0.3:
            print("   🛡️  ESTÁVEL: Baixa volatilidade emocional.")
        elif desvio < 0.7:
            print("   ⚠️  MODERADAMENTE VOLÁTIL: Algumas oscilações emocionais.")
        else:
            print("   🌀 ALTA VOLATILIDADE: Fortes oscilações emocionais.")
        
        # Diagnóstico baseado nos coeficientes
        print(f"\n🎯 DIAGNÓSTICO BASEADO NOS COEFICIENTES:")
        
        # Caso 1: Desinteresse (a ≈ 0)
        if abs(self.a) < 0.1:
            if self.b > 0:
                print("   📌 RELACIONAMENTO POR CONVENIÊNCIA")
                print("      Sem conexão emocional, mas fatores externos mantêm a relação.")
            else:
                print("   📌 RELACIONAMENTO EM RISCO")
                print("      Sem conexão emocional e com fatores externos negativos.")
        
        # Caso 2: Estabilidade saudável (0.3 < |a| < 0.7, b positivo ou neutro)
        elif 0.3 < abs(self.a) < 0.7 and self.b >= -0.2:
            print("   📌 RELACIONAMENTO SAUDÁVEL")
            print("      Conexão emocional equilibrada com ambiente favorável.")
        
        # Caso 3: Instabilidade emocional (|a| > 1)
        elif abs(self.a) > 1.0:
            if self.b > 0:
                print("   📌 RELACIONAMENTO INTENSO E IMPREVISÍVEL")
                print("      Emoções amplificadas, mas com apoio externo.")
            else:
                print("   📌 RELACIONAMENTO EM RISCO DE COLAPSO")
                print("      Emoções amplificadas em ambiente desfavorável.")
        
        # Caso 4: Padrão negativo (a < 0)
        elif self.a < -0.3:
            print("   📌 PADRÃO DE CONFLITO")
            print("      Reações emocionais inversas, possíveis ciclos de conflito.")
        
        # Recomendações
        print(f"\n💡 RECOMENDAÇÕES:")
        
        if abs(self.a) < 0.2:
            print("   • Trabalhar na conexão emocional e memória afetiva.")
            print("   • Criar rituais e experiências compartilhadas.")
        
        if abs(self.a) > 1.0:
            print("   • Buscar moderar reações emocionais.")
            print("   • Considerar aconselhamento para regular intensidade emocional.")
        
        if self.a < 0:
            print("   • Identificar padrões de reação negativa.")
            print("   • Trabalhar comunicação para quebrar ciclos negativos.")
        
        if self.b < -0.3:
            print("   • Reduzir fontes externas de estresse.")
            print("   • Estabelecer limites com interferências externas.")
        
        if self.b > 0.3:
            print("   • Aproveitar o apoio externo para fortalecer a relação.")
            print("   • Manter rede de apoio e fatores positivos.")
        
        return {
            'crescimento': crescimento,
            'media': media,
            'desvio': desvio,
            'max': max_val,
            'min': min_val
        }
    
    def plotar_simulacao(self, titulo="Evolução do Relacionamento"):
        """
        Plota a evolução do relacionamento ao longo do tempo.
        
        Args:
            titulo: Título do gráfico
        """
        if not self.historico:
            print("Nenhuma simulação para plotar.")
            return
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
        
        # Gráfico 1: Evolução temporal
        ax1.plot(self.meses, self.historico, 'b-', linewidth=2, marker='o', markersize=6)
        ax1.axhline(y=0, color='r', linestyle='--', alpha=0.5)
        ax1.fill_between(self.meses, self.historico, 0, where=np.array(self.historico)>=0, 
                        alpha=0.3, color='green', interpolate=True)
        ax1.fill_between(self.meses, self.historico, 0, where=np.array(self.historico)<=0, 
                        alpha=0.3, color='red', interpolate=True)
        ax1.set_xlabel('Mês')
        ax1.set_ylabel('Estado do Relacionamento')
        ax1.set_title(f'{titulo}\na = {self.a:.3f}, b = {self.b:.3f}')
        ax1.grid(True, alpha=0.3)
        ax1.set_xlim([0, len(self.meses)-1])
        
        # Adiciona anotações para pontos críticos
        max_idx = np.argmax(self.historico)
        min_idx = np.argmin(self.historico)
        
        if max_idx != 0 and max_idx != len(self.historico)-1:
            ax1.annotate(f'Máx: {self.historico[max_idx]:.2f}', 
                        xy=(max_idx, self.historico[max_idx]),
                        xytext=(max_idx, self.historico[max_idx] + 0.5),
                        arrowprops=dict(arrowstyle='->', color='green'))
        
        if min_idx != 0 and min_idx != len(self.historico)-1:
            ax1.annotate(f'Mín: {self.historico[min_idx]:.2f}', 
                        xy=(min_idx, self.historico[min_idx]),
                        xytext=(min_idx, self.historico[min_idx] - 0.5),
                        arrowprops=dict(arrowstyle='->', color='red'))
        
        # Gráfico 2: Diagrama de fases (a vs b)
        ax2.scatter(self.a, self.b, s=200, c='red', alpha=0.7, edgecolors='black')
        
        # Regiões no diagrama de fases
        ax2.axvline(x=0, color='gray', linestyle='--', alpha=0.5)
        ax2.axhline(y=0, color='gray', linestyle='--', alpha=0.5)
        
        # Adiciona regiões de diagnóstico
        ax2.add_patch(plt.Rectangle((-1.5, -1), 1.5, 2, alpha=0.1, color='red', label='Risco de Colapso (a<0)'))
        ax2.add_patch(plt.Rectangle((0, -1), 0.3, 2, alpha=0.1, color='yellow', label='Desinteresse (a≈0)'))
        ax2.add_patch(plt.Rectangle((0.3, -1), 0.7, 2, alpha=0.1, color='lightgreen', label='Estabilidade (0.3≤a<1)'))
        ax2.add_patch(plt.Rectangle((1.0, -1), 0.5, 2, alpha=0.1, color='orange', label='Amplificação (a>1)'))
        
        ax2.set_xlabel('Coeficiente Emocional (a)')
        ax2.set_ylabel('Força Externa (b)')
        ax2.set_title('Diagnóstico: a vs b')
        ax2.grid(True, alpha=0.3)
        ax2.set_xlim([-1.5, 1.5])
        ax2.set_ylim([-1, 1])
        
        # Legenda simplificada
        ax2.legend(loc='upper left', fontsize=8)
        
        plt.tight_layout()
        plt.show()
    
    def executar_simulacao_completa(self, num_meses=12):
        """Executa uma simulação completa do relacionamento."""
        print("=" * 60)
        print("SIMULAÇÃO DE DINÂMICA DE RELACIONAMENTO")
        print("=" * 60)
        
        # Coleta os coeficientes via questionário
        print("\n[PASSO 1/3] Avaliação do coeficiente emocional (a)")
        self.questionario_coeficiente_a()
        
        print("\n[PASSO 2/3] Avaliação da força externa (b)")
        self.questionario_coeficiente_b()
        
        print("\n[PASSO 3/3] Simulação da evolução do relacionamento")
        
        # Estado inicial neutro
        estado_inicial = 0.0
        
        # Simula os meses
        self.simular_meses(num_meses=num_meses, estado_inicial=estado_inicial)
        
        # Mostra análise
        self.analisar_tendencia()
        
        # Plota resultados
        self.plotar_simulacao()
        
        return self.historico


# Função para exemplo rápido (sem questionário interativo)
def exemplo_rapido():
    """Executa um exemplo rápido do modelo."""
    print("EXEMPLO RÁPIDO - DIFERENTES CENÁRIOS DE RELACIONAMENTO")
    print("=" * 60)
    
    # Cria instância do modelo
    modelo = RelacionamentoLinear()
    
    # Define cenários de exemplo
    cenarios = [
        {"nome": "RELACIONAMENTO ESTÁVEL E SAUDÁVEL", "a": 0.6, "b": 0.2},
        {"nome": "DESINTERESSE PROGRESSIVO", "a": 0.1, "b": -0.1},
        {"nome": "COLAPSO EMOCIONAL", "a": 1.3, "b": -0.3},
        {"nome": "AMOR INTENSO COM APOIO", "a": 1.2, "b": 0.4},
        {"nome": "CICLOS NEGATIVOS", "a": -0.5, "b": 0.1},
    ]
    
    for i, cenario in enumerate(cenarios):
        print(f"\n\n{'='*60}")
        print(f"CENÁRIO {i+1}: {cenario['nome']}")
        print(f"{'='*60}")
        
        # Configura os coeficientes
        modelo.a = cenario['a']
        modelo.b = cenario['b']
        
        # Interpreta os coeficientes
        modelo.interpretar_coeficiente_a()
        modelo.interpretar_coeficiente_b()
        
        # Simula 12 meses
        modelo.simular_meses(num_meses=12, estado_inicial=0.0)
        
        # Mostra análise
        modelo.analisar_tendencia()
        
        # Plota (apenas para o primeiro cenário para não sobrecarregar)
        if i == 0:
            modelo.plotar_simulacao(titulo=cenario['nome'])


# Função principal
def main():
    """Função principal do programa."""
    print("=" * 60)
    print("MODELO DE DINÂMICA DE RELACIONAMENTO")
    print("Baseado em Iteração Linear: Rₙ = a·Rₙ₋₁ + b")
    print("=" * 60)
    
    while True:
        print("\nMENU PRINCIPAL:")
        print("1. Executar simulação completa com questionário")
        print("2. Ver exemplos rápidos de diferentes cenários")
        print("3. Sair")
        
        escolha = input("\nEscolha uma opção (1-3): ")
        
        if escolha == "1":
            # Cria instância do modelo
            modelo = RelacionamentoLinear()
            
            # Executa simulação completa
            modelo.executar_simulacao_completa(num_meses=12)
            
            input("\nPressione Enter para continuar...")
            
        elif escolha == "2":
            # Mostra exemplos rápidos
            exemplo_rapido()
            input("\nPressione Enter para continuar...")
            
        elif escolha == "3":
            print("\nObrigado por usar o modelo de dinâmica de relacionamento!")
            break
            
        else:
            print("Opção inválida. Tente novamente.")


# Executa o programa se for executado diretamente
if __name__ == "__main__":
    main()
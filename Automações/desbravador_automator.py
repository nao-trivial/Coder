from engine_automate import AutomacaoMouse

# Uso da classe para realizar as ações
def login():
    automacao_mouse = AutomacaoMouse()

    # Esperar 5 segundos para se preparar
    automacao_mouse.esperar(5)

    # Clique no icone.exe
    automacao_mouse.realizar_acao((1380, 275), automacao_mouse.duplo_clique)
    
    # Esperar iniciar
    automacao_mouse.esperar(5)
    
    # Usuario
    automacao_mouse.realizar_acao((726, 443), automacao_mouse.duplo_clique)
    automacao_mouse.realizar_acao((726, 443), automacao_mouse.digitar, 'HAPR')
    automacao_mouse.realizar_acao((726, 443), automacao_mouse.pressionar_enter)

    # Senha
    automacao_mouse.realizar_acao((730, 468), automacao_mouse.digitar, '919277')
    automacao_mouse.realizar_acao((730, 468), automacao_mouse.pressionar_enter)

    # Clique em Okay
    automacao_mouse.realizar_acao((730, 468), automacao_mouse.pressionar_enter)
    
    # Coloque a senha novamente
    automacao_mouse.realizar_acao((765, 487), automacao_mouse.digitar, '919277')
    automacao_mouse.realizar_acao((765, 487), automacao_mouse.pressionar_enter)

def cadastro():
    automacao_mouse = AutomacaoMouse()

    # Entra no cadastro de hospede principal
    coordenadas = [
        (71, 755), (578, 388),
        (399, 347), (399, 347)
    ]
    for posicao in coordenadas:
        automacao_mouse.realizar_acao(posicao, automacao_mouse.clicar)
    automacao_mouse.realizar_acao((399, 347), automacao_mouse.duplo_clique)

    

def check_in():
    automacao_mouse = AutomacaoMouse()

    #Insira um nome inicial para realizar busca
    pax = input("Insira o nome do pax: ")

    # Iniciar busca
    automacao_mouse.realizar_acao((726, 443), automacao_mouse.duplo_clique)
    automacao_mouse.realizar_acao((102, 54), automacao_mouse.clicar)
    automacao_mouse.realizar_acao((93, 136), automacao_mouse.clicar)
    automacao_mouse.realizar_acao((93, 136), automacao_mouse.digitar, pax)
    automacao_mouse.realizar_acao((1149, 244), automacao_mouse.clicar)


# Executar a automação
if __name__ == "__main__":
    cadastro()
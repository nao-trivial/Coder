from engine_automate import AutomacaoMouse

# Uso da classe para realizar as ações
def automacao():
    automacao_mouse = AutomacaoMouse()

    # Esperar 5 segundos para se preparar
    automacao_mouse.esperar(5)

    # Realizar as ações de automação
    automacao_mouse.realizar_acao((1380, 275), automacao_mouse.duplo_clique)
    
    # Esperar 5 segundos
    automacao_mouse.esperar(5)
    
    automacao_mouse.realizar_acao((730, 468), automacao_mouse.digitar, '919277')
    automacao_mouse.realizar_acao((730, 468), automacao_mouse.pressionar_enter)

    automacao_mouse.realizar_acao((731, 542), automacao_mouse.clicar)
    automacao_mouse.realizar_acao((765, 487), automacao_mouse.clicar)
    
    automacao_mouse.realizar_acao((765, 487), automacao_mouse.digitar, '919277')
    automacao_mouse.realizar_acao((765, 487), automacao_mouse.pressionar_enter)
    
    automacao_mouse.realizar_acao((102, 54), automacao_mouse.clicar)
    
    pax = input("Insira o nome do pax: ")
    
    automacao_mouse.realizar_acao((93, 136), automacao_mouse.clicar)
    automacao_mouse.realizar_acao((93, 136), automacao_mouse.digitar, pax)
    
    automacao_mouse.realizar_acao((1149, 244), automacao_mouse.clicar)


# Executar a automação
if __name__ == "__main__":
    automacao()
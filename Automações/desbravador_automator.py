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

# Função para fazer cadastro
def faca_cadastro():
    automacao_mouse = AutomacaoMouse()

    nome = input("Insira o nome compelto: ")
    cpf_id = input("Insira o cpf/id: ")
    cep_zip = input("Insira o cep: ")
    contato = input("Insira o numero p/ ctt: ")
    email = input("Insira o email p/ ctt: ")

    # Selecione o pais internacional para evitar problemas com Ex
    automacao_mouse.realizar_acao((597, 468), automacao_mouse.clicar)
    automacao_mouse.realizar_acao((597, 468), automacao_mouse.pressionar_baixo)
    automacao_mouse.realizar_acao((597, 468), automacao_mouse.pressionar_enter)

    # Nome + CPF
    automacao_mouse.realizar_acao((673, 261), automacao_mouse.clicar)
    automacao_mouse.realizar_acao((673, 261), automacao_mouse.digitar, nome)
    automacao_mouse.realizar_acao((673, 261), automacao_mouse.pressionar_enter)
    automacao_mouse.realizar_acao((673, 261), automacao_mouse.digitar, cpf_id)

    # Endereço 
    automacao_mouse.realizar_acao((774, 469), automacao_mouse.clicar)
    automacao_mouse.realizar_acao((774, 469), automacao_mouse.digitar, cep_zip)
    automacao_mouse.realizar_acao((774, 469), automacao_mouse.pressionar_enter)
    automacao_mouse.realizar_acao((774, 469), automacao_mouse.pressionar_enter)
    automacao_mouse.realizar_acao((927, 517), automacao_mouse.clicar)

    # Formas de contato
    automacao_mouse.realizar_acao((590, 560), automacao_mouse.clicar)
    automacao_mouse.realizar_acao((590, 560), automacao_mouse.digitar, contato)
    automacao_mouse.realizar_acao((582, 610), automacao_mouse.clicar)
    automacao_mouse.realizar_acao((582, 610), automacao_mouse.digitar, email)

# Função para abrir cadastro
def abrir_cadastro():
    automacao_mouse = AutomacaoMouse()

    # Entra no cadastro de hospede principal
    coordenadas = [
        (71, 755), (578, 388),
        (399, 347), (399, 347)
    ]
    for posicao in coordenadas:
        automacao_mouse.realizar_acao(posicao, automacao_mouse.clicar)
    automacao_mouse.realizar_acao((399, 347), automacao_mouse.duplo_clique)

# Função para abrir o check-in e buscar pax
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

# Menu de opções
def exibir_menu():
    print("\nMenu de opções:")
    print("1. Login")
    print("2. Cadastro")
    print("3. Cadastro de Hóspede")
    print("4. Check-in")
    print("5. Sair")

# Função principal para executar o menu
def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-5): ")

        if opcao == '1':
            print("Executando Login...")
            login()
        elif opcao == '2':
            print("Executando Cadastro...")
            abrir_cadastro()
        elif opcao == '3':
            print("Executando Cadastro de Hóspede...")
            faca_cadastro()
        elif opcao == '4':
            print("Executando Check-in...")
            check_in()
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção entre 1 e 5.")

if __name__ == "__main__":
    main()
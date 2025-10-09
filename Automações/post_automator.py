from engine_automate import AutomacaoMouse

# Função principal que executa a automação
def automacao():
    automacao_mouse = AutomacaoMouse()

    # Esperar 5 segundos para se preparar
    automacao_mouse.esperar(5)

    # Realizar o clique em um local específico
    automacao_mouse.realizar_acao((1157, 1050), automacao_mouse.clicar)

    # Esperar 5 segundos
    automacao_mouse.esperar(5)

    # Digitar URL
    automacao_mouse.digitar('https://www.anroll.net/a/IlmxWi1ryo')
    automacao_mouse.pressionar_enter()

    """nome_do_post = input("Insira o nome do post a ser postado: ")

    # Realizar o clique para inserir o nome do post
    automacao_mouse.realizar_acao((1301, 140), automacao_mouse.clicar)
    automacao_mouse.digitar(nome_do_post)
    automacao_mouse.pressionar_enter()

    # Verificar se o post é o primeiro
    verificacao1 = input("O post é o primeiro? Responda com o numero '1' se o for: ")

    if verificacao1 == "1":
        # Realizar o clique se for o primeiro post
        automacao_mouse.realizar_acao((1173, 461), automacao_mouse.clicar)

    # Realizar outros cliques
    coordenadas = [
        (1845, 280),
        (1894, 144),
        (1466, 651),
        (1716, 321),
        (1654, 468),
        (1638, 714)
    ]

    for posicao in coordenadas:
        automacao_mouse.realizar_acao(posicao, automacao_mouse.clicar)

    # Esperar 15 segundos para se preparar
    automacao_mouse.esperar(15)"""


# Executar a automação
if __name__ == "__main__":
    automacao()

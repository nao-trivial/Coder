import pyautogui
import time

class AutomacaoMouse:
    def __init__(self, duracao_move=2):
        self.duracao_move = duracao_move
    
    def esperar(self, segundos):
        """Aguardar um determinado tempo."""
        time.sleep(segundos)
    
    def mover_para(self, posicao):
        """Mover o mouse para a posição desejada."""
        pyautogui.moveTo(posicao, duration=self.duracao_move)
    
    def clicar(self):
        """Realizar um clique do mouse."""
        pyautogui.click()
    
    def duplo_clique(self):
        """Realizar um duplo clique do mouse."""
        pyautogui.doubleClick()
    
    def digitar(self, texto, intervalo=0.1):
        """Digitar um texto com intervalo entre as teclas."""
        pyautogui.write(texto, interval=intervalo)
    
    def pressionar_enter(self):
        """Pressionar a tecla Enter."""
        pyautogui.press('enter')

    def pressionar_baixo(self):
        # Pressione a tecla baixo
        pyautogui.press('down')

    def realizar_acao(self, posicao, acao, *args):
        """Executar uma ação em uma posição específica."""
        self.mover_para(posicao)
        acao(*args)

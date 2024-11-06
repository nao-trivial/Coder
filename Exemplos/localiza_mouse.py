import pyautogui
import time

# Aguardar 5 segundos
time.sleep(5)

# Obter a posição do mouse
posicao_mouse = pyautogui.position()

# Exibir a posição
print(f'A posição do mouse após 5 segundos é: {posicao_mouse}')

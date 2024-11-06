import pyautogui
import time

# Esperar 5 segundos para você se preparar
time.sleep(5)

# Coordenadas desejadas
posicao = (1380, 275)

# Mover o mouse para a posição especificada e clicar
pyautogui.click(posicao)

print(f'Cliquei na posição {posicao}')

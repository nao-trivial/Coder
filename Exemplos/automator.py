import pyautogui
import time

# Esperar 5 segundos para você se preparar
time.sleep(5)

# Coordenadas desejadas
posicao = (1380, 275)
# Mover o mouse para a posição desejada com uma duração de 3 segundos
pyautogui.moveTo(posicao, duration=3)

# Realizar o duplo clique
pyautogui.doubleClick()

# Esperar 5 segundos para você se preparar
time.sleep(5)

# Coordenadas desejadas
posicao = (730, 468)
# Mover o mouse para a posição desejada com uma duração de 3 segundos
pyautogui.moveTo(posicao, duration=3)

# Digitar um texto
pyautogui.write('919277', interval=0.1)

# Pressionar Enter
pyautogui.press('enter')

# Coordenadas desejadas
posicao = (731, 542)
# Mover o mouse para a posição desejada com uma duração de 3 segundos
pyautogui.moveTo(posicao, duration=3)
pyautogui.click()

# Coordenadas desejadas
posicao = (765, 487)
# Mover o mouse para a posição desejada com uma duração de 3 segundos
pyautogui.moveTo(posicao, duration=3)
pyautogui.click()

# Digitar um texto
pyautogui.write('919277', interval=0.1)

# Pressionar Enter
pyautogui.press('enter')

# Coordenadas desejadas
posicao = (102, 54)
# Mover o mouse para a posição desejada com uma duração de 3 segundos
pyautogui.moveTo(posicao, duration=3)
pyautogui.click()

pax = input("insira o nome do pax: ")

# Coordenadas desejadas
posicao = (93, 136)
# Mover o mouse para a posição desejada com uma duração de 3 segundos
pyautogui.moveTo(posicao, duration=3)
pyautogui.click()

# Digitar um texto
pyautogui.write(pax, interval=0.1)

# Coordenadas desejadas
posicao = (1149, 244)
# Mover o mouse para a posição desejada com uma duração de 3 segundos
pyautogui.moveTo(posicao, duration=3)
pyautogui.click()
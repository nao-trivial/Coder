import pyautogui
import time

# Esperar 5 segundos para você se preparar
time.sleep(5)

# Coordenadas desejadas
posicao = (1453, 1066)
# Mover o mouse para a posição desejada com uma duração de 3 segundos
pyautogui.moveTo(posicao, duration=3)

# Esperar 5 segundos para você se preparar
time.sleep(5)

# Realizar o clique
pyautogui.click()

# Esperar 5 segundos para você se preparar
time.sleep(5)

# Digitar um texto
pyautogui.write('https://www.canva.com/', interval=0.1)

# Pressionar Enter
pyautogui.press('enter')

nome_do_post = input("Insira o nome do post a ser postado: ")

# Coordenadas desejadas
posicao = (1301, 140)
# Mover o mouse para a posição desejada com uma duração de 3 segundos
pyautogui.moveTo(posicao, duration=3)

# Realizar o clique
pyautogui.click()

# Digitar um texto
pyautogui.write(nome_do_post, interval=0.1)

# Pressionar Enter
pyautogui.press('enter')

verificacao1 = input("O post é o primeiro? Responda com o numero '1' se o for (exemplo)")

if verificacao1 == "1":
    # Coordenadas desejadas
    posicao = (1173, 461)
    # Mover o mouse para a posição desejada com uma duração de 3 segundos
    pyautogui.moveTo(posicao, duration=3)

    # Realizar o clique
    pyautogui.click()

# Coordenadas desejadas
posicao = (1845, 280)
# Mover o mouse para a posição desejada com uma duração de 3 segundos
pyautogui.moveTo(posicao, duration=3)
# Realizar o clique
pyautogui.click()

# Coordenadas desejadas
posicao = (1894, 144)
# Mover o mouse para a posição desejada com uma duração de 3 segundos
pyautogui.moveTo(posicao, duration=3)
# Realizar o clique
pyautogui.click()

# Coordenadas desejadas
posicao = (1466, 651)
# Mover o mouse para a posição desejada com uma duração de 3 segundos
pyautogui.moveTo(posicao, duration=3)
# Realizar o clique
pyautogui.click()

# Coordenadas desejadas
posicao = (1716, 321)
# Mover o mouse para a posição desejada com uma duração de 3 segundos
pyautogui.moveTo(posicao, duration=3)
# Realizar o clique
pyautogui.click()

# Coordenadas desejadas
posicao = (1654, 468)
# Mover o mouse para a posição desejada com uma duração de 3 segundos
pyautogui.moveTo(posicao, duration=3)
# Realizar o clique
pyautogui.click()

# Coordenadas desejadas
posicao = (1654, 468)
# Mover o mouse para a posição desejada com uma duração de 3 segundos
pyautogui.moveTo(posicao, duration=3)
# Realizar o clique
pyautogui.click()

# Coordenadas desejadas
posicao = (1638, 714)
# Mover o mouse para a posição desejada com uma duração de 3 segundos
pyautogui.moveTo(posicao, duration=3)
# Realizar o clique
pyautogui.click()

# Esperar 5 segundos para você se preparar
time.sleep(15)


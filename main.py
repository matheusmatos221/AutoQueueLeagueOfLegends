import pyautogui as py


'''

0,0       X increases -->
+---------------------------+
|                           | Y increases
|                           |     |
|   1920 x 1080 screen      |     |
|                           |     V
|                           |
|                           |
+---------------------------+ 1919, 1079

'''

def run():
    #  Enquanto não aceitar a partida, tenta aceitar
    while True:
        if aceitar():
            break

#  1. Clica em aceitar partida
def aceitar():
    screen_pos = py.locateOnScreen('images/aceitar.JPG', grayscale=True, confidence=0.8)
    if screen_pos is not None:
        py.click(py.center(screen_pos))
        return True
    return False



#  2. Bane o campeão
#  3. Escolhe o campeão (De acordo com a posição, verifica os disponíveis)
#  4. Runas e Talentos


if __name__ == '__main__':
    run()
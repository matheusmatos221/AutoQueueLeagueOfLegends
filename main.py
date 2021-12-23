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
    init_message()
    #  Enquanto não aceitar a partida, tenta aceitar
    while True:
        if aceitar():
            break
    print("Programa finalizado.")

#  1. Clica em aceitar partida
def aceitar():
    screen_pos = py.locateOnScreen('images/aceitar.JPG', grayscale=True, confidence=0.8)
    if screen_pos is not None:
        py.click(py.center(screen_pos))
        print("ACEITAR encontrado!")
        return True
    print("Procurando pelo botão ACEITAR")
    return False



#  2. Bane o campeão
#  3. Escolhe o campeão (De acordo com a posição, verifica os disponíveis)
#  4. Runas e Talentos

def init_message():
    print(
          "|==================================================================================||\n"
          "||   _______  __   __  _______  _______    _______  _______  _______               ||\n"
          "||  |   _   ||  | |  ||       ||       |  |   _   ||       ||       |              ||\n"
          "||  |  |_|  ||  | |  ||_     _||   _   |  |  |_|  ||       ||       |              ||\n"
          "||  |       ||  |_|  |  |   |  |  | |  |  |       ||       ||       |              ||\n"
          "||  |       ||       |  |   |  |  |_|  |  |       ||      _||      _|              ||\n"
          "||  |   _   ||       |  |   |  |       |  |   _   ||     |_ |     |_               ||\n"
          "||  |__| |__||_______|  |___|  |_______|  |__| |__||_______||_______|              ||\n"
          "||   ___      _______  _______  _______  __   __  _______       _______  __   __   ||\n"
          "||  |   |    |       ||   _   ||       ||  | |  ||       |     |       ||  | |  |  ||\n"
          "||  |   |    |    ___||  |_|  ||    ___||  | |  ||    ___|     |    _  ||  |_|  |  ||\n"
          "||  |   |    |   |___ |       ||   | __ |  |_|  ||   |___      |   |_| ||       |  ||\n"
          "||  |   |___ |    ___||       ||   ||  ||       ||    ___| ___ |    ___||_     _|  ||\n"
          "||  |       ||   |___ |   _   ||   |_| ||       ||   |___ |   ||   |      |   |    ||\n"
          "||  |_______||_______||__| |__||_______||_______||_______||___||___|      |___|    ||\n"
          "||                                                                                 ||\n"
          "|==================================================================================||\n")


    print("Inicializando programa...")



if __name__ == '__main__':
    run()
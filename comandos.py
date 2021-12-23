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

class Comandos:
    @staticmethod
    def aceitar():
        screen_pos = py.locateOnScreen('images/aceitar.JPG', grayscale=True, confidence=0.8)
        if screen_pos is not None:
            py.click(py.center(screen_pos))
            print("ACEITAR encontrado!")
            return True
        print("Procurando pelo botão ACEITAR")
        return False

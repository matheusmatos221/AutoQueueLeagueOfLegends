import pyautogui as py


class Comandos:
    @staticmethod
    def click_accept():
        screen_pos = py.locateOnScreen('images/aceitar.JPG', grayscale=True, confidence=0.8)
        if screen_pos is not None:
            py.click(py.center(screen_pos))
            print("ACEITAR encontrado!")
            return True
        print("ACEITAR não encontrado!")
        return False

    @staticmethod
    def is_support():
        """Se a role for suporte, retorna TRUE, se não for retorna FALSE"""
        if py.locateOnScreen('images/role_sup.JPG', grayscale=True, confidence=0.8) is not None:
            print("É SUPORTE!")
            return True
        print("Não é SUPORTE!")
        return False

    @staticmethod
    def time_to_choose():
        """É a vez de escolher = TRUE or FALSE"""
        if py.locateOnScreen('images/escolha.JPG', grayscale=True, confidence=0.8) is not None:
            print("Vez de escolher!")
            return True
        print("Não é a vez de escolher!")
        return False

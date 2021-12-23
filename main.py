from mensagens import Mensagens
from comandos import Comandos


def run():
    Mensagens.init_message()
    #  Enquanto não aceitar a partida, tenta aceitar
    while True:
        if Comandos.click_accept():
            break
    Mensagens.finish_message()


#  1. Clica em aceitar partida
#  2. Bane o campeão
#  3. Escolhe o campeão (De acordo com a posição, verifica os disponíveis)
#  4. Runas e Talentos

if __name__ == '__main__':
    run()

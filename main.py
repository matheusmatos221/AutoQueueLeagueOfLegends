
from mensagens import Mensagens as msg
from comandos import Comandos as cmd


def run():
    msg.init_message()
    #  Enquanto não aceitar a partida, tenta aceitar
    while True:
        if cmd.aceitar():
            break
    msg.finish_message()

#  1. Clica em aceitar partida
#  2. Bane o campeão
#  3. Escolhe o campeão (De acordo com a posição, verifica os disponíveis)
#  4. Runas e Talentos



if __name__ == '__main__':
    run()
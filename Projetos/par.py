import random
import time
import os

while True:

    jogador_1 = random.randint(1,10)
    jogador_2 = random.randint(1,10)
    resultado = (jogador_1+jogador_2)


    print(jogador_1)
    time.sleep(0.7)
    print(jogador_2)
    time.sleep(0.7)
    if resultado%2==0:
        print("Par venceu")
    else:
        print("ímpar ganhou")
        time.sleep(1)
        os.system("cls")
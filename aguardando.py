import os
import time

pontos = [".", "..", "..."]

while True:

    for ponto in pontos:
        print("Aguardando" + ponto)
        time.sleep(0.5)
        os.system("cls")
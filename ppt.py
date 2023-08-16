import random 
import time
import os

while True:

    jogador_1 = random.choice(["Pedra".lower(),"Papel".lower(), "Tesoura".lower()])
    jogador_2 = random.choice(["Pedra".lower(),"Papel".lower(), "Tesoura".lower()])
    
    print("Jogador 1 escolheu: " + jogador_1)
    time.sleep(0.5)
    print("Jogador 2 escolheu: " + jogador_2)
    time.sleep(0.5)

    if jogador_1 == jogador_2:
        print("Resultado: empate")
    elif jogador_1 == "pedra" and jogador_2 == "tesoura":
        print("Jogador 1 venceu")
    elif jogador_1 == "pedra" and jogador_2 == "papel":
        print("Jogador 1 perdeu")
    elif jogador_1 == "tesoura" and jogador_2 == "papel":
        print("Jogador 1 venceu")
    elif jogador_1 == "tesoura" and jogador_2 == "pedra":
        print("Jogador 1 perdeu")
    elif jogador_1 == "papel" and jogador_2 == "pedra":
        print("Jogador 1 venceu")
    elif jogador_1 == "papel" and jogador_2 == "tesoura":
        print("Jogador 1 perdeu")
    else:
        print("Entrada inválida")
    time.sleep(0.5)
    os.system("cls")

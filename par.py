import random 
 
min = input("Pedra, papel ou tesoura?\n")
jogador_2 = random.choice(["Pedra".lower(),"Papel".lower(), "Tesoura".lower()])
jogador_1 = min.lower()


print("Jogador 1 digitou: " + jogador_1)
print("Jogador 2 digitou: " + jogador_2)


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
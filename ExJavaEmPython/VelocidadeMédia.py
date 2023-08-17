distancia = input ("Digite a distância percorrida em km: ")
tempo = input("Digite o tempo percorrido em horas: ")

distanciaMetros = int(distancia)*1000
tempoSegundos = int(tempo)*3600

resultado = distanciaMetros/tempoSegundos

print(f"{resultado:.2f} metros por segundo")
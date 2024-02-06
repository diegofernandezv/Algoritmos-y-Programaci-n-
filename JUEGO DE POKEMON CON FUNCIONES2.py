import random

def malicioso(PS_jugador):
    PS_jugador = (PS_jugador[0], max(1, PS_jugador[1] - 10))
    return PS_jugador

def placaje(PS_jugador):
    PS_jugador = (max(0, PS_jugador[0] - 35 / (PS_jugador[1]/100)), PS_jugador[1])
    return PS_jugador

def ascuas(PS_jugador):
    PS_jugador = (max(0, PS_jugador[0] - 20), PS_jugador[1])
    return PS_jugador

def latigo(PS_jugador):
    PS_jugador = (PS_jugador[0], max(1, PS_jugador[1] - 10))
    return PS_jugador

def pistola_agua(PS_jugador):
    PS_jugador = (max(0, PS_jugador[0] - 40), PS_jugador[1])
    return PS_jugador

PS_jugador = (100, 100)
PS_oponente = (100, 100)

while PS_jugador[0] > 0 and PS_oponente[0] > 0: 
    ataque_jugador = input("Elige un ataque entre malicioso,ascuas y placaje: ")
    if ataque_jugador in ["malicioso", "placaje", "ascuas"]:
        PS_oponente = globals()[ataque_jugador](PS_oponente)
    else:
        print("Que estas haciendo?! tus ataques son malicioso, placaje, y ascuas!")
        continue

    # turno oponente
    ataque_oponente = random.choice([latigo, placaje, pistola_agua])
    PS_jugador = ataque_oponente(PS_jugador)

# Si termina el ciclo, alguien ha ganado
if PS_oponente[0] <= 0 and PS_jugador[0] <= 0:
    print("Empate")
elif PS_oponente[0] <= 0:  
    print("Felicitaciones, has ganado")
else:  
    print("Lo siento, has perdido")

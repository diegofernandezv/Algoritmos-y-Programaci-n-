import random

PS_jugador = 100 
Ps_oponente = 100
defensa_oponente = 100
defensa_jugador = 100

# Cambié los diccionarios por tuplas en la definición de los ataques
ataque_jugador = [("malicioso", (0, 10)),
                   ("placaje", (35, 0)),
                   ("ascuas", (20, 0))]

ataque_oponente = [("latigo", (10, 10)),
                    ("placaje", (35, 0)),
                    ("pistola de agua", (40, 0))]

while PS_jugador > 0 and Ps_oponente > 0:
    ataque_jugador_input = input("Entre malicioso, ascuas y placaje, decide y haz tu ataque: ")
    
    # Buscar el ataque seleccionado por el jugador en la lista de ataques
    ataque_seleccionado = next((a for a in ataque_jugador if a[0] == ataque_jugador_input.lower()), None)

    if ataque_seleccionado:
        daño, defensa = ataque_seleccionado[1]
        defensa_oponente -= defensa
        if defensa_oponente <= 0:
            defensa_oponente = 1
        Ps_oponente -= daño
    else:
        print("¡Qué estás haciendo?! Tus ataques son maliciosos, placaje y ascuas!")
        continue

    # Turno del Oponente
    ataque_oponente_seleccionado = random.choice(ataque_oponente)
    daño_oponente, defensa_oponente_oponente = ataque_oponente_seleccionado[1]
    
    defensa_jugador -= defensa_oponente_oponente
    if defensa_jugador <= 0:
        defensa_jugador = 1
    
    PS_jugador -= daño_oponente

# Si termina el ciclo, alguien ha ganado
if Ps_oponente <= 0 and PS_jugador > 0:
    print("¡Felicidades, has ganado!")
elif Ps_oponente <= 0 and PS_jugador <= 0:
    print("Empate")
else:
    print("Lo siento, has perdido")

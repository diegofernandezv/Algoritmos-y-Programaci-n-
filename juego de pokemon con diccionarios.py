import random #para Randrange (elegir ataque oponente)


PS_jugador = 100 
Ps_oponente = 100
defensa_oponente=100
defensa_jugador=100
#Podemos cambiar los ataques a un diccionario dentro de una lista o a un diccionario directamente
#Añadi el daño y defensa de cada uno de los ataques para ver que pasaba y me gustó el resultado

ataque_jugador: {"malicioso": {"daño": 0, "defensa": 10},
                   "placaje": {"daño": 35, "defensa": 0},
                   "ascuas": {"daño": 20, "defensa": 0}}
ataque_oponente: {"latigo": {"daño": 0, "defensa": 10},
                    "placaje": {"daño": 35, "defensa": 0},
                    "pistola de agua": {"daño": 40, "defensa": 0}}

while PS_jugador > 0 and Ps_oponente> 0:
    ataque_jugador= input ("Entre malicioso, ascuas y placaje, decide y Haz tu ataque: ")
    if ataque_jugador.lower() == "malicioso":
        defensa_oponente = defensa_oponente - 10
        if defensa_oponente <= 0:
            defensa_oponente = 1
    elif ataque_jugador == "placaje":
        Ps_oponente -= 35 /(defensa_oponente/100)
    elif ataque_jugador == "ascuas":
        Ps_oponente -= 20
        pass
    else:
        print("Que estas haciendo?! Tus ataques son maliciosos, placaje, y ascuas!")
        continue


#Turno del Oponente
    ataque_oponente = random.randrange(1,3+1)
    if ataque_oponente == 1: #latigo
        defensa_jugador -= 10
        if defensa_jugador <= 0:
            defensa_jugador = 1
    elif ataque_oponente == 2 : #placaje
        PS_jugador -= 35 * (100/defensa_jugador)        
    elif ataque_oponente == 3: #Pistola de agua
        PS_jugador -= 40
    #randrange esta garantizado a ser 1,2 o 3

        
#Si termina el ciclo, alguien ha ganado
if Ps_oponente <= 0 :
    print("Felicidades, has ganado")
elif Ps_oponente <= 0 and PS_jugador <= 0:
    print("empate")
else: #ya sabemos que el oponente es > 0
    print("Lo siento, has perdido")



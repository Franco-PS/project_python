import random


"""
Juega con la computadora a priedra papel y tijeras

*ingresa tu opción: pi= piedra, pa= papel y ti= tijeras
la computadora escojio ya la suya es hora de comparrar
"""

def jugar():
    usuario = input("Escoge una opción:").lower()
    computadora = random.choice(["pi","pa","ti"])

    if computadora == usuario:
        return "Empate"
    elif gano_jugador(usuario,computadora):
        return "Ganaste"
    else:
        return "perdiste"

    
def gano_jugador(jugador,oponente):
    if(
        (jugador == "pi" and oponente == "ti") or
        (jugador == "pa" and oponente == "pi") or
        (jugador == "ti" and oponente == "pa")):
        return True
    else:
        return False


print(jugar())


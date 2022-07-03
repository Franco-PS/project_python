import random


def adivina_numero(x):
    print("=============")
    print("   !Bienvenido(a) al Juego¡¡¡  ")
    print("=============")
    print("Tu meta es adivinar el número generado por la computadora.")

    num_aleatorio = random.randint(1, x)

    prediccion = 0

    while prediccion != num_aleatorio:
        # El usuario ingresa un número
        prediccion = int(input(f"adivina un número 1 y el {x}: "))

        if prediccion < num_aleatorio:
            print("El número es más grande")
        elif prediccion > num_aleatorio:
            print("Este número es menor")

    print(f"!Felicidades adivinaste el número: {num_aleatorio}")


adivina_numero(10)
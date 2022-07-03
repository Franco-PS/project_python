import random


def adivina_numero_pc(x):
    print(f"Selecciona el número entre el 1 y  {x} para que la computadora adivine el número")

    limite_inferior = 1  # [1,x]
    limite_superior = x

    respuesta = ""
    while respuesta != "c":
        #generar predicciones
        if limite_inferior != limite_superior:
            prediccion = random.randint(limite_inferior, limite_superior)
        else:
            prediccion = limite_inferior #tambíen pordria ser el limite superor

        #obtener respuesta del usuario

        print("Si es muy alta (A), si es muy baja ingresa B y si es correcto ingresa (C)")
        respuesta = input(f"la compu predijo el número: {prediccion}. ").lower() #lower()-> este método convierte a mínusculas

        if respuesta == "a":
            limite_superior = prediccion - 1
        elif respuesta == "b":
            limite_inferior = prediccion + 1
        # elif respuesta == "c":
    print(f"Siii...¡¡¡ la computadora adivinó tu número {prediccion}")



adivina_numero_pc(20)
preguntas = [
    {
        "pregunta": "¿Cual es la capital de España?",
        "opcion": ["1.Berlín", "2.París", "3.Madrid", "4.Roma"],
        "respuesta": 3, 'tematica': 'Cultura General'
    },
    {
        "pregunta": "¿Cual es el número PI?",
        "opcion": ["1.3,14161718", "2.3", "3.4", "4.5"],
        "respuesta": 1, 'tematica': 'Cultura General'
    },
    # Más preguntas aquí...
]

def Quiz():
    """Función que define la mecánica del juego de preguntas y respuestas.
    
    Permite al jugador responder preguntas y ganar puntos si acierta.
    Si introduce "salir", el juego se detiene inmediatamente.
    """
    marcador = 0
    for pregunta in preguntas:
        print(pregunta["pregunta"])
        print(f'Esta pregunta es de {pregunta["tematica"]}')
        print('---------------------------------------------')
        for opcion in pregunta["opcion"]:
            print(opcion)

        respuesta_concursante = input("Elige una opción (1-4) o escribe 'salir' para terminar: ")
        
        if respuesta_concursante.lower() == "salir":
            print("Has salido del juego. Gracias por jugar!")
            return
        
        try:
            respuesta_concursante = int(respuesta_concursante)
            if respuesta_concursante == pregunta["respuesta"]:
                print("¡Correcto!\n")
                marcador += 1
            else:
                print("Incorrecto. La respuesta correcta era:", pregunta["opcion"][pregunta["respuesta"]-1])
                print("¡HAS PERDIDO!")
                break
        except ValueError:
            print("Por favor, introduce un número válido.")
    
    if marcador == len(preguntas):
        print("¡HAS GANADO EL JUEGO!")

if __name__ == "__main__":
    Quiz()

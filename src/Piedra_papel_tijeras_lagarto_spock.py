import random

# Lista de opciones disponibles para la máquina
listaparamaquina = ['piedra', 'papel', 'tijeras', 'lagarto', 'spock']

# Diccionario que define los ganadores de cada opción
ganadores = {
    'piedra': ['lagarto', 'tijeras'],
    'papel': ['piedra', 'spock'],
    'tijeras': ['papel', 'lagarto'],
    'lagarto': ['spock', 'papel'],
    'spock': ['tijeras', 'piedra']
}

def Piedra_papel_tijeras_lagarto_spock():
    """
    Juego de Piedra, Papel, Tijeras, Lagarto, Spock contra la máquina.
    El jugador compite contra la máquina, eligiendo una de las cinco opciones 
    (piedra, papel, tijeras, lagarto, spock), y la máquina elige aleatoriamente. 
    El objetivo es ganar 3 rondas antes que la máquina.

    En cada ronda, se determina quién gana entre el jugador y la máquina según las reglas del juego.
    Si el jugador escribe 'salir', el juego termina.
    """

    # Inicialización de variables de puntuación
    ganajugador = 0  # Puntuación del jugador
    ganamaquina = 0  # Puntuación de la máquina
    elecciones_maquina = []  # Lista para llevar el control de las elecciones de la máquina

    # Bucle principal del juego, que continúa hasta que un jugador o la máquina gane 3 veces
    while ganajugador < 3 and ganamaquina < 3:
        # Filtra las opciones para que la máquina no repita la elección anterior
        opciones_disponibles = [opcion for opcion in listaparamaquina if opcion not in elecciones_maquina]
        maquina = random.choice(opciones_disponibles)  # La máquina elige una opción aleatoria
        elecciones_maquina.append(maquina)  # Agrega la elección a la lista de elecciones de la máquina

        # Entrada del jugador, se convierte a minúsculas para evitar errores de formato
        jugador1 = input("¿Piedra, Papel, Tijera, Lagarto, Spock? (o escribe 'salir' para terminar): ").lower()

        # Si el jugador escribe 'salir', termina el juego
        if jugador1 == "salir":
            print("Juego terminado por el jugador.")
            exit()

        # Verifica que la opción ingresada por el jugador sea válida
        if jugador1 not in listaparamaquina:
            print("Opción no válida. Por favor elige entre Piedra, Papel, Tijera, Lagarto, Spock.")
            continue  # Si no es válida, vuelve a pedir una opción

        # Muestra la elección de la máquina
        print(f"La máquina eligió: {maquina}")

        # Determina el resultado de la ronda
        if jugador1 == maquina:
            print("Empate")
        elif maquina in ganadores[jugador1]:
            ganajugador += 1  # Si el jugador gana, aumenta su puntuación
            print("Gana el jugador 1")
        else:
            ganamaquina += 1  # Si la máquina gana, aumenta su puntuación
            print("Gana la máquina")

        # Muestra las puntuaciones actuales
        print(f"Victorias del jugador: {ganajugador}")
        print(f"Victorias de la máquina: {ganamaquina}")

        # Si la máquina ha usado todas sus opciones, reinicia su lista de elecciones
        if len(elecciones_maquina) == len(listaparamaquina):
            elecciones_maquina.clear()

    # Anuncia al ganador del juego
    if ganajugador == 3:
        print("¡El jugador 1 ha ganado el juego!")
    else:
        print("¡La máquina ha ganado el juego!")


 
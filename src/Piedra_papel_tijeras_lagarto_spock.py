import random

listaparamaquina = ['piedra', 'papel', 'tijeras', 'lagarto', 'spock']

ganadores = {
    'piedra': ['lagarto', 'tijeras'],
    'papel': ['piedra', 'spock'],
    'tijeras': ['papel', 'lagarto'],
    'lagarto': ['spock', 'papel'],
    'spock': ['tijeras', 'piedra']
}

def juego():
    """Definimos una funcion donde introducimos las normas del juego piedra papel,tijeras,spock,lagarto.
    Args:
         mientras uno de los jugadores no gane 3 partidas el bucle se sigue ejecutando.
         introducimos varios if como condiciones para sabe quien gana la partida.
         hemos definido un diccionario donde tenemos las claves y los valores de las variables ganadoras y perfedoras.
         la maquina elige a traves de import random.
    retun: Nada
    """
    ganajugador = 0
    ganamaquina = 0
    elecciones_maquina = []

    while ganajugador < 3 and ganamaquina < 3:
        opciones_disponibles = [opcion for opcion in listaparamaquina if opcion not in elecciones_maquina]
        maquina = random.choice(opciones_disponibles)
        elecciones_maquina.append(maquina)

        jugador1 = input('¿Piedra, Papel, Tijera, Lagarto, Spock? ').lower()

        if jugador1 not in listaparamaquina:
            print("Opción no válida. Por favor elige entre Piedra, Papel, Tijera, Lagarto, Spock.")
            continue

        print(f"La máquina eligió: {maquina}")

        if jugador1 == maquina:
            print("Empate")
        elif maquina in ganadores[jugador1]:
            ganajugador += 1
            print('Gana el jugador 1')
        else:
            ganamaquina += 1
            print('Gana la máquina')

        print(f"Victorias del jugador: {ganajugador}")
        print(f"Victorias de la máquina: {ganamaquina}")

        if len(elecciones_maquina) == len(listaparamaquina):
            elecciones_maquina.clear()

    if ganajugador == 3:
        print("¡El jugador 1 ha ganado el juego!")
    else:
        print("¡La máquina ha ganado el juego!")


if __name__ == "__main__":
    juego()
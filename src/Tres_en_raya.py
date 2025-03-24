import random
class Tres_en_raya:
    def __init__(self):
        """Defino la clase del juego donde le meto las variables que vamos a ir usando."""
        self.tablero = [[' ' for _ in range(3)] for _ in range(3)]
        self.jugadores = ['X', 'O']
        self.jugadores[0] = input('Jugador 1, dime cómo te llamas: ')
        self.jugadores[1] = input('Jugador 2, dime cómo te llamas: ')
        self.jugadores_nombres = [self.jugadores[0], self.jugadores[1]]
        self.turno = 0
        self.movimientos = 0
        self.jugar()

    def patron_tablero(self):
        """Esta función define el patrón del tablero."""
        print("\n")
        for fila in self.tablero:
            print("----" * 10)
            print("           | ".join(fila))
            print("----" * 10)
        print("\n")
    
    def verificar_ganador(self):
        """Verifica si hay un ganador en el juego."""
        for fila in self.tablero:
            if fila[0] == fila[1] == fila[2] != ' ':
                return fila[0]
        
        for columna in range(3):
            if self.tablero[0][columna] == self.tablero[1][columna] == self.tablero[2][columna] != ' ':
                return self.tablero[0][columna]
        
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != ' ':
            return self.tablero[0][0]
        
        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != ' ':
            return self.tablero[0][2]
        
        return None

    def jugar(self):
        """Función que desarrolla el flujo del juego."""
        while self.movimientos < 9:
            self.patron_tablero()
            jugador_actual = self.jugadores[self.turno % 2]
            if jugador_actual == self.jugadores[0]:
                print(f"Turno del jugador {self.jugadores_nombres[0]}. Elige una fila y columna (0, 1 o 2) o escribe 'salir' para terminar el juego:")
            else:
                print(f"Turno del jugador {self.jugadores_nombres[1]}. Elige una fila y columna (0, 1 o 2) o escribe 'salir' para terminar el juego:")
            
            fila_input = input("Fila: ")
            if fila_input.lower() == "salir":
                print("Juego terminado por el jugador.")
                return
            
            columna_input = input("Columna: ")
            if columna_input.lower() == "salir":
                print("Juego terminado por el jugador.")
                return
            
            try:
                fila = int(fila_input)
                columna = int(columna_input)
            except ValueError:
                print("Entrada inválida. Intenta de nuevo.")
                continue
            
            if fila < 0 or fila > 2 or columna < 0 or columna > 2 or self.tablero[fila][columna] != ' ':
                print("Movimiento inválido. Intenta de nuevo.")
                continue
            
            self.tablero[fila][columna] = jugador_actual
            self.movimientos += 1
            
            ganador = self.verificar_ganador()
            if ganador:
                self.patron_tablero()
                print(f"¡El jugador {ganador} ha ganado!")
                return
            
            self.turno += 1

        self.patron_tablero()
        print("¡Es un empate!")

if __name__ == "__main__":
    Tres_en_raya()


    


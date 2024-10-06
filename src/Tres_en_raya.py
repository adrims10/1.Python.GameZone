import random
class Tres_en_raya:
    def __init__(self):
        """defino la clase del juego donde le meto las variables que vamos a ir usando.
        """
        self.tablero = [[' ' for _ in range(3)] for _ in range(3)]
        self.jugadores = ['X', 'O']
        self.jugadores[0]= input('Jugador 1 dime como te llamas')
        self.jugadores[1]= input('Jugador 2 dime como te llamas')
        self.jugadores_nombres = [ self.jugadores[0],self.jugadores[1]]
        self.turno = 0
        self.movimientos = 0
        self.juego()

    def patron_tablero(self):
        """Esta funcion esta para definir el patron del tablero.
        return:None
        """
        print("\n")
        for fila in self.tablero:
            print("----" * 10)
            print("           | ".join(fila))
            print("----" * 10)
        print("\n")
    
    def verificar_ganador(self):
        """Definimos la siguiente funcion metodo para meter las reglas de la victoria de uno o de otro jugador.
        Arg: Se establecen las condiciones de quien gana si se meten los patrones en las columnas y las filas 
            mediante for e if condicionales.

        Returns:
            _none
        """
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

    def juego(self):
        """funcion metodo que define el juego y como se desarrolla.
        Arg: mientras que sean menos de 9 movimientos, 3 y 3 entonces se desarrola la partida, utilizamos un 
            excep value error por si se mete un valor a la hora de indicar filas y columnas.
            llamamos a la funcion anterior para verificar el ganador 
            y devilvemos el final.
            tambien llamamos a la funcion metodo del patron del tablero
        return: none
        """
        while self.movimientos < 9:
            self.patron_tablero()
            jugador_actual = self.jugadores[self.turno % 2]
            if jugador_actual == self.jugadores[0]:
                print(f"Turno del jugador {self.jugadores_nombres[0]}. Elige una fila y columna (0, 1 o 2):")
            else:
                print(f"Turno del jugador {self.jugadores_nombres[1]}. Elige una fila y columna (0, 1 o 2):")
            try:
                fila = int(input("Fila: "))
                columna = int(input("Columna: "))
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
    
   
    

     

    


from src import Piedra_papel_tijeras_lagarto_spock as pplsp
from src import Ahorcado
from src import Quiz as q
from src import Tres_en_raya

def menu():
    """
    Muestra el menú principal con las opciones de juegos disponibles.
    """
    print("╔══════════════════════════╗")
    print("║    MENÚ PRINCIPAL        ║")
    print("╠════════════════════════════════════════════╣")
    print("║ 1. Piedra Papel Tijera Lagarto Spock       ║")
    print("║ 2. Ahorcado                                ║")
    print("║ 3. Quiz                                    ║")
    print("║ 4. Tres en Raya                            ║")
    print("║ 5. Salir                                   ║")
    print("╚════════════════════════════════════════════╝")

def main():
    """
    Función principal que gestiona el flujo del menú y la selección de juegos.
    """
    while True:
        menu()
        try:
            juego = int(input("Selecciona un juego (Escribe salir en cualquier momento para salir: "))
            
            if juego == 5:
                print("Escribe salir en cualquier momento para salir")
                break
            elif juego == 1:
                print("Escribe salir en cualquier momento para salir")
                pplsp.Piedra_papel_tijeras_lagarto_spock()
            elif juego == 2:
                print("Escribe salir en cualquier momento para salir")
                ahorcado_instance = Ahorcado.Ahorcado()
                ahorcado_instance.jugar()
            elif juego == 3:
                print("Escribe salir en cualquier momento para salir")
                q.Quiz()
            elif juego == 4:
                print("Escribe salir en cualquier momento para salir")
                Tres_en_raya_instance = Tres_en_raya.Tres_en_raya()
                Tres_en_raya_instance.jugar()
            elif juego == 'salir':
                print("Saliendo del juego...\n")
                break
            else:
                print("\nPor favor ingrese un número entre 1 y 5.")
        except ValueError:
            print("Por favor ingrese un número válido.\n")

if __name__ == "__main__":
    main()


  
 




    


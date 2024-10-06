from src import Piedra_papel_tijeras_lagarto_spock
from src import ahorcado
from src import Quiz   
from src import Tres_en_raya

def menu():
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
    
    while True:
        menu()
        try:
            juego = int(input("Selecciona un juego: "))
        
            if juego == 5:
                print("Gracias por jugar con nosotros, hasta pronto.")
                break
            elif juego == 1:
                Piedra_papel_tijeras_lagarto_spock.juego()
            elif juego == 2:
                ahorcado_instance = ahorcado.Ahorcado()
                ahorcado_instance.juego()
            elif juego == 3:
                Quiz.juego()
            elif juego == 4:
                Tres_en_raya.Tres_en_raya()
            else:
                print("\nPor favor ingrese un número entre 1 y 5.")


        except ValueError:
            print("Por favor ingrese un número entre 1 y 5.\n")


if __name__ == "__main__":
    main()

  
 




    


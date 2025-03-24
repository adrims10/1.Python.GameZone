import random

class Ahorcado:
    def __init__(self):                                               
        self.palabras = ['Pandas', 'sql', 'Python']
        self.palabra = self.elegir_palabra()
        self.letras_adivinadas = set()
        self.intentos_restantes = 10

    def elegir_palabra(self):
        """Elige una palabra aleatoria de la lista."""
        return random.choice(self.palabras)

    def mostrar_estado(self):
        """Muestra el estado actual de la palabra con letras adivinadas y espacios."""
        return ''.join(letra if letra in self.letras_adivinadas else '_' for letra in self.palabra)

    def adivinar_letra(self, letra):
        """Comprueba si la letra introducida está en la palabra y actualiza el estado del juego."""
        if letra == "salir":
            print("Juego terminado por el jugador.")
            exit()

        if letra in self.letras_adivinadas:
            print("Ya has adivinado esa letra. Intenta de nuevo.")
            return False

        self.letras_adivinadas.add(letra)

        if letra not in self.palabra:
            self.intentos_restantes -= 1
            print("Letra incorrecta.")
        else:
            print("¡Letra correcta!")

    def jugar(self):
        """Inicia el juego del ahorcado y gestiona el flujo del mismo."""
        patron_bienvenida = r"""
      .--------------------------------------------------.
     /                                                    \
    |             ¡Bienvenido/a al juego del Ahorcado!      |
    |                                                    |
    |   Disfruta de una experiencia única e interactiva!  |
     \                                                  /
      '--------------------------------------------------'
              \   ^   ^   ^   ^   ^   ^   ^   ^   /
               \__________________________________/
                      \   |   |   |   |   /
                       \__|___|___|___|__/
                
    """
        print(patron_bienvenida)
        print('Pista: Palabras relacionadas con el Bootcamp')
        
        while self.intentos_restantes > 0:
            estado_actual = self.mostrar_estado()
            print(f"Palabra: {estado_actual}")
            print(f'Quedan {self.intentos_restantes} intentos')
            letra = input("Introduce una letra (o escribe 'salir' para terminar el juego): ").lower()

            self.adivinar_letra(letra)

            if all(letra in self.letras_adivinadas for letra in self.palabra):
                print(f"¡Felicidades! Has adivinado la palabra: {self.palabra}")
                print('Has ganado el juego!!!!!')
                n = 5 
                for i in range(n):
                    espacios = ' ' * (n - i - 1)
                    texto = ' '.join(['WIN'] * (i + 1))
                    print(espacios + texto)
                break
        else:
            print(f"Has perdido. La palabra era: {self.palabra}")
            n = 5 
            for i in range(n):
                espacios = ' ' * (n - i - 1)
                texto = ' '.join(['LOSE'] * (i + 1))
                print(espacios + texto)

if __name__ == "__main__":
    Ahorcado()

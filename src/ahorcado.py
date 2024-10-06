import random

class Ahorcado:
    def __init__(self):                                               
        self.palabras = ['hackio','sql','frustrado']
        self.palabra = self.elegir_palabra()
        self.letras_adivinadas = set()
        self.intentos_restantes = 10

    def elegir_palabra(self):
        return random.choice(self.palabras)

    def mostrar_estado(self):
        return ''.join(letra if letra in self.letras_adivinadas else '_' for letra in self.palabra)

    def adivinar_letra(self, letra):
        if letra in self.letras_adivinadas:
            print("Ya has adivinado esa letra. Intenta de nuevo.")
            return False

        self.letras_adivinadas.add(letra)

        if letra not in self.palabra:
            self.intentos_restantes -= 1
            print("Letra incorrecta.")
        else:
            print("¡Letra correcta!")
            

    def juego(self):
        patron = r"""
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
        print(patron)
        
        while self.intentos_restantes > 0:
            estado_actual = self.mostrar_estado()
            print(f"Palabra: {estado_actual}")
            print(f'Quedan {self.intentos_restantes} intentos')
            letra = input("Introduce una letra: ").lower()

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
  
    
preguntas = [
    {
        "pregunta": "¿Cual es la capital de españa?",
        "opcion": ["1.Berlín", "2.París", "3.Madrid", "4.Roma"],
        "respuesta": 3,'tematica':'Cultura General'
    },
    {
        "pregunta": "¿Cual es el numero PI?",
        "opcion": ["1.3,14161718", "2.3", "3.4", "4.5"],
        "respuesta": 1,'tematica':'Cultura General'
    },
    {
        "pregunta": "¿Quien descubrio America '?",
        "opcion": ["1.Jonny walker", "2.Francisco Franco", "3.Rocky Balboa", "4.Cristobal Colon"],
        "respuesta": 4,'tematica':'Historia'
    },{
        "pregunta": "¿En qué año comenzó la Segunda Guerra Mundial?",
        "opcion": ["1.1914", "2.1939", "3.1945", "4.1950"],
        "respuesta": 2,'tematica':'Historia'
    },{
        "pregunta": "¿Cuantas Champions tiene el Real Madrid?",
        "opcion": ["1.10", "2.11", "3.14", "4.15"],
        "respuesta": 4,'tematica':'Actualidad'
    },{
        "pregunta": "¿Como se llama el hijo varon de los simpsoms?",
        "opcion": ["1.Bort", "2.Bert", "3.Adri", "4.Bart"],
        "respuesta": 4,'tematica':'Actualidad'
    },{
        "pregunta": "¿Quién fue el primer presidente de los Estados Unidos?",
        "opcion": ["1.Abraham Lincoln", "2.Thomas Jefferson", "3.Geoge Washington", "4.John Adams"],
        "respuesta": 3,'tematica':'Historia'
    },{
        "pregunta": "¿Cuantas operaciones esteticas se ha realizado belen esteban?",
        "opcion": ["1.Innumerables", "2.1939", "3.1945", "4.1950"],
        "respuesta": 1,'tematica':'Random'
    },{
        "pregunta": "¿De que color era el caballo blanco de santiago?",
        "opcion": ["1.Marron", "2.Toldo", "3.Blanco", "4.Negro"],
        "respuesta": 3,'tematica':'Random'
    },{
        "pregunta": "Oro parece plata no es,¿que es?",
        "opcion": ["1.Paja","2.Platano", "3.Pis", "4.Metamizol"],
        "respuesta": 2,'tematica':'Ramdom'
    }
]

def juego():
    marcador = 0
    for pregunta in preguntas:
        print(pregunta["pregunta"])
        print(f'Esta pregunta es de {pregunta['tematica']}')
        print('---------------------------------------------')
        for opcion in pregunta["opcion"]:
            print(opcion)

        try:
            respuesta_concursante= int(input("Elige una opción (1-4): "))
            if respuesta_concursante == pregunta["respuesta"]:
                print("¡Correcto!")
                print()
                marcador += 1
            else:
                print("Incorrecto. La respuesta correcta era:", pregunta["opcion"][pregunta["respuesta"]-1])
                print("!HAS PERDIDO!")
                break
        except ValueError:
            print("Por favor, introduce un número válido.")
    if marcador == 10:
        print('!HAS GANADO EL JUEGO')

       

if __name__ == "__main__":
   juego()
    
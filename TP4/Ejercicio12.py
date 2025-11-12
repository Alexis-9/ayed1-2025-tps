"""Escribir un programa para crear una lista por comprensión con los naipes de la baraja española. La lista debe contener cadenas de caracteres. Ejemplo: ["1 Oros", "2
Oros"... ]. Imprimir la lista por pantalla. """

def lista_baraja() -> list:
    """
    Genera una lista que representa una baraja española de 48 cartas, sin comodines

    Pre:
    - No recibe parámetros

    Post:
    - Devuelve una lista de cadenas donde cada elemento representa una carta
      en el formato 'número palo', con números del 1 al 12 y palos 'oro', 'basto', 'espada' y 'copa'
    """
    return [f"{x} {i}" for x in range(1,13)  for i in ["oro","basto","espada","copa"]]

print(lista_baraja())
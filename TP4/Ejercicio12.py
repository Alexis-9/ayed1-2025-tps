"""Escribir un programa para crear una lista por comprensión con los naipes de la baraja española. La lista debe contener cadenas de caracteres. Ejemplo: ["1 Oros", "2
Oros"... ]. Imprimir la lista por pantalla. """

def lista_baraja():
     return [f"{x} {i}" for x in range(1,13)  for i in ["oro","basto","espada","copa"]]

print(lista_baraja())
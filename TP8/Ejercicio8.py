"""Generar e imprimir un diccionario donde las claves sean nÃºmeros enteros entre 1 y
20 (ambos incluidos) y los valores asociados sean el cuadrado de las claves.
"""
def cuadrado_claves() -> None:
    """
    Crea un diccionario con números del 1 al 20 como claves y sus cuadrados como valores

    Pre:
    - No recibe parámetros
    - No requiere entrada del usuario

    Post:
    - Genera un diccionario con claves del 1 al 20 y valores iguales al cuadrado de cada clave
    - Imprime el diccionario completo por pantalla
    - No devuelve ningún valor
    """

    diccionario={}
    for i in range(1,21):
        diccionario[i]=i**2

    print(diccionario)

cuadrado_claves()
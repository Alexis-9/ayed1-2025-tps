""" Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas
son recibidas en dos tuplas, por ejemplo: (3, 4) y (5, 4). La función devuelve True
o False. Escribir también un programa para verificar su comportamiento. Considerar
el uso de conjuntos para resolver este ejercicio.
"""

def domino(tup1: tuple, tup2: tuple) -> bool:
    """
    Determina si dos fichas de dominó pueden colocarse una junto a la otra,
    es decir, si comparten al menos un valor

    Pre:
    - tup1 y tup2 son tuplas de longitud 2 que representan fichas de dominó,
      donde cada elemento es una cadena con el valor de un lado de la ficha
    - Los elementos pueden ser números o palabras, pero deben ser comparables por igualdad

    Post:
    - Devuelve True si las fichas comparten al menos un valor
    - Devuelve False si no tienen valores en común
    - No modifica las tuplas originales
    """

    largo = 4

    conjunto1=set(tup1)
    if len(conjunto1)<2:
        largo-=1
    conjunto2=set(tup2)
    if len(conjunto2)<2:
        largo-=1

    return len(conjunto1.union(conjunto2))<largo

print(domino(("uno","dos"),("tres","uno")))
print(domino((1,2),(3,1)))
print(domino((1,2),(3,4)))
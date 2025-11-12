"""Escribir una función que reciba dos vectores en forma de tuplas y devuelva un valor
de verdad indicando si son ortogonales o no. Desarrollar también un programa que
permita verificar el comportamiento de la función. """

def ortogonal(tup1: tuple[int, int], tup2: tuple[int, int]) -> bool:
    """
    Determina si dos vectores  son ortogonales

    Pre:
    - tup1 y tup2 son tuplas de dos números enteros o reales que representan vectores
    - Ambos vectores deben tener longitud 2

    Post:
    - Devuelve True si el producto escalar entre los vectores es igual a 0
    - Devuelve False en caso contrario
    - No modifica los valores originales de las tuplas
    """

    return (tup1[0]*tup2[0] + tup1[1]*tup2[1])==0

print(ortogonal((2,3),(-3,2)))
print(ortogonal((4,3),(-3,2)))
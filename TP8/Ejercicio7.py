"""Definir un conjunto con números enteros entre 0 y 9. Luego solicitar valores al
usuario y eliminarlos del conjunto mediante el método remove, mostrando el contenido del conjunto luego de cada eliminación.
Finalizar el proceso al ingresar -1.
Utilizar manejo de excepciones para evitar errores al intentar quitar elementos
inexistentes.
"""
def conjunto_remove() -> None:
    """
    Permite al usuario eliminar elementos de un conjunto de enteros del 0 al 9

    Pre:
    - No recibe parámetros
    - El usuario debe ingresar números enteros
    - Ingresar -1 termina el proceso

    Post:
    - Muestra por pantalla el conjunto actualizado después de cada intento de eliminación
    - Elimina el elemento del conjunto si existe
    - Informa al usuario si se ingresa un valor no entero o si el elemento no está en el conjunto
    - No devuelve ningún valor
    """

    conjunto={0,1,2,3,4,5,6,7,8,9}

    while True:
        try:
            print(conjunto)
            n=int(input("Ingrese el valor a eliminar (-1 para terminar): "))
            if n==-1:
                break
            conjunto.remove(n)
        except ValueError:
            print("Debe ingresar un número entero")
        except KeyError:
            print("Ese elemento no existe en el conjunto")

conjunto_remove()
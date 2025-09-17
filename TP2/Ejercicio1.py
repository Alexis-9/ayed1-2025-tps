"""1. Desarrollar cada una de las siguientes funciones y escribir un programa que permita verificar su funcionamiento imprimiendo la lista luego de invocar a cada función:

a. Cargar una lista con números al azar de cuatro dígitos. La cantidad de elementos también será un número al azar de dos dígitos.

b. Calcular y devolver el producto de todos los elementos de la lista anterior.

c. Eliminar todas las apariciones de un valor en la lista anterior.
El valor a eliminar se ingresa desde el teclado y la función lo recibe como parámetro.
No utilizar listas auxiliares.

d. Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas auxiliares.
Un ejemplo de lista capicúa es [50, 17, 91, 17, 50]."""

import random as rn
def cargar_lista() -> list[int]:
    """
    Genera una lista de números aleatorios de 4 dígitos

    pre: No recibe nada

    post: Devuelve una lista de entre 10 a 99 elementos elegidos aleatoriamente, los elementos son números enteros de 4 digitos elegidos aleatoriamente
    """
    return [rn.randint(1000,9999) for i in range(rn.randint(10,99) )]


def producto_lista(lista: list[int]) -> int:
    """
    Calcula el producto de todos los elementos de una lista de enteros

    pre: lista como lista de números enteros

    post: Devuelve un número entero que es el producto de todos los elementos de la lista
    """
    total = 1
    for producto in lista:
        total *= producto
    return total


def eliminar_valor(lista: list[int], numero: int) -> list[int]:
    """
    Elimina todas las veces que aparece un valor en una lista de enteros

    pre:
    - lista como lista de números enteros
    - numero como número entero a eliminar de la lista

    post: Devuelve la lista sin el número a eliminar
    """
    i = 0
    while i < len(lista):
        if lista[i] == numero:
            lista = lista[:i] + lista[i + 1:]
        else:
            i += 1
    return lista

def es_capicua(lista: list[int]) -> bool:
    """
    Verifica si una lista es capicúa

    pre: lista como lista de números enteros

    post: Devuelve True si la lista es capicúa o False en caso contrario
    """
    largo = len(lista)//2
    for i in range(largo):
        if lista[i] != lista[-(i+1)]:
            return False
    return True

def main()-> None:
    """
    Crea una lista vacia, invoca el resto de funciones e imprime sus resultados
    pre: No recibe nada
    post: Imprime las funciones
    """
    lista = [1,2,2,3]
    print(f"La lista es: {lista}")

    print(f"El producto de todos los elementos de la lista es: {producto_lista(lista)}")
    if es_capicua(lista):
        print("La lista es capicúa")
    else:
        print("La lista no es capicúa")

    n_eliminar = int(input("Ingrese el numero que desea eliminar: "))
    lista=eliminar_valor(lista,n_eliminar)
    print(f"La lista sin {n_eliminar} es: {lista}")

    if es_capicua(lista):
        print("La lista es capicúa")
    else:
        print("La lista no es capicúa")

main()
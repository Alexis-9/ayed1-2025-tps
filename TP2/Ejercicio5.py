"""Escribir una función que reciba una lista como parámetro y devuelva True si la lista
está ordenada en forma ascendente o False en caso contrario. Por ejemplo,
ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False. Desarrollar
además un programa para verificar el comportamiento de la función."""
import random as rn
from string import ascii_lowercase

def orden_ascendente(lista: list[int]) -> bool:
    """
    Verifica si una lista está ordenada en orden ascendente

    Pre: lista de números enteros

    Post: Devuelve True si la lista está ordenada de menor a mayor y False en caso contrario
    """
    return lista==sorted(lista)

def probar_lista(lista: list[int]) -> None:
    """
    Imprime si una lista está ordenada o no y muestra la lista ordenada

    Pre: lista de números enteros

    Post:
    - Imprime si la lista está o no en orden ascendente
    - Imprime la lista ordenada de forma ascendente si no lo estaba previamente
    """
    if orden_ascendente(lista):
        print(f"La lista {lista} está ordenada de forma ascendente")
    else:
        print(f"La lista {lista} no está ordenada de forma ascendente")
        lista_ordenada = sorted(lista)
        print(f"La lista {lista_ordenada} estaría ordenada de forma ascendente\n")



def main() -> None:
    """
    Genera dos listas de prueba y muestra si están ordenadas, junto con su versión ordenada

    Pre: No recibe nada

    Post: Llama a las funciones para comprobar si la lista esta ordenada en una lista de números y otra de letras
    """
    lista_de_prueba = [rn.randint(1,99) for x in range(10)]
    probar_lista(lista_de_prueba)

    lista_de_prueba = [rn.choice(ascii_lowercase) for i in range(10)]
    probar_lista(lista_de_prueba)
main()
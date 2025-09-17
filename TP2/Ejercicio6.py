"""Escribir una función que reciba una lista de números enteros como parámetro y la
normalice, es decir que todos sus elementos deben sumar 1.0, respetando las proporciones relativas que cada elemento tiene en la lista original. Desarrollar también
un programa que permita verificar el comportamiento de la función.
Por ejemplo, normalizar([1, 1, 2]) debe devolver [0.25, 0.25, 0.50]."""
import random as rn

def normalizar(lista: list[int]) -> list[float]:
    """
    Normaliza una lista de números

    Pre: lista de lista de números enteros

    Post: Devuelve la lista modificada donde la suma de los elementos es 1
    """
    total=sum(lista)
    for i,x in enumerate(lista):
        lista[i]=x/total
    return lista


def main() -> None:
    """
    Genera una lista de números aleatorios, la normaliza y muestra los resultados.

    Pre: No recibe nada

    Post:
    - Imprime la lista original.
    - Imprime la lista normalizada
    - Imprime la suma de los elementos normalizados
    """
    lista = [rn.randint(1, 10) for i in range(5)]

    print(f"La lista original es {lista}")
    lista_normalizada = normalizar(lista)
    print(f"La Lista normalizada es {lista_normalizada}")
    print(f"La suma de los elementos: {sum(lista_normalizada)}")

main()

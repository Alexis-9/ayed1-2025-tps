"""2. Escribir funciones para:
a. Generar una lista de N números aleatorios del 1 al 100.  El valor de N se ingresa a través del teclado.

b. Recibir una lista como parámetro y devolver True si la misma contiene algún elemento repetido. La función no debe modificar la lista.

c. Recibir una lista como parámetro y devolver una nueva lista con los elementos únicos de la lista original, sin importar el orden.

Combinar estas tres funciones en un mismo programa."""

import random as rn

def generar_lista() -> list[int]:
    """
    Genera una lista de n números enteros aleatorios entre 1 y 10

    Pre: Se solicita al usuario la cantidad de números a generar

    Post: Devuelve una lista de n números enteros aleatorios entre 1 y 10
    """
    n=int(input("Cuantos números desea generar en la lista: "))
    return [rn.randint(1,10) for x in range(n)]

def buscar_repetido(lista: list[int]) -> bool:
    """
    Verifica si una lista contiene elementos repetidos

    pre: lista como lista de números enteros.

    post:
    - Devuelve True si hay al menos un valor que se repite
    - Devuelve False si todos los elementos son únicos
    """
    for indice,valor in enumerate(lista):
        for indice2,valor2 in enumerate(lista):
            if valor==valor2 and indice!=indice2:
                return True
    return False

def lista_unica(lista: list[int]) -> list[int]:
    """
    Elimina los elementos duplicados de una lista, manteniendo el orden original

    pre: lista de números enteros

    Post: Devuelve una nueva lista con los elementos únicos de la lista original
    """
    nueva=[]
    for numero in lista:
        if numero not in nueva:
            nueva.append(numero)
    return nueva

def main() -> None:
    """
    Genera una lista aleatoria de números, elimina duplicados si existen
    y muestra los resultados.

    Pre: No recibe nada

    Post: Imprime la lista generada, si tiene elementos repetidos los elimina e imprime nuevamente la lista pero sin los repetidos
    """
    lista=generar_lista()
    print(f"La lista es {lista}")
    if buscar_repetido(lista):
        print("Se borran elementos repetidos")
        lista_nueva=lista_unica(lista)
        print(f"La nueva lista es {lista_nueva}")

main()
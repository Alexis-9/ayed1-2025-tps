"""Generar una lista con números al azar entre 1 y 100 y crear una nueva lista con los
elementos de la primera que sean impares. El proceso deberá realizarse utilizando
la función filter(). Imprimir las dos listas por pantalla."""
import random as rn

def generar_lista() -> list[int]:
    """
    Genera una lista de números enteros aleatorios entre 1 y 100

    Pre: El usuario ingresa un número entero

    Post: Devuelve una lista de tamaño n con números enteros aleatorios entre 1 y 100
    """
    n=int(input("Cuantos números desea generar: "))
    return [rn.randint(1,100) for x in range(n)]

def main() -> None:
    """
    Genera una lista de números aleatorios entre 1 y 100, imprime la lista completa
    y luego imprime solo los números impares

    Pre: No recibe nada

    Post:
    - Imprime la lista generada
    - Imprime una lista con los números impares de la lista generada
    """
    lista = generar_lista()
    print(lista)
    print(list(filter(lambda x: x % 2 != 0, lista)))

main()

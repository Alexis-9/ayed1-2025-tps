"""Desarrollar un programa para rellenar una matriz de N x N con números enteros al
azar comprendidos en el intervalo [0,N2), de tal forma que ningún número se repita. Imprimir la matriz por pantalla."""

import random as rn


def generar_matriz_azar(n: int) -> list:
    """
    Genera una matriz cuadrada de tamaño n x n con números aleatorios sin repetir

    Pre:
    - Recibe un número entero positivo n que indica el tamaño de la matriz
    - Debe haberse importado el módulo random como rn

    Post:
    - Devuelve una lista de listas que representa la matriz con valores enteros únicos
    """

    matriz = []
    usados=[]
    for i in range(n):
        fila = []
        while len(fila) < n:
            num = rn.randint(0, n * n - 1)
            if num not in usados:
                fila.append(num)
                usados.append(num)
        matriz.append(fila)
    return matriz

def main() -> None:
    """
    Permite al usuario ingresar el tamaño de la matriz, genera una matriz aleatoria y la muestra por pantalla

    Pre:
    - El usuario debe ingresar un número entero positivo (n) válido

    Post:
    - Muestra por consola la matriz generada de tamaño n x n con números aleatorios sin repetir
    """
    n = int(input("Ingrese el tamaño N de la matriz: "))
    matriz = generar_matriz_azar(n)
    print("Matriz generada:")
    for fila in matriz:
        print(fila)


if __name__ == '__main__':
    main()

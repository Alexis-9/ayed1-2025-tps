"""Desarrollar un programa para rellenar una matriz de N x N con números enteros al
azar comprendidos en el intervalo [0,N2), de tal forma que ningún número se repita. Imprimir la matriz por pantalla."""

import random as rn


def generar_matriz_azar(n):
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

def main():
    n = int(input("Ingrese el tamaño N de la matriz: "))
    matriz = generar_matriz_azar(n)
    print("Matriz generada:")
    for fila in matriz:
        print(fila)


if __name__ == '__main__':
    main()

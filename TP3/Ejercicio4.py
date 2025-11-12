import random as rn

def crear_matriz() -> list:
    """
    Crea una matriz con valores aleatorios de producción de fábricas durante 7 días de la semana

    Pre: No recibe parámetros, solo solicita al usuario un número entero positivo mayor que 0
    Post: Devuelve una matriz de tamaño n x 7 con valores enteros aleatorios entre 0 y 150
    """
    while True:
        try:
            n=int(input("Ingrese cuantas filas y columnas tendra la matriz: "))
            if n>0:
                break
            else:
                print("Debe ingresar un valor mayor a 0")
        except ValueError:
            print("Debe ingresar un número entero")

    matriz = []
    for i in range(n):
        fila = []
        for j in range(7):
            fila.append(rn.randint(0, 150))
        matriz.append(fila)

    for i, fila in enumerate(matriz):
        print(f"Fabrica {i + 1} {fila}")

    return matriz


def bicicletas_por_fabrica(matriz: list) -> None:
    """
    Calcula y muestra la cantidad total de bicicletas producidas por cada fábrica en la semana

    Pre: recibe una matriz de tamaño n x 7 con valores enteros que representan la producción diaria de cada fábrica
    Post: muestra por pantalla la producción total semanal de cada fábrica
    """
    fabricas=[]
    total=0
    for i in range(len(matriz)):
        for j in range(7):
           total+=matriz[i][j]
        fabricas.append(total)
        total=0

    for i,x in enumerate(fabricas):
        print(f"La fábrica {i+1} produjo {x} bicicletas")


def mayor_en_un_dia(matriz: list) -> None:
    """
    Determina qué fábrica produjo la mayor cantidad de bicicletas en un solo día y en qué día ocurrió

    Pre: recibe una matriz de tamaño n x 7 con valores enteros que representan la producción diaria de cada fábrica
    Post: muestra por pantalla la fábrica y el día con mayor producción individual
    """
    dias = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
    mayor=0
    fabrica=0
    dia=0
    for i in range(len(matriz)):
        for j in range(7):
            if matriz[i][j]>mayor:
                mayor=matriz[i][j]
                fabrica=i
                dia=j

    print(f"La fabrica {fabrica+1} fue la que más produjo en la semana y fue en el día {dias[dia].title()}")


def dia_mas_productivo(matriz: list) -> None:
    """
    Determina qué día de la semana tuvo la mayor producción total sumando todas las fábricas

    Pre: recibe una matriz de tamaño n x 7 con valores enteros que representan la producción diaria de cada fábrica
    Post: muestra por pantalla el día más productivo y la cantidad total de bicicletas producidas ese día
    """
    dias = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
    mayor=0
    total=0
    dia=0
    for i in range(7):
        for j in range(len(matriz)):
            total+=matriz[j][i]
        if total>mayor:
            mayor=total
            dia=i
        total=0

    print(f"El dìa más productivo fue el {dias[dia]} con {mayor} bicicletas")

def dia_por_fabrica(matriz: list) -> None:
    """
    Muestra el día con menor producción de cada fábrica

    Pre: recibe una matriz de tamaño n x 7 con valores enteros que representan la producción diaria de cada fábrica
    Post: muestra por pantalla la menor cantidad de bicicletas producidas por cada fábrica en la semana
    """
    menor=[min(fabrica) for fabrica in matriz]
    for fab,dia in enumerate(menor):
        print(f"El día con menor producción de la fábrica {fab+1} produjo {dia} bicicletas")

def main() -> None:
    """
    Función principal que ejecuta todas las funciones

    Pre: no recibe parámetros
    Post: genera la matriz de producción y ejecuta todas las funciones
    """
    matriz=crear_matriz()
    print()
    bicicletas_por_fabrica(matriz)
    print()
    mayor_en_un_dia(matriz)
    print()
    dia_mas_productivo(matriz)
    print()
    dia_por_fabrica(matriz)

if __name__ == '__main__':
    main()
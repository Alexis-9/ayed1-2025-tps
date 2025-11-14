#Punto a
def punto_a(n: int) -> None:
    """
    Genera y muestra una matriz n x n donde la diagonal principal tiene números impares consecutivos y el resto ceros

    Pre:
    - Recibe un número entero n
    - n representa la cantidad de filas y columnas de la matriz

    Post:
    - Crea una matriz cuadrada con un patrón específico
    - Muestra la matriz por pantalla
    - No devuelve ningún valor
    """

    matriz=[]
    num=1
    for i in range(n):
        fila=[]
        for j in range(n):
            if i==j:
                fila.append(num)
                num+=2
            else:
                fila.append(0)
        matriz.append(fila)

    for fila in matriz:
        print(fila)



#Punto b
def punto_b(n: int) -> None:
    """
    Genera y muestra una matriz n x n donde la diagonal secundaria contiene potencias de 3 en orden descendente y el resto ceros

    Pre:
    - Recibe un número entero n
    - n representa la cantidad de filas y columnas de la matriz

    Post:
    - Crea una matriz cuadrada con un patrón específico
    - Muestra la matriz por pantalla
    - No devuelve ningún valor
    """
    matriz=[]
    num=3**(n-1)
    for i in range(n):
        fila=[]
        for j in range(n):
            if j==n-1-i:
                fila.append(num)
                num//=3
            else:
                fila.append(0)
        matriz.append(fila)

    for fila in matriz:
        print(fila)


#Punto c
def punto_c(n: int) -> None:
    """
    Genera y muestra una matriz n x n tipo escalera con valores decrecientes y el resto ceros

    Pre:
    - Recibe un número entero n
    - n representa la cantidad de filas y columnas de la matriz

    Post:
    - Crea una matriz cuadrada con un patrón específico
    - Muestra la matriz por pantalla
    - No devuelve ningún valor
    """
    matriz = []
    num=n
    for i in range(n):
        fila = []
        for j in range(n):
            if i >= j:
                fila.append(num)
            else:
                fila.append(0)
        num -= 1
        matriz.append(fila)

    for fila in matriz:
        print(fila)


#Punto d
def punto_d(n: int) -> None:
    """
    Genera y muestra una matriz n x n donde cada fila tiene un mismo número y ese valor se va dividiendo por 2 en cada fila

    Pre:
    - Recibe un número entero n
    - n representa la cantidad de filas y columnas de la matriz

    Post:
    - Crea una matriz cuadrada con un patrón específico
    - Muestra la matriz por pantalla
    - No devuelve ningún valor
    """
    matriz = []
    num = 2**(n-1)
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(num)
        matriz.append(fila)
        num //= 2

    for fila in matriz:
        print(fila)


#Punto e
def punto_e(n: int) -> None:
    """
    Genera y muestra una matriz n x n donde solo se rellenan con números consecutivos las posiciones cuya suma de índices es impar

    Pre:
    - Recibe un número entero n
    - n representa la cantidad de filas y columnas de la matriz

    Post:
    - Crea una matriz cuadrada con un patrón específico
    - Muestra la matriz por pantalla
    - No devuelve ningún valor
    """
    matriz = []
    num = 1
    for i in range(n):
        fila = []
        for j in range(n):
            if (i+j) % 2 != 0:
                fila.append(num)
                num += 1
            else:
                fila.append(0)
        matriz.append(fila)

    for fila in matriz:
        print(fila)



#Punto f
def punto_f(n: int) -> None:
    """
    Genera y muestra una matriz n x n tipo escalera invertida y el resto con ceros

    Pre:
    - Recibe un número entero n
    - n representa la cantidad de filas y columnas de la matriz

    Post:
    - Crea una matriz cuadrada con un patrón específico
    - Muestra la matriz por pantalla
    - No devuelve ningún valor
    """
    matriz = []
    num = 1

    for i in range(n):
        fila = []
        for j in range(n):
            if j<=i:
                fila.append(num)
                num += 1
            else:
                fila.append(0)
        fila.reverse()
        matriz.append(fila)

    for fila in matriz:
        print(fila)

#Punto g
def punto_g(n: int) -> None:
    """
    Genera y muestra una matriz n x n espiralada

    Pre:
    - Recibe un número entero n
    - n representa la cantidad de filas y columnas de la matriz

    Post:
    - Crea una matriz cuadrada con un patrón específico
    - Muestra la matriz por pantalla
    - No devuelve ningún valor
    """
    matriz=[]
    for i in range(n):
        fila=[]
        for j in range(n):
            fila.append(0)
        matriz.append(fila)

    num=1
    inicio=0
    fin=n-1

    while inicio<=fin:
        for arriba in range(inicio,n-inicio):
            matriz[inicio][arriba]=num
            num+=1

        for derecha in range(inicio+1, fin+1):
            matriz[derecha][fin]=num
            num+=1

        for abajo in range(inicio+1, fin):
            fin2=n-1-abajo
            matriz[fin][fin2]=num
            num+=1

        for izquierda in range(inicio+1, fin+1):
            fin2=n-izquierda
            matriz[fin2][inicio]=num
            num+=1

        inicio+=1
        fin-=1

    for fila in matriz:
        print(fila)

#Punto h
def punto_h(n: int) -> None:
    """
    Genera y muestra una matriz n x n llena por diagonales, de arriba a la izquierda hacia abajo a la derecha


    Pre:
    - Recibe un número entero n
    - n representa la cantidad de filas y columnas de la matriz

    Post:
    - Crea una matriz cuadrada con un patrón específico
    - Muestra la matriz por pantalla
    - No devuelve ningún valor
    """

    print("No la pude hacer")

#Punto i
def punto_i(n: int) -> None:
    print("No la pude hacer")

def main() -> None:
    """
    Permite al usuario elegir y ejecutar diferentes patrones de matrices nxn

    Pre:
    - No recibe parámetros
    - Pide al usuario que ingrese un número entero n mayor a 0 para el tamaño de las matrices
    - Pide al usuario que elija qué patrón ejecutar

    Post:
    - Ejecuta la función relacionada al patrón elegido pasando n como tamaño de la matriz
    - Muestra cada matriz por pantalla
    - Permite repetir la elección hasta que el usuario ingrese 0
    - No devuelve ningún valor
    """
    opciones = {
        "a": punto_a,
        "b": punto_b,
        "c": punto_c,
        "d": punto_d,
        "e": punto_e,
        "f": punto_f,
        "g": punto_g,
        "h": punto_h,
        "i": punto_i
    }

    while True:
        try:
            n = int(input("Ingrese de cuantas filas y columnas sera la matriz: "))
            if n<0:
                print("Debe ser un número mayor a 0")
            else:
                break
        except ValueError:
            print("Debe ingresar un número entero")

    while True:
        print("\nSeleccione el patrón que desea ver:")
        for key in opciones:
            print(f"{key}: Patrón {key}")
        print("0: Salir")

        opcion = input("Ingrese su opción: ").strip()

        if opcion == "0":
            break
        elif opcion in opciones:
            print(f"=========== PATRÓN {opcion} ===========")
            opciones[opcion](n)
            print("========================================")
            input("ENTER para continuar al menú")
        else:
            print("Opción incorrecta")

if __name__ == '__main__':
    main()
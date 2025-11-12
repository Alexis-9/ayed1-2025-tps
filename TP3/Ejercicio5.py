import random as rn

def generar_matriz() -> list:
    """
    Genera una matriz de tamaño n x m inicializada con ceros

    Pre: Pide al usuario los valores de n y m
    Post: devuelve una matriz de tamaño n x m con todos los elementos inicializados en 0
    """
    while True:
        try:
            n = int(input("Ingrese cuantas filas tendra la matriz: "))
            m = int(input("Ingrese cuantas columnas tendra la matriz: "))
            if n > 0 and m>0:
                break
            else:
                print("Debe ingresar valores mayores a 0")
        except ValueError:
            print("Debe ingresar un número entero")


    matriz=[]
    for i in range(n):
        fila=[]
        for j in range(m):
            fila.append(0)
        matriz.append(fila)
    return matriz

def mostrar_butacas(matriz: list) -> None:
    """
    Muestra por pantalla la disposición de las butacas de la matriz

    Pre: recibe una matriz de tamaño n x m con valores enteros que representan el estado de cada butaca
    Post: imprime cada fila de la matriz por pantalla, no devuelve ningún valor
    """
    for fila in matriz:
        print(fila)

def reservar(matriz: list) -> bool:
    """
    Permite al usuario reservar una butaca en la matriz y muestra un ejemplo numerado de todas las butacas

    Pre:
    - Recibe una matriz de tamaño n x m con valores 0 (libre) o 1 (ocupada)
    - La matriz debe estar inicializada previamente

    Post:
    - Muestra por pantalla los números de todas las butacas
    - Solicita al usuario el número de la butaca que desea reservar
    - Si la butaca está libre, la marca como ocupada (1) y la muestra
    - Devuelve True si la reserva se realizó con éxito, False en caso contrario
    """
    print("\nNúmeros de las butacas")
    ejemplo=[fila[:] for fila in matriz]

    num=1
    for i in range(len(ejemplo)):
        for j in range(len(ejemplo[i])):
            ejemplo[i][j]=num
            num+=1
    mostrar_butacas(ejemplo)


    while True:
        try:
            butaca = int(input("Ingrese el número de la que butaca desea reservar: "))-1
            if butaca>=0 and butaca<num-1:
                break
            else:
                print("Debe ingresar un número de butaca")
        except ValueError:
            print("Debe ingresar un número entero")

    nfila = 0

    while butaca>len(matriz[0]):
        butaca-=len(matriz[0])
        nfila+=1

    if not matriz[nfila][butaca]:
        print("\nButaca reservada")
        matriz[nfila][butaca]=1
        mostrar_butacas(matriz)

        return True

    else:
        print("No se pudo reservar la butaca")
        return False



def cargar_sala(matriz: list) -> None:
    """
    Llena la matriz de butacas con valores aleatorios 0 (libre) o 1 (ocupada) y muestra la sala

    Pre:
    - Recibe una matriz de tamaño n x m ya creada
    - La matriz puede estar inicializada en cualquier estado

    Post:
    - Cada elemento de la matriz se asigna aleatoriamente a 0 o 1
    - Muestra la matriz resultante por pantalla
    - No devuelve ningún valor
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j]=rn.randint(0,1)
    mostrar_butacas(matriz)


def butacas_libres(matriz: list) -> None:
    """
    Cuenta y muestra la cantidad de butacas libres en la sala

    Pre:
    - Recibe una matriz de tamaño n x m con valores 0 (libre) o 1 (ocupada)

    Post:
    - Calcula cuántas butacas están libres
    - Muestra por pantalla la cantidad de butacas desocupadas
    - No devuelve ningún valor
    """
    desocupadas=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if not matriz[i][j]:
                desocupadas+=1
    print(f"Hay {desocupadas} butacas desocupadas")


def butacas_contiguas(matriz: list) -> None:
    """
    Encuentra y muestra la secuencia más larga de butacas libres en la sala

    Pre:
    - Recibe una matriz de tamaño n x m con valores 0 (libre) o 1 (ocupada)

    Post:
    - Calcula la secuencia más larga de butacas libres consecutivas
    - Muestra por pantalla la cantidad de butacas libres en esa secuencia, la fila y la posición inicial
    - Si no hay butacas libres, indica que no existen
    - No devuelve ningún valor
    """
    mayor=0
    secuencia=0
    fila=0
    posicion=0
    num=0
    butaca=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
           num+=1
           if not matriz[i][j]:
               secuencia+=1
               if secuencia>mayor:
                   mayor=secuencia
                   fila=i
                   posicion=j-secuencia
                   butaca=num-secuencia
           else:
               secuencia=0
        secuencia=0

    if mayor:
        print(f"La secuencia más larga de butacas libres es de {mayor}")
        print(f"Esta en la fila {fila+1} y empieza en la butaca {posicion+2} de esa fila o la butaca {butaca+1} del total")
    else:
        print("No hay butacas libres")


def main() -> None:
    """
    Función principal que gestiona la reserva de butacas y el análisis de la sala

    Pre:
    - No recibe parámetros
    - Las funciones generar_matriz, cargar_sala, reservar, butacas_libres y butacas_contiguas deben estar definidas previamente

    Post:
    - Genera la matriz de butacas
    - Carga aleatoriamente el estado de la sala
    - Permite reservar una butaca
    - Muestra la cantidad de butacas libres
    - Muestra la secuencia más larga de butacas libres
    - No devuelve ningún valor
    """
    matriz=generar_matriz()
    print("Sala cargada")
    cargar_sala(matriz)

    reservar(matriz)
    print()

    butacas_libres(matriz)
    butacas_contiguas(matriz)


if __name__ == '__main__':
    main()
"""Desarrollar cada una de las siguientes funciones y escribir un programa que permita verificar su funcionamiento,
imprimiendo la matriz luego de invocar a cada función:
a. Cargar números enteros en una matriz de N x N, ingresando los datos desde
teclado.
b. Ordenar en forma ascendente cada una de las filas de la matriz.
c. Intercambiar dos filas, cuyos números se reciben como parámetro.
d. Intercambiar dos columnas dadas, cuyos números se reciben como parámetro.
e. Trasponer la matriz sobre si misma. (intercambiar cada elemento Aij por Aji)
f. Calcular el promedio de los elementos de una fila, cuyo número se recibe como
parámetro.
g. Calcular el porcentaje de elementos con valor impar en una columna, cuyo número se recibe como parámetro.
h. Determinar si la matriz es simétrica con respecto a su diagonal principal.
i. Determinar si la matriz es simétrica con respecto a su diagonal secundaria.
j. Determinar qué columnas de la matriz son palíndromos (capicúas), devolviendo
una lista con los números de las mismas.
NOTA: El valor de N debe leerse por teclado. Las funciones deben servir cualquiera
sea el valor ingresado."""

def cargar_matriz(n):
    matriz=[]
    for i in range(n):
        fila=[]
        for j in range(n):
            num=int(input(f"Ingrese el número para la fila {i+1} y columna {j+1}: "))
            fila.append(num)
        matriz.append(fila)

    print()
    for fila in matriz:
        print(fila)


    return matriz

def filas_ascendentes(matriz):
    print("\nTodas las filas en orden ascendente: ")

    for i in range(len(matriz)):
        for j in range(len(matriz[i])-1):
            if matriz[i][j] > matriz[i][j+1]:
                matriz[i][j],matriz[i][j+1]=matriz[i][j+1],matriz[i][j]

    print()
    for fila in matriz:
        print(fila)

def intercambiar_filas(matriz):
    if len(matriz)<=1:
        print("No hay filas suficientes")
        return

    for fila in matriz:
        print(fila)
    print("Qué dos filas desea intercambiar: ")
    fila1=int(input("Fila 1: "))-1
    fila2=int(input("Fila 2: "))-1

    while fila1>len(matriz) or fila2>len(matriz):
        print("Error")
        fila1 = int(input("Fila 1: ")) - 1
        fila2 = int(input("Fila 2: ")) - 1

    matriz[fila1],matriz[fila2]=matriz[fila2],matriz[fila1]

    print()
    for fila in matriz:
        print(fila)

def intercambiar_columnas(matriz):
    if len(matriz)<=1:
        print("No hay columnas suficientes")
        return

    for fila in matriz:
        print(fila)
    print("Qué dos columnas desea intercambiar: ")
    col1 = int(input("Columna 1: ")) - 1
    col2 = int(input("Columna 2: ")) - 1
    while col1>len(matriz) or col2>len(matriz):
        print("Error")
        col1 = int(input("Fila 1: ")) - 1
        col2 = int(input("Fila 2: ")) - 1

    for i in range(len(matriz[0])):
        matriz[i][col1],matriz[i][col2]=matriz[i][col2],matriz[i][col1]

    print()
    for fila in matriz:
        print(fila)


def trasponer_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(i+1, len(matriz)):
            matriz[i][j], matriz[j][i] = matriz[j][i], matriz[i][j]

    print(f"La matriz traspuesta es: ")
    for fila in matriz:
        print(fila)

def promedio_fila(matriz):
    if len(matriz)<1:
        print("No hay filas suficientes")
        return
    print()
    for fila in matriz:
        print(fila)

    nfila=int(input("Número de la fila que quiere ver el promedio: "))-1
    while nfila > len(matriz):
        print("Error")
        nfila=int(input("Número de la fila que quiere ver el promedio: "))-1

    total=0

    for i in range(len(matriz)):
        total+= matriz[nfila][i]

    promedio= total / len(matriz)

    print(matriz[nfila])
    print(f"El promedio es {promedio}")

def porcentaje_impares(matriz):
    if len(matriz)<1:
        print("No hay columnas suficientes")
        return
    print()
    for fila in matriz:
        print(fila)
    ncolumna = int(input("Número de la columna que quiere ver el promedio de impares: ")) - 1
    while ncolumna > len(matriz):
        print("Error")
        ncolumna = int(input("Número de la columna que quiere ver el promedio de impares: ")) - 1
    impar=0

    for i in range(len(matriz)):
        if matriz[i][ncolumna] %2 !=0:
            impar+=1


    porcentaje= impar / len(matriz) *100

    columna=[]
    for i in range(len(matriz)):
        columna.append(matriz[i][ncolumna])

    print(f"La columna {ncolumna+1} es {columna}")
    print(f"Su porcentaje de impares es {porcentaje}%")

def simetrica_diagonal_principal(matriz):
    fin=len(matriz)-1
    capicua=True
    diagonal = []

    for i in range(len(matriz)):
        if matriz[i][i] != matriz[fin][fin]:
            capicua=False
        diagonal.append(matriz[i][i])
        fin -= 1

    print(f"La matriz es: ")
    for fila in matriz:
        print(fila)

    if capicua==True:
        print(f"Su diagonal principal {diagonal} es capicua")
    else:
        print(f"Su diagonal principal {diagonal} no es capicua")


def simetrica_diagonal_secundaria(matriz):
    fin=len(matriz)-1
    capicua=True
    diagonal = []

    for i in range(len(matriz)):
        if matriz[i][fin] != matriz[fin][i]:
            capicua=False
        diagonal.append(matriz[i][fin])
        fin -= 1

    print(f"La matriz es: ")
    for fila in matriz:
        print(fila)

    if capicua == True:
        print(f"Su diagonal secundaria {diagonal} es capicua")
    else:
        print(f"Su diagonal secunadaria {diagonal} no es capicua")



def columnas_capicua(matriz):
    listas=[]
    indices=[]
    for i in range(len(matriz)):
        lista=[]
        for j in range(len(matriz)):
            lista.append(matriz[j][i])
            indice=matriz[j]
        if lista==lista[::-1]:
            listas.append(lista)
            indices.append(indice)

    print(f"La matriz es: ")
    for fila in matriz:
        print(fila)

    if listas:
        print(f"Las columnas capicuas son:")
        for i,x in enumerate(listas):
            print(f"La columna {i+1} {x}")
    else:
        print("No hay columnas capicuas")

def main():
    menu =["","0. Salir","1. Filas ascendentes","2. Intercambiar filas","3. Intercambiar columnas","4. Trasponer matriz","5. Promedio por fila","6. Porcentaje de impares","7. Simétrica diagonal principal","8. Simétrica diagonal secundaria","9. Columnas capicúas"]
    opciones = {
        "1": filas_ascendentes,
        "2": intercambiar_filas,
        "3": intercambiar_columnas,
        "4": trasponer_matriz,
        "5": promedio_fila,
        "6": porcentaje_impares,
        "7": simetrica_diagonal_principal,
        "8": simetrica_diagonal_secundaria,
        "9": columnas_capicua
    }

    n = int(input("De cuanto por cuanto será la matriz: "))
    matriz=cargar_matriz(n)
    for opcion in menu:
        print(opcion)

    while True:
        op = input("\nElija una opción(-1 para ver las opciones): ")

        if op=="0":
            break
        elif op=="-1":
            for opcion in menu:
                print(opcion)
        elif op in opciones:
            opciones[op](matriz)  # Llama a la función correspondiente
        else:
            print("Opción invalida")




if __name__ == '__main__':
    main()

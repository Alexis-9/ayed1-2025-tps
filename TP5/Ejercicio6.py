"""El método index permite buscar un elemento dentro de una lista, devolviendo la
posición que éste ocupa. Sin embargo, si el elemento no pertenece a la lista se
produce una excepción de tipo ValueError. Desarrollar un programa que cargue
una lista con números enteros ingresados a través del teclado (terminando con -1)
y permita que el usuario ingrese el valor de algunos elementos para visualizar la
posición que ocupan, utilizando el método index. Si el número no pertenece a la
lista se imprimirá un mensaje de error y se solicitará otro para buscar. Abortar el
proceso al tercer error detectado. No utilizar el operador in durante la búsqueda.
"""

def cargar_numeros() -> list:
    """
    Solicita al usuario ingresar números enteros y los agrega a una lista hasta que ingrese -1

    Pre:
    - No recibe parámetros
    - El usuario debe ingresar números enteros o -1 para finalizar

    Post:
    - Devuelve una lista con los números ingresados por el usuario
    - Imprime por pantalla la lista cargada
    """

    lista=[]
    while True:
        try:
            n = int(input("Número a agregar (-1 para terminar): "))
            if n==-1:
                break
            lista.append(n)
        except ValueError:
            print("Debe ingresar un número entero")

    print(f"Lista cargada: {lista}")
    return lista

def buscar_posicion(lista: list) -> None:
    """
    Solicita al usuario un número a buscar en la lista y muestra su posición,
    permitiendo hasta 3 intentos en caso de error

    Pre:
    - lista es una lista de números enteros
    - El usuario debe ingresar números enteros

    Post:
    - Imprime por pantalla la posición del número encontrado
    - Si el número no se encuentra, permite hasta 3 intentos mostrando un mensaje de error
    - No devuelve ningún valor
    """

    errores=0
    while errores<3:
        try:
            buscar=int(input("Número a buscar: "))
            posicion=lista.index(buscar)
            print(f"El número {buscar} está en la posición {posicion+1}")
        except ValueError:
            errores+=1
            print("No se encontró ese número")

def main():
    lista=cargar_numeros()
    print()
    buscar_posicion(lista)

if __name__ == '__main__':
    main()
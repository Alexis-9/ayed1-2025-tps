"""Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos),
donde N se ingresa desde el teclado. Luego se solicita imprimir los últimos 10 valores de la lista. """

def lista_cuadrados()->None:
    """
    Genera una lista con los cuadrados de los números del 1 hasta n
    pre: El usuario ingresa n como número entero
    post: Imprime la lista con los cuadrados de 1 hasta n
          Imprime hasta los últimos 10 valores de la lista
    """
    n=int(input("Hasta que número desea ver su cuadrado en la lista: "))
    lista = [x ** 2 for x in range(1, n + 1)]

    print(f"La lista es {lista}")
    if n<10:
        print(f"Los últimos {n} valores son {lista[-10:]}")
    else:
        print(f"Los últimos 10 valores son {lista[-10:]}")

lista_cuadrados()
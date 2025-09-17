"""Eliminar de una lista de números enteros aquellos valores que se encuentren en
una segunda lista. Imprimir la lista original, la lista de valores a eliminar y la lista
resultante. La función debe modificar la lista original sin crear una copia modificada."""
import random as rn

def eliminar_valores(lista1: list[int], lista2: list[int]) -> None:
    """
    Elimina de la lista1 todos los elementos que se encuentran en lista2

    Pre:
    - lista1 lista de números enteros
    - lista2 lista de números enteros a eliminar de lista1

    Post:
    - Modifica lista1 eliminando todas las veces que aparecen los elementos de lista2
    - Imprime la lista original, los valores a eliminar y la lista final
    """
    print(f"La primera lista es {lista1}")
    print(f"Los valores a eliminar son {lista2}")
    for eliminar in lista2:
        while eliminar in lista1:
            lista1.remove(eliminar)
    print(f"La lista sin los valores a eliminar es {lista1}")


def ingresar_lista_manual(nombre_lista: str) -> list[int]:
    """
    Permite al usuario ingresar manualmente los elementos de una lista

    Pre: nombre_lista como string para mostrar en los mensajes

    Post: Devuelve una lista de números enteros ingresados por el usuario.
    """
    lista = []
    cantidad = int(input(f"Cuántos números quiere ingresar en {nombre_lista}: "))
    validar=(lambda x: x>0)
    while not validar(cantidad):
        print("Error")
        cantidad = int(input(f"Cuántos números quiere ingresar en {nombre_lista}: "))
    for i in range(cantidad):
        lista.append(int(input(f"Número {i+1} para {nombre_lista}: ")))
    return lista

def generar_lista_aleatoria(nombre_lista: str) -> list[int]:
    """
    Genera una lista de números aleatorios dentro de un rango definido por el usuario

    Pre: nombre_lista como string para mostrar en los mensajes

    Post:
    - Devuelve una lista de números enteros aleatorios con una longitud ingresada por el usuario
    - Los números generados están entre los rangos minimos y maximos ingresados por el usuario
    """
    lista = []
    cantidad = int(input(f"Cuántos números desea generar para {nombre_lista}: "))
    validar_cantidad= (lambda x: x > 0)
    while not validar_cantidad(cantidad):
        print("Error")
        cantidad = int(input(f"Cuántos números quiere ingresar en {nombre_lista}: "))

    rango_min = int(input("Ingrese el valor mínimo del rango: "))
    rango_max = int(input("Ingrese el valor máximo del rango: "))
    validar_rango= (lambda x,y: x < y)
    while not validar_rango(rango_min,rango_max):
        print("Error")
        rango_min = int(input("Ingrese el valor mínimo del rango: "))
        rango_max = int(input("Ingrese el valor máximo del rango: "))

    for i in range(cantidad):
        lista.append(rn.randint(rango_min, rango_max))
    return lista

def main() -> None:
    """
    Permite al usuario ingresar o generar listas y eliminar de la primera lista los elementos que están en la segunda.

    Pre: El usuario elige el modo de ingreso de números para las listas

    Post:
    - Modifica lista1 eliminando todos los elementos presentes en lista2
    - Imprime las listas originales y el resultado final
    """
    print("1: Ingresar lista manualmente")
    print("2: Generar lista aleatoriamente")
    op=input("Ingrese una opción: ")
    while op!="1" and op!="2":
        print("Error")
        op = input("Ingrese una opción: ")
    if op=="1":
        lista1 = ingresar_lista_manual("Lista 1")
        lista2 = ingresar_lista_manual("Lista 2")
    elif op=="2":
        lista1 = generar_lista_aleatoria("la primera lista")
        lista2 = generar_lista_aleatoria("la segunda lista")

    return eliminar_valores(lista1,lista2)

main()

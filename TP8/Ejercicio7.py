"""Definir un conjunto con números enteros entre 0 y 9. Luego solicitar valores al
usuario y eliminarlos del conjunto mediante el método remove, mostrando el contenido del conjunto luego de cada eliminación.
Finalizar el proceso al ingresar -1.
Utilizar manejo de excepciones para evitar errores al intentar quitar elementos
inexistentes.
"""
conjunto={0,1,2,3,4,5,6,7,8,9}

while True:
    try:
        print(conjunto)
        n=int(input("N: "))
        if n==-1:
            break
        conjunto.remove(n)
    except ValueError:
        print("Debe ingresar un número entero")
    except KeyError:
        print("Ese elemento no existe en el conjunto")
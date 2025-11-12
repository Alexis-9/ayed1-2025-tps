"""Desarrollar una función eliminarclaves() que reciba como parámetros un diccionario
y una lista de claves. La función debe eliminar del diccionario todas las claves
contenidas en la lista, devolviendo el diccionario modificado y un número entero
que represente la cantidad de claves eliminadas. Desarrollar también un programa
para verificar su comportamiento.
"""

def eliminarclaves(diccionario: dict, claves: list) -> tuple[dict, int]:
    """
    Elimina de un diccionario las claves que se encuentran en una lista dada

    Pre:
    - diccionario es un diccionario con cualquier tipo de claves y valores
    - claves es una lista que contiene las claves a eliminar
    - Las claves pueden existir o no en el diccionario

    Post:
    - Devuelve una tupla con el diccionario actualizado y la cantidad de claves eliminadas
    - Modifica el diccionario original eliminando las claves indicadas
    """

    cantidad=0
    for clave in claves:
        if clave in diccionario:
            del diccionario[clave]
            cantidad+=1
    return diccionario,cantidad

def main() -> None:
    """
    Use valores definidos

    Pre:
    - No recibe parámetros
    - La función eliminarclaves debe estar definida previamente
    - El diccionario inicial contiene claves numéricas y valores tipo str
    - La lista de claves indica qué elementos se desean eliminar

    Post:
    - Llama a eliminarclaves y obtiene el nuevo diccionario junto con la cantidad de eliminaciones realizadas
    - Muestra por pantalla el diccionario actualizado y la cantidad de claves eliminadas
    - No devuelve ningún valor
    """

    diccionario,cantidad=eliminarclaves({1:"a",2:"b",3:"c"},[1,2])

    print(f"Nuevo diccionario: {diccionario}")
    print(f"Cantidad de eliminaciones: {cantidad}")

if __name__ == '__main__':
    main()
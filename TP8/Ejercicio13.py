"""Escribir una función buscarclave() que reciba como parámetros un diccionario y un
valor, y devuelva una lista de claves que apunten ("mapeen") a ese valor en el diccionario. Comprobar el comportamiento de la función mediante un programa apropiado."""

def buscarclave(diccionario: dict, valor_a_buscar: int) -> list:
    """

    """
    claves = []

    for clave, valor in diccionario.items():
        if valor == valor_a_buscar:
            claves.append(clave)
    return claves


def main():
    dicc = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": "asd",
        "e": 1,
        "f": 4,
        "g": 5,
        "h": 2,
    }

    print(dicc)

    valor_a_buscar = input("Ingrese el valor a buscar: ")
    resultado = buscarclave(dicc, valor_a_buscar)

    if resultado:
        print(f"Las claves que tienen el valor {valor_a_buscar} son: {resultado}")
    else:
        print(f"No se encontró ninguna clave con el valor {valor_a_buscar}")


if __name__ == "__main__":
    main()

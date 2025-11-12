"""Escribir una función buscarclave() que reciba como parámetros un diccionario y un
valor, y devuelva una lista de claves que apunten ("mapeen") a ese valor en el diccionario. Comprobar el comportamiento de la función mediante un programa apropiado."""

def buscarclave(diccionario: dict, valor_a_buscar: str) -> list:
    """
    Busca todas las claves en un diccionario que tengan un valor específico

    Pre:
    - diccionario debe ser un diccionario válido
    - valor_a_buscar puede ser de cualquier tipo comparable con los valores del diccionario

    Post:
    - Devuelve una lista con todas las claves cuyo valor coincide con valor_a_buscar
    - Si no se encuentra ningún valor coincidente, devuelve una lista vacía
    """

    claves = []

    for clave, valor in diccionario.items():
        if str(valor) == valor_a_buscar:
            claves.append(clave)
    return claves


def main() -> None:
    """
    Crea un diccionario de ejemplo y permite al usuario buscar todas las claves que tengan un valor específico

    Pre:
    - No recibe parámetros
    - El usuario debe ingresar un valor a buscar

    Post:
    - Llama a la función `buscarclave` pasando el diccionario y el valor ingresado
    - Muestra por pantalla las claves que contienen el valor ingresado, si existen
    - Si no hay coincidencias, informa que no se encontró ninguna clave
    - No devuelve ningún valor
    """

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
    print("Claves - Valores")
    for clave,valor in dicc.items():
        print(f"{clave} - {valor}")

    valor_a_buscar = input("Ingrese el valor a buscar: ")
    resultado = buscarclave(dicc, valor_a_buscar)

    if resultado:
        print(f"Las claves que tienen el valor {valor_a_buscar} son: {resultado}")
    else:
        print(f"No se encontró ninguna clave con el valor {valor_a_buscar}")


if __name__ == "__main__":
    main()

"""Utilizar la técnica de listas por comprensión para construir una lista con todos los
números impares comprendidos entre 100 y 200"""

def lista_comprension() -> list[int]:
    """
    Genera una lista de números impares entre 100 y 200

    Pre: No recibe nada

    Post: Devuelve una lista con todos los números impares del 100 al 200
    """

    return [x for x in range(100,201) if x%2==1]

print(lista_comprension())



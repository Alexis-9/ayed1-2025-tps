"""Desarrollar una función que devuelva una cadena de caracteres con el nombre del
mes cuyo número se recibe como parámetro. Los nombres de los meses deberán
obtenerse de una lista de cadenas de caracteres inicializada dentro de la función.
Devolver una cadena vacía si el número de mes es inválido. La detección de meses
inválidos deberá realizarse a través de excepciones.
"""

def funcion(n1: int) -> None:
    """
    Muestra el nombre del mes correspondiente a un número entero del 1 al 12

    Pre:
    - n1 es un número entero que representa el mes (1-12)

    Post:
    - Imprime por pantalla el nombre del mes correspondiente
    - Si n1 es menor que 1 o mayor que 12, imprime un mensaje de error
    - No devuelve ningún valor
    """

    meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
    try:
        assert n1 > 0
        print(meses[n1-1])
    except IndexError:
        print("Mes inválido")
    except AssertionError:
        print("El número debe ser mayor a 0")

funcion(12)
funcion(13)
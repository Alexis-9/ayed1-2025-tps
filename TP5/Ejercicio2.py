"""Realizar una función que reciba como parámetros dos cadenas de caracteres conteniendo números reales, sume ambos valores y devuelva el resultado como un
número real. Devolver -1 si alguna de las cadenas no contiene un número válido,
utilizando manejo de excepciones para detectar el error."""


def sumar_cadenas(n1, n2) -> int:
    """
    Suma dos valores convertidos a enteros si es posible

    Pre:
    - n1 y n2 son valores que se intentarán convertir a enteros
    - Pueden ser cadenas numéricas o enteros

    Post:
    - Devuelve la suma de los dos números si la conversión es exitosa
    - Devuelve -1 si alguno de los valores no puede convertirse a entero
    """

    try:
        n1=int(n1)
        n2=int(n2)
        suma=n1+n2
        return suma
    except ValueError:
        return -1



print(sumar_cadenas("1","13"))
print(sumar_cadenas("uno","2"))
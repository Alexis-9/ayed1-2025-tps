"""Realizar una función que reciba como parámetros dos cadenas de caracteres conteniendo números reales, sume ambos valores y devuelva el resultado como un
número real. Devolver -1 si alguna de las cadenas no contiene un número válido,
utilizando manejo de excepciones para detectar el error."""


def sumar_cadenas(n1, n2):
    try:
        n1=int(n1)
        n2=int(n2)
        suma=n1+n2
        return suma
    except ValueError:
        return -1



print(sumar_cadenas("1","13"))
print(sumar_cadenas("uno","2"))
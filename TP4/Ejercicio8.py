"""Desarrollar una función que devuelva una subcadena con los últimos N caracteres
de una cadena dada. La cadena y el valor de N se pasan como parámetros."""

def ultimos_caracteres(cadena: str, n: int) -> str:
    """
    Devuelve los últimos n caracteres de una cadena usando rebanadas

    Pre:
    - cadena es una cadena de caracteres
    - n es un entero positivo menor o igual a la longitud de la cadena

    Post:
    - Devuelve una subcadena formada por los últimos n caracteres de la cadena original
    """

    subcadena=cadena[-n:]
    return subcadena

def main() -> None:
    """
    Solicita una cadena y un número n,
    y muestra los últimos n caracteres de la cadena

    Pre:
    - No recibe parámetros
    - El usuario debe ingresar una cadena de texto y un número entero positivo
    - El valor de n debe ser menor o igual a la longitud de la cadena

    Post:
    - Llama a la función ultimos_caracteres para obtener la subcadena
    - Imprime por pantalla los últimos n caracteres de la cadena ingresada
    - No devuelve ningún valor
    """

    cadena = input("Ingrese la cadena: ")
    n = int(input("Cuantos carácteres finales quiere mostrar: "))
    cadena_nueva=ultimos_caracteres(cadena,n)
    print(cadena_nueva)

if __name__ == '__main__':
    main()
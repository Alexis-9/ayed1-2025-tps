"""Escribir un programa que permita ingresar un número entero N y genere un
diccionario por comprensión con la tabla de multiplicar de N del 1 al 12. Mostrar la
tabla de multiplicar con el formato apropiado."""

def diccionario_comprension() -> None:
    """
    Genera y muestra un diccionario con la tabla de multiplicar de un número del 1 al 12

    Pre:
    - No recibe parámetros
    - El usuario debe ingresar un número entero positivo

    Post:
    - Crea un diccionario donde las claves son los números del 1 al 12 y los valores son el producto con el número ingresado
    - Imprime la tabla de multiplicar en formato 'n x i = resultado'
    - No devuelve ningún valor
    """

    n=int(input("Número del que desea ver la tabla de multiplicar del 1 al 12: "))

    diccionario={i:i*n for i in range(1,13)}

    for numero, resultado in diccionario.items():
        print(f"{n} x {numero} = {resultado}")

diccionario_comprension()
""" La raíz cuadrada de un número puede obtenerse mediante la función sqrt() del
módulo math. Escribir un programa que utilice esta función para calcular la raíz
cuadrada de un número cualquiera ingresado a través del teclado. El programa
debe utilizar manejo de excepciones para evitar errores si se ingresa un número
negativo"""
import math

def funcion():
    try:
        n = int(input("Número: "))
        raiz=math.sqrt(n)
        print(f"La raíz cuadrada de {n} es {raiz}")
        return
    except ValueError:
        print("Error: Debe ser un número entero positivo")
        return funcion()

funcion()
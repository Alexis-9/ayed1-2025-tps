"""Escribir un programa que permita ingresar un número entero N y genere un
diccionario por comprensión con la tabla de multiplicar de N del 1 al 12. Mostrar la
tabla de multiplicar con el formato apropiado."""

n=int(input("N: "))

diccionario={i:i*n for i in range(1,13)}

for numero, resultado in diccionario.items():
    print(f"{n} x {numero} = {resultado}")
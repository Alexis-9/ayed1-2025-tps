"""Desarrollar una función que determine si una cadena de caracteres es capicúa, sin
utilizar cadenas auxiliares ni rebanadas. Escribir además un programa que permita
verificar su funcionamiento."""

def es_capicua(cadena):
    largo=len(cadena)//2
    cantidad=0
    inicio=0
    fin=len(cadena)-1
    capicua=True

    while cantidad<largo:
        cantidad+=1
        if cadena[inicio]!=cadena[fin]:
            capicua=False
        inicio += 1
        fin -= 1
    return capicua

def main():
    texto = input("Cadena: ")
    if es_capicua(texto):
        print("La cadena es capicúa")
    else:
        print("La cadena no es capicúa")

if __name__ == '__main__':
    main()
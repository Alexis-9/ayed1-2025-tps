"""Desarrollar una función que determine si una cadena de caracteres es capicúa, sin
utilizar cadenas auxiliares ni rebanadas. Escribir además un programa que permita
verificar su funcionamiento."""

def es_capicua(cadena: str) -> bool:
    """
    Determina si una cadena es capicúa

    Pre: recibe una cadena de caracteres no vacía
    Post: devuelve True si la cadena es capicúa, False en caso contrario
    """
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

def main() -> None:
    """
    Función principal que solicita al usuario una cadena y verifica si es capicúa

    Pre: no recibe parámetros, el usuario ingresa una cadena por teclado
    Post: muestra por pantalla si la cadena ingresada es capicúa o no
    """
    texto = input("Cadena: ")
    if es_capicua(texto):
        print("La cadena es capicúa")
    else:
        print("La cadena no es capicúa")

if __name__ == '__main__':
    main()
"""Desarrollar una función que devuelva una subcadena con los últimos N caracteres
de una cadena dada. La cadena y el valor de N se pasan como parámetros."""

def ultimos_caracteres(cadena,n):
    subcadena=cadena[-n:]
    return subcadena

def main():
    cadena = input("Ingrese la cadena: ")
    n = int(input("Cuantos carácteres finales quiere mostrar: "))
    cadena_nueva=ultimos_caracteres(cadena,n)
    print(cadena_nueva)

if __name__ == '__main__':
    main()
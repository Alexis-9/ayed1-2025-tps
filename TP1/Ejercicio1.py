"""Desarrollar una función que reciba tres números enteros positivos y devuelva el
mayor de los tres, sólo si éste es único (es decir el mayor estricto). Devolver -1 en
caso de no haber ninguno. No utilizar operadores lógicos (and, or, not). Desarrollar
también un programa para ingresar los tres valores, invocar a la función y mostrar
el máximo hallado, o un mensaje informativo si éste no existe."""

def encontrar_mayor(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    elif c>a and c>b:
        return c
    else:
        return -1

def ingresar_valores():
    primero = int(input("Ingrese el primer número: "))
    segundo = int(input("Ingrese el segundo número: "))
    tercero = int(input("Ingrese el tercer número: "))

    bien=False
    while bien==False:
        if primero < 0:
            print("No se permiten números negativos.")
            primero = int(input("Ingrese el primer número: "))
        elif segundo < 0:
            print("No se permiten números negativos.")
            segundo = int(input("Ingrese el segundo número: "))
        elif tercero < 0:
            print("No se permiten números negativos.")
            tercero = int(input("Ingrese el tercer número: "))
        else:
            bien=True

    resultado = encontrar_mayor(primero, segundo, tercero)

    if resultado == -1:
        print("No existe un mayor único.")
    else:
        print(f"El mayor único es: {resultado}")
ingresar_valores()
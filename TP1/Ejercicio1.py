"""Desarrollar una función que reciba tres números enteros positivos y devuelva el
mayor de los tres, sólo si éste es único (es decir el mayor estricto). Devolver -1 en
caso de no haber ninguno. No utilizar operadores lógicos (and, or, not). Desarrollar
también un programa para ingresar los tres valores, invocar a la función y mostrar
el máximo hallado, o un mensaje informativo si éste no existe."""

def encontrar_mayor(a:int,b:int,c:int)-> int:
    """
    Busca el número mayor
    pre: Recibe 3 números enteros
    post: Hace return de el unico número mayor o -1 en caso de que no haya un mayor unico
    """
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    elif c>a and c>b:
        return c
    else:
        return -1

def ingresar_valores() -> None:
    """
    Pide tres números enteros por teclado, valida que no sean negativos y devuelve el mayor entre ellos usando la función encontrar_mayor

    pre:-El usuario ingresa tres números enteros
        -No se permiten números negativos

    post: Imprime el mayor único o imprime que no existe un mayor único en caso de que no haya

    """
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
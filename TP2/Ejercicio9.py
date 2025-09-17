"""Generar e imprimir una lista por comprensión entre A y B con los múltiplos de 7
que no sean múltiplos de 5. A y B se ingresar desde el teclado"""

def lista() -> list[int]:
    """
    Genera una lista de números entre dos valores distintos ingresados por el usuario,
    que sean múltiplos de 7 pero no múltiplos de 5

    Pre: El usuario ingresa dos números enteros distintos

    Post: Devuelve una lista de números enteros que sean múltiplos de 7 y no de 5 dentro de los rangos A y B
    """
    a=int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    while a==b:
        print("Ingrese valores distintos")
        a = int(input("Ingrese el primer número: "))
        b = int(input("Ingrese el segundo número: "))
    menor = min(a, b)
    mayor = max(a, b)
    return [x for x in range(menor,mayor+1) if x % 7 == 0 and x % 5 != 0]

print(lista())
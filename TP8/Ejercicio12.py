"""Una librería almacena su lista de precios en un diccionario. Diseñar un programa
para crearlo, incrementar los precios de los cuadernos en un 15%, imprimir un
listado con todos los elementos de la lista de precios e indicar cuál es el ítem más
costoso que venden en el comercio"""


def generar_diccionario()->dict:
    """
    """
    diccionario = dict()
    while True:
        producto = input("Ingrese el producto (Enter para salir): ")
        if producto == "":
            break

        while True:
            precio = int(input("Ingrese el precio: "))
            if precio <= 0:
                print("El precio debe ser mayor a 0")
            else:
                break

        while True:
            cuaderno = input("Es cuaderno (si/no): ")
            cuaderno.strip().lower()
            if cuaderno not in ("si", "no"):
                print("Opción inválida")
            elif cuaderno=="si":
                precio=round(precio*1.15)
                break
            else:
                break

        diccionario[producto] = precio
    return diccionario

def mayor_precio(diccionario:dict):
    mayor=0
    producto=0
    for clave,valor in diccionario.items():
        if mayor<valor:
            mayor=valor
            producto=clave
    return producto,mayor


def main()->None:
    """
    """
    diccionario=generar_diccionario()
    producto,precio=mayor_precio(diccionario)
    print(diccionario)
    print(f"El producto más caro es ({producto}) con un valor de ${precio}")





main()
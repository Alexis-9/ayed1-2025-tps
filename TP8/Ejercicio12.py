"""Una librería almacena su lista de precios en un diccionario. Diseñar un programa
para crearlo, incrementar los precios de los cuadernos en un 15%, imprimir un
listado con todos los elementos de la lista de precios e indicar cuál es el ítem más
costoso que venden en el comercio"""


def generar_diccionario() -> dict:
    """
    Genera un diccionario de productos con sus precios, aplicando un aumento si es cuaderno

    Pre:
    - No recibe parámetros
    - El usuario ingresa el nombre del producto (str)
    - El usuario ingresa el precio del producto (entero mayor a 0)
    - El usuario indica si el producto es cuaderno con 'Si: 1' o 'No: 2'

    Post:
    - Devuelve un diccionario donde las claves son los nombres de los productos y los valores son los precios
    - Si el producto es un cuaderno, se aplica un aumento del 15% al precio
    - Permite ingresar múltiples productos hasta que el usuario ingrese una cadena vacía como nombre del producto
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
            cuaderno = input("Es cuaderno (Si: 1 | No: 2): ")
            cuaderno.strip()
            if cuaderno not in ("1", "2"):
                print("Opción inválida")
            elif cuaderno=="1":
                precio=round(precio*1.15)
                break
            else:
                break

        diccionario[producto] = precio
    return diccionario

def mayor_precio(diccionario: dict) -> tuple:
    """
    Encuentra el producto con el precio más alto en un diccionario

    Pre:
    - diccionario debe ser un diccionario válido con claves como nombres de productos y valores numéricos positivos (precios)


    Post:
    - Devuelve una tupla (producto, precio) donde:
        - producto: clave del diccionario con el mayor valor
        - precio: valor más alto en el diccionario
    """

    mayor=0
    producto=0
    for clave,valor in diccionario.items():
        if mayor<valor:
            mayor=valor
            producto=clave
    return producto,mayor


def main() -> None:
    """
    Función principal que genera un diccionario de productos con sus precios y muestra el producto más caro

    Pre:
    - No recibe parámetros

    Post:
    - Llama a la función `generar_diccionario` para crear un diccionario de productos
    - Llama a la función `mayor_precio` para determinar el producto más caro
    - Si se ingresaron productos, imprime el diccionario completo y el producto más caro con su precio
    - Si no se ingresaron productos, muestra un mensaje indicando que no se ingresaron productos
    - No devuelve ningún valor
    """

    diccionario=generar_diccionario()
    producto,precio=mayor_precio(diccionario)
    if diccionario:
        print(diccionario)
        print(f"El producto más caro es ({producto}) con un valor de ${precio}")
    else:
        print("No se ingresaron productos")


if __name__ == '__main__':
    main()
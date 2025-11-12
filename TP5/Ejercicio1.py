""""Desarrollar una función para ingresar a través del teclado un número natural. La
función rechazará cualquier ingreso inválido de datos utilizando excepciones y
mostrará la razón exacta del error. Controlar que se ingrese un número, que ese
número sea entero y que sea mayor que 0, mostrando un mensaje con la razón
exacta del error en caso necesario. Devolver el valor ingresado cuando éste sea
correcto. Escribir también un programa que permita probar el correcto funcionamiento de la misma"""

def ingresar_numero_natural() -> int:
    """
    Solicita al usuario ingresar un número natural y lo valida

    Pre:
    - No recibe parámetros
    - El usuario debe ingresar un número entero mayor a 0

    Post:
    - Devuelve un número entero positivo ingresado por el usuario
    - Si el valor ingresado no es válido, solicita el ingreso nuevamente hasta obtener un número correcto con manejo de excepciones
    """

    while True:
        try:
            num = int(input("Ingrese un número natural: "))
            assert num>0
            return num

        except ValueError:
            print("El número debe ser un entero válido.")
        except AssertionError:
            print("El número debe ser mayor a 0")

def main() -> None:
    """
    Solicita al usuario un número natural y lo muestra por pantalla

    Pre:
    - No recibe parámetros
    - El usuario debe ingresar un número entero mayor a 0

    Post:
    - Llama a la función ingresar_numero_natural para obtener un número válido
    - Imprime por pantalla el número ingresado
    - No devuelve ningún valor
    """

    numero = ingresar_numero_natural()
    print(f"Número ingresado: {numero}")

if __name__ == "__main__":
    main()
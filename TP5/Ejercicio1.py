""""Desarrollar una función para ingresar a través del teclado un número natural. La
función rechazará cualquier ingreso inválido de datos utilizando excepciones y
mostrará la razón exacta del error. Controlar que se ingrese un número, que ese
número sea entero y que sea mayor que 0, mostrando un mensaje con la razón
exacta del error en caso necesario. Devolver el valor ingresado cuando éste sea
correcto. Escribir también un programa que permita probar el correcto funcionamiento de la misma"""

def ingresar_numero_natural():
    while True:
        try:
            num = int(input("Ingrese un número natural: "))
            assert num>0
            return num

        except ValueError:
            print("El número debe ser un entero válido.")
        except AssertionError:
            print("El número debe ser mayor a 0")

def main():
    numero = ingresar_numero_natural()
    print(f"Número ingresado: {numero}")

if __name__ == "__main__":
    main()
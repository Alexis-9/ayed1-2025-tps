"""Desarrollar una función que extraiga una subcadena de una cadena de caracteres,
indicando la posición y la cantidad de caracteres deseada. Devolver la subcadena
como valor de retorno. Escribir también un programa para verificar el comportamiento de la misma. Ejemplo, dada la cadena "El número de teléfono es 4356-
7890" extraer la subcadena que comienza en la posición 25 y tiene 9 caracteres,
resultando la subcadena "4356-7890". Escribir una función para cada uno de los siguientes casos:
a. Utilizando rebanadas
b. Sin utilizar rebanadas
"""
def sin_rebanadas(frase: str, posicion: int, largo: int) -> None:
    """
    Extrae y muestra una subcadena de la frase empezando en una posición específica y con una longitud determinada, sin usar rebanadas

    Pre:
    - frase es una cadena de caracteres
    - posicion es un entero que indica la posición inicial
    - largo es un entero que indica la cantidad de caracteres a extraer
    - posicion y largo deben ser válidos para la longitud de la frase

    Post:
    - Construye la subcadena usando un for y la imprime por pantalla
    - No devuelve ningún valor
    """

    frase2=""
    for x in range(len(frase)):
        if posicion==x:
            for i in range(largo):
                frase2+=frase[posicion+i]
    print(frase2)

def con_rebanadas(frase: str, posicion: int, largo: int) -> None:
    """
    Extrae y muestra una subcadena de la frase usando rebanadas

    Pre:
    - frase es una cadena de caracteres
    - posicion es un entero que indica la posición inicial
    - largo es un entero que indica la cantidad de caracteres a extraer
    - posicion y largo deben ser válidos para la longitud de la frase

    Post:
    - Imprime por pantalla la subcadena obtenida mediante rebanadas
    - No devuelve ningún valor
    """
    frase2=frase[posicion:posicion+largo]
    print(frase2)

def main() -> None:
    """
    Función principal que solicita una frase, una posición inicial y un largo,
    y muestra la subcadena correspondiente usando dos métodos: con y sin rebanadas

    Pre:
    - No recibe parámetros
    - El usuario debe ingresar una cadena de texto, un número entero para la posición y un número entero para el largo
    - Los valores de posición y largo deben ser válidos para la frase

    Post:
    - Muestra por pantalla la subcadena extraída sin rebanadas y usando rebanadas
    - No devuelve ningún valor
    """

    frase = input("Frase: ")
    posicion = int(input("Posición: "))
    largo = int(input("Largo: "))

    print("Sin utilizar rebanadas: ")
    sin_rebanadas(frase,posicion,largo)

    print("Utilizando rebanadas: ")
    con_rebanadas(frase, posicion, largo)

if __name__ == '__main__':
    main()
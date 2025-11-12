"""Escribir una función para eliminar una subcadena de una cadena de caracteres, a
partir de una posición y cantidad de caracteres dadas, devolviendo la cadena resultante. Escribir también un programa para verificar el comportamiento de la misma.
Escribir una función para cada uno de los siguientes casos:
a. Utilizando rebanadas
b. Sin utilizar rebanadas
"""
def con_rebanadas(frase: str, posicion: int, largo: int) -> None:
    """
    Elimina una subcadena de la frase utilizando rebanadas y muestra el resultado

    Pre:
    - frase es una cadena de caracteres
    - posicion es un entero que indica la posición inicial de la subcadena a eliminar
    - largo es un entero que indica la cantidad de caracteres a eliminar
    - posicion y largo deben ser válidos para la longitud de la frase

    Post:
    - Imprime por pantalla la frase resultante después de eliminar la subcadena
    - No devuelve ningún valor
    """

    frase2=frase[:posicion]+frase[posicion+largo:]
    print(frase2)

def sin_rebanadas(frase: str, posicion: int, largo: int) -> None:
    """
    Elimina una subcadena de la frase sin usar rebanadas y muestra el resultado

    Pre:
    - frase es una cadena de caracteres
    - posicion es un entero que indica la posición inicial de la subcadena a eliminar
    - largo es un entero que indica la cantidad de caracteres a eliminar
    - posicion y largo deben ser válidos para la longitud de la frase

    Post:
    - Construye la frase resultante omitiendo la subcadena especificada y la imprime por pantalla
    - No devuelve ningún valor
    """

    frase2=""
    indice=0
    for i in range(len(frase)-(largo-1)):
        if i==posicion:
            indice+=largo
        else:
            frase2+=frase[indice]
            indice += 1
    print(frase2)

def main() -> None:
    """
    Solicita una frase, una posición inicial y un largo,
    y elimina la subcadena correspondiente mostrando el resultado con y sin rebanadas

    Pre:
    - No recibe parámetros
    - El usuario debe ingresar una cadena de texto, un número entero para la posición y un número entero para el largo
    - Los valores de posición y largo deben ser válidos para la frase

    Post:
    - Muestra por pantalla la frase resultante después de eliminar la subcadena usando rebanadas y sin rebanadas
    - No devuelve ningún valor
    """

    frase = input("Frase: ")
    posicion = int(input("Posicion: "))
    largo = int(input("Largo: "))

    print("Usando rebanadas: ")
    con_rebanadas(frase,posicion,largo)
    print("Sin usar rebanadas: ")
    sin_rebanadas(frase,posicion,largo)

if __name__ == '__main__':
    main()
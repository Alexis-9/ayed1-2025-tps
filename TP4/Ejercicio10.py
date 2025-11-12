"""Desarrollar una función para reemplazar todas las apariciones de una palabra por
otra en una cadena de caracteres y devolver la cadena obtenida y un entero con la
cantidad de reemplazos realizados. Tener en cuenta que sólo deben reemplazarse
palabras completas, y no fragmentos de palabras. Escribir también un programa
para verificar el comportamiento de la función. """

def reemplazar_palabra(frase: str, reemplazar: str, nueva: str) -> tuple:
    """
    Reemplaza todas las ocurrencias de una palabra en una frase por otra palabra y cuenta cuántas se reemplazaron

    Pre:
    - frase es una cadena de caracteres
    - reemplazar es la palabra que se desea sustituir
    - nueva es la palabra que reemplazará a la original

    Post:
    - Devuelve una tupla:
        - nueva_frase: la frase resultante con los reemplazos realizados
        - contador: un entero con la cantidad de palabras reemplazadas
    """

    frase_separada=frase.split()
    contador=0

    for i,x in enumerate(frase_separada):
        if reemplazar==x:
            frase_separada[i]=nueva
            contador+=1

    nueva_frase=" ".join(frase_separada)

    return nueva_frase,contador

def main() -> None:
    """
    Solicita una frase y dos palabras al usuario,
    reemplaza todas las ocurrencias de la primera palabra por la segunda
    y muestra la frase resultante junto con la cantidad de reemplazos

    Pre:
    - No recibe parámetros
    - El usuario debe ingresar una cadena de texto y dos palabras válidas para realizar los reemplazos

    Post:
    - Llama a la función reemplazar_palabra para generar la frase modificada
    - Imprime por pantalla la nueva frase y el número de palabras reemplazadas
    - No devuelve ningún valor
    """

    texto = input("Ingrese una frase: ")
    palabra_vieja = input("Palabra a reemplazar: ")
    palabra_nueva =  input("Palabra nueva: ")

    frase, cantidad= reemplazar_palabra(texto, palabra_vieja, palabra_nueva)

    print(f"La nueva frase es: {frase}")
    print(f"Reemplazos de la palabra: {cantidad} ")


if __name__ == '__main__':
    main()

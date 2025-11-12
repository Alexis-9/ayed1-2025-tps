"""Crear una función contarvocales(), que reciba una palabra y cuente cuántas vocales
contiene, identificando la cantidad de cada una. Devolver un diccionario con los
resultados. Luego desarrollar un programa para leer una frase e invocar a la
función por cada palabra que contenga la misma. Imprimir las palabras y la
cantidad de vocales hallada.
"""

def contarvocales(palabra: str) -> dict:
    """
    Cuenta cuántas veces aparece cada vocal en una palabra

    Pre:
    - Recibe una cadena de caracteres (palabra)
    - La palabra debe contener solo letras

    Post:
    - Devuelve un diccionario con las vocales 'a', 'e', 'i', 'o', 'u' como claves
    - Los valores son la cantidad de veces que aparece cada vocal en la palabra
    """

    vocales={"a":0,"e":0,"i":0,"o":0,"u":0}

    for x in palabra:
        if x in vocales:
            vocales[x]+=1

    return vocales

def main() -> None:
    """
    Cuenta las vocales de todas las palabras de una frase

    Pre:
    - No recibe parámetros
    - El usuario debe ingresar una cadena de texto

    Post:
    - Separa la frase en palabras
    - Llama a la función contarvocales para cada palabra y acumula las cantidades
    - Imprime por pantalla la cantidad de cada vocal en toda la frase
    - No devuelve ningún valor
    """

    frase= input("Frase: ")

    palabras=frase.split()
    vocales={"a":0,"e":0,"i":0,"o":0,"u":0}
    for palabra in frase:
        vocales_palabra=contarvocales(palabra)
        for vocal in vocales:
            vocales[vocal]+=vocales_palabra[vocal]

    print(f"En las palabras {palabras} hay: ")

    for vocal in vocales:
        print(vocales[vocal] ,vocal)

if __name__ == '__main__':
    main()
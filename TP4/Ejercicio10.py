"""Desarrollar una función para reemplazar todas las apariciones de una palabra por
otra en una cadena de caracteres y devolver la cadena obtenida y un entero con la
cantidad de reemplazos realizados. Tener en cuenta que sólo deben reemplazarse
palabras completas, y no fragmentos de palabras. Escribir también un programa
para verificar el comportamiento de la función. """

def reemplazar_palabra(frase, reemplazar, nueva):
    frase_separada=frase.split()
    contador=0

    for i,x in enumerate(frase_separada):
        if reemplazar==x:
            frase_separada[i]=nueva
            contador+=1

    nueva_frase=" ".join(frase_separada)

    return nueva_frase,contador

def main():
    texto = input("Ingrese una frase: ")
    palabra_vieja = input("Palabra a reemplazar: ")
    palabra_nueva =  input("Palabra nueva: ")

    frase, cantidad= reemplazar_palabra(texto, palabra_vieja, palabra_nueva)

    print(f"La nueva frase es: {frase}")
    print(f"Reemplazos de la palabra: {cantidad} ")


if __name__ == '__main__':
    main()

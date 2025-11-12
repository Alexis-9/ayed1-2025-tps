"""Ingresar una frase desde el teclado y usar un conjunto para eliminar las palabras
repetidas, dejando un solo ejemplar de cada una. Finalmente mostrar las palabras
ordenadas según su longitud. Los signos de puntuación no deben afectar el
proceso.
"""
def ordenar_palabras(cadena: str) -> list[str]:
    """
    Ordena las palabras de una cadena por longitud y elimina duplicados y signos de puntuación

    Pre:
    - Recibe una cadena de texto
    - La cadena puede contener palabras separadas por espacios y signos de puntuación

    Post:
    - Devuelve una lista de palabras únicas ordenadas de menor a mayor longitud
    - Los signos de puntuación se eliminan
    - No se incluyen palabras repetidas
    """

    frase2=[]
    frases=set()

    for i,x in enumerate(cadena):
        if x==" ":
            if frase2 and ("".join(frase2)) not in frases:
                frases.add("".join(frase2))
            frase2=[]

        elif x=="," or x=="." or x=="?" or x=="¿" or x=="!" or x=="¡":
            continue
        else:
            frase2.append(x)

        if i+1==len(cadena):
            if  frase2 and ("".join(frase2)) not in frases:
                frases.add("".join(frase2))


    frases=list(frases)

    for i in range(len(frases)):
        for j in range(len(frases) - 1 - i):
            if len(frases[j]) > len(frases[j+1]):
                frases[j], frases[j + 1] = frases[j + 1], frases[j]

    return frases

def main() -> None:
    """
    Función principal que solicita al usuario ingresar una frase, la procesa y muestra sus palabras ordenadas por longitud

    Pre:
    - No recibe parámetros
    - El usuario debe ingresar una cadena de texto

    Post:
    - Llama a la función ordenar_palabras para obtener las palabras únicas ordenadas de menor a mayor longitud
    - Imprime por pantalla la frase original y la lista de palabras ordenadas
    - No devuelve ningún valor
    """

    cadena = input("Ingrese una frase: ")
    frases=ordenar_palabras(cadena)
    print(f"Las palabras de la frase: ")
    print("================================================")
    print(cadena)
    print("================================================")
    print("Ordenadas de menor a mayor longitud: ")
    print(f"{frases}")

if __name__ == '__main__':
    main()
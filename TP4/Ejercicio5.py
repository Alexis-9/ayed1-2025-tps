"""Escribir una función filtrar_palabras() que reciba una cadena de caracteres conteniendo una frase y un entero N, y devuelva otra cadena con las palabras que
tengan N o más caracteres de la cadena original.
Escribir también un programa para verificar el comportamiento de la misma.
Hacer tres versiones de la función, para cada uno de los siguientes casos:
a. Utilizando sólo ciclos normales
b. Utilizando listas por comprensión
c. Utilizando la función filter"""

def filtrar_palabras_ciclos(frase, n):
    palabras = frase.split()
    lista=[]
    for i in palabras:
        if len(i)>=n:
            lista.append(i)
    return " ".join(lista)

def filtrar_palabras_comprension(frase, n):
    return " ".join([x for x in frase.split() if len(x) >= n])

def filtrar_palabras_filter(frase, n):
    return " ".join(filter(lambda x: len(x) >= n, frase.split()))


def main():
    frase = input("Ingrese una frase: ")
    n = int(input("Ingrese el mínimo de caracteres: "))

    print(f"Las palabras con {n} o más caracteres son: ")
    print("Usando ciclos normales: ")
    print(filtrar_palabras_ciclos(frase, n))

    print("Usando lista por comprensión: ")
    print(filtrar_palabras_comprension(frase, n))

    print("Usando filter(): ")
    print(filtrar_palabras_filter(frase, n))


if __name__ == '__main__':
    main()
"""Desarrollar una función que extraiga una subcadena de una cadena de caracteres,
indicando la posición y la cantidad de caracteres deseada. Devolver la subcadena
como valor de retorno. Escribir también un programa para verificar el comportamiento de la misma. Ejemplo, dada la cadena "El número de teléfono es 4356-
7890" extraer la subcadena que comienza en la posición 25 y tiene 9 caracteres,
resultando la subcadena "4356-7890". Escribir una función para cada uno de los siguientes casos:
a. Utilizando rebanadas
b. Sin utilizar rebanadas
"""
def sin_rebanadas(frase,posicion,largo):
    frase2=""
    for x in range(len(frase)):
        if posicion==x:
            for i in range(largo):
                frase2+=frase[posicion+i]
    print(frase2)

def con_rebanadas(frase,posicion,largo):
    frase2=frase[posicion:posicion+largo]
    print(frase2)

def main():
    frase = input("Frase: ")
    posicion = int(input("Posición: "))
    largo = int(input("Largo: "))

    print("Sin utilizar rebanadas: ")
    sin_rebanadas(frase,posicion,largo)

    print("Utilizando rebanadas: ")
    con_rebanadas(frase, posicion, largo)

if __name__ == '__main__':
    main()
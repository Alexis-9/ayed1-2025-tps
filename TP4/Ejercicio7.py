"""Escribir una función para eliminar una subcadena de una cadena de caracteres, a
partir de una posición y cantidad de caracteres dadas, devolviendo la cadena resultante. Escribir también un programa para verificar el comportamiento de la misma.
Escribir una función para cada uno de los siguientes casos:
a. Utilizando rebanadas
b. Sin utilizar rebanadas
"""
def con_rebanadas(frase,posicion,largo):
    frase2=frase[:posicion]+frase[posicion+largo:]
    print(frase2)

def sin_rebanadas(frase,posicion,largo):
    frase2=""
    indice=0
    for i in range(len(frase)-(largo-1)):
        if i==posicion:
            indice+=largo
        else:
            frase2+=frase[indice]
            indice += 1
    print(frase2)

def main():
    frase = input("Frase: ")
    posicion = int(input("Posicion: "))
    largo = int(input("Largo: "))

    print("Usando rebanadas: ")
    con_rebanadas(frase,posicion,largo)
    print("Sin usar rebanadas: ")
    sin_rebanadas(frase,posicion,largo)

if __name__ == '__main__':
    main()
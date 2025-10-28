"""Crear una función contarvocales(), que reciba una palabra y cuente cuántas vocales
contiene, identificando la cantidad de cada una. Devolver un diccionario con los
resultados. Luego desarrollar un programa para leer una frase e invocar a la
función por cada palabra que contenga la misma. Imprimir las palabras y la
cantidad de vocales hallada.
"""

def contarvocales(palabra):
    vocales={"a":0,"e":0,"i":0,"o":0,"u":0}

    for x in palabra:
        if x in vocales:
            vocales[x]+=1

    return vocales


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
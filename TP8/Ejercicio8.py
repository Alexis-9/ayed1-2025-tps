"""Generar e imprimir un diccionario donde las claves sean nÃºmeros enteros entre 1 y
20 (ambos incluidos) y los valores asociados sean el cuadrado de las claves.
"""

diccionario={}
for i in range(1,21):
    diccionario[i]=i**2

print(diccionario)
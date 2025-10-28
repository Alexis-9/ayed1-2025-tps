"""Desarrollar una función eliminarclaves() que reciba como parámetros un diccionario
y una lista de claves. La función debe eliminar del diccionario todas las claves
contenidas en la lista, devolviendo el diccionario modificado y un número entero
que represente la cantidad de claves eliminadas. Desarrollar también un programa
para verificar su comportamiento.
"""

def eliminarclaves(diccionario, claves):
    cantidad=0
    for clave in claves:
        if clave in diccionario:
            del diccionario[clave]
            cantidad+=1
    return diccionario,cantidad


diccionario,cantidad=eliminarclaves({1:"a",2:"b",3:"c"},[1,2])

print(f"Nuevo diccionario: {diccionario}")
print(f"Cantidad de eliminaciones: {cantidad}")
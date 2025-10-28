"""Ingresar una frase desde el teclado y usar un conjunto para eliminar las palabras
repetidas, dejando un solo ejemplar de cada una. Finalmente mostrar las palabras
ordenadas según su longitud. Los signos de puntuación no deben afectar el
proceso.
"""

cadena="hola chau pasto,,,, casa preciso pasto hola chau pasto casa hola"
frase2=[]
frases=set()

for i,x in enumerate(cadena):
    if x==" ":
        if frase2 and ("".join(frase2)) not in frases:
            frases.add("".join(frase2))
        frase2=[]
        cantidad = 0
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


print(f"Las palabras de la frase: ")
print("================================================")
print(cadena)
print("================================================")
print("Ordenadas de menor a mayor longitud: ")
print(f"{frases}")
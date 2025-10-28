"""Escribir una función que reciba como parámetro una cadena de caracteres en la que
las palabras se encuentran separadas por uno o más espacios. Devolver otra
cadena con las palabras ordenadas según su longitud, dejando un espacio entre
cada una. Los signos de puntuación no deben ser tenidos en cuenta al medir la
longitud de las palabras, pero deberán conservarse en la cadena final."""

def ordenar_por_longitud(cadena):
    cantidad=0
    cantidades=[]
    frases=[]
    frase2 = []

    for i,x in enumerate(cadena):
        cantidad+=1
        if x=="," or x=="." or x=="?" or x=="¿" or x=="!" or x=="¡":
            cantidad-=1
        if x==" ":
            if frase2:
                cantidades.append(cantidad-1)
                frases.append("".join(frase2))
            frase2=[]
            cantidad = 0
        else:
            frase2.append(x)

        if i+1==len(cadena):
            if frase2:
                cantidades.append(cantidad)
                frases.append("".join(frase2))


    for i in range(len(cantidades)):
        for j in range(len(cantidades)-1-i):
            if cantidades[j]>cantidades[j+1]:
                cantidades[j], cantidades[j+1]=cantidades[j+1],cantidades[j]
                frases[j],frases[j+1]=frases[j+1],frases[j]

    return " ".join(frases)

def main():
    cadena=input("Ingrese la cadena: ")
    nueva_cadena=ordenar_por_longitud(cadena)
    print(f"La cadena con sus palabras ordenadas por longitud: {nueva_cadena}")

if __name__ == '__main__':
    main()
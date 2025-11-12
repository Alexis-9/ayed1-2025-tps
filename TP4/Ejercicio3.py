"""Los números de claves de dos cajas fuertes están intercalados dentro de un número
entero llamado "clave maestra", cuya longitud no se conoce. Realizar un programa
para obtener ambas claves, donde la primera se construye con los dígitos ubicados
en posiciones impares de la clave maestra y la segunda con los dígitos ubicados en
posiciones pares. Los dígitos se numeran desde la izquierda. Ejemplo: Si clave
maestra fuera 18293, la clave 1 sería 123 y la clave 2 sería 89."""

def buscar_clave(clave: str) -> None:
    """
    Separa una clave en dos partes alternando los caracteres y muestra ambas partes

    Pre: recibe una cadena de caracteres que representa la clave
    Post: imprime la primera parte y la segunda parte
    """
    lista1=[]
    lista2=[]
    for uno in range(len(clave)):
        if uno%2==0:
            lista1.append(clave[uno])
        else:
            lista2.append((clave[uno]))

    clave1="".join(lista1)
    clave2="".join(lista2)
    print(f"La primera parte de la clave es {clave1}")
    print(f"La segunda parte de la clave es {clave2}")

buscar_clave("18293")
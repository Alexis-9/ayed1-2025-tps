""" Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas
son recibidas en dos tuplas, por ejemplo: (3, 4) y (5, 4). La función devuelve True
o False. Escribir también un programa para verificar su comportamiento. Considerar
el uso de conjuntos para resolver este ejercicio.
"""

def domino(tup1,tup2):
    largo = 4

    conjunto1=set(tup1)
    if len(conjunto1)<2:
        largo-=1
    conjunto2=set(tup2)
    if len(conjunto2)<2:
        largo-=1

    return len(conjunto1.union(conjunto2))<largo

print(domino(("uno","dos"),("tres","uno")))
"""Escribir una función que reciba dos vectores en forma de tuplas y devuelva un valor
de verdad indicando si son ortogonales o no. Desarrollar también un programa que
permita verificar el comportamiento de la función. """

def ortogonal(tup1,tup2):
    return (tup1[0]*tup2[0] + tup1[1]*tup2[1])==0


print(ortogonal((2,3),(-3,2)))
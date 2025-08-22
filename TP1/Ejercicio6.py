"""Desarrollar una función que reciba como parámetros dos números enteros positivos
y devuelva como valor de retorno el número que resulte de concatenar ambos
parámetros. Por ejemplo, si recibe 1234 y 567 debe devolver 1234567. No se permite utilizar facilidades de Python no vistas en clase."""

def concatenar(primero, segundo):
    digitos = 0
    aux = segundo
    concatenado=0
    while aux > 0:
        aux = aux // 10
        digitos += 1
        concatenado= primero * (10 ** digitos) + segundo
    return concatenado

n1=int(input("Primer número: "))
n2=int(input("Segundo número: "))

print(concatenar(n1,n2))
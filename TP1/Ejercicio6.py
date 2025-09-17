"""Desarrollar una función que reciba como parámetros dos números enteros positivos
y devuelva como valor de retorno el número que resulte de concatenar ambos
parámetros. Por ejemplo, si recibe 1234 y 567 debe devolver 1234567. No se permite utilizar facilidades de Python no vistas en clase."""


def concatenar(a:int,b:int)->int:
    """
    Concatena dos números enteros y devuelve el número concatenado

    pre: a y b como números enteros
    post: Devuelve el resultado de concatenar a y b
    """
    digitos=0
    sobrante=b
    while sobrante>0:
        sobrante = sobrante // 10
        digitos+=1
    concatenado=a*(10**digitos)+b
    return concatenado

def ingresar_valores()->None:
    """
    Pide al usuario dos números enteros positivos e imprime su concatenación con la función concatenar
    pre: El usuario ingresa dos números enteros y en caso de ser negativos los vuelve a pedir
    post: Imprime el resultado de concatenar los dos números
    """
    n1=int(input("Primer número: "))
    n2=int(input("Segundo número: "))
    while n1<0 or n2<0:
        print("Ingrese números enteros positivos")
        n1 = int(input("Primer número: "))
        n2 = int(input("Segundo número: "))

    print(concatenar(n1,n2))

ingresar_valores()


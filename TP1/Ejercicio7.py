"""Escribir una función diasiguiente(dia, mes año) que reciba como parámetro una
fecha cualquiera expresada por tres enteros y calcule y devuelva otros tres enteros
correspondientes el día siguiente al dado. Utilizando esta función sin modificaciones
ni agregados, desarrollar programas que permitan:
a. Sumar N días a una fecha.
b. Calcular la cantidad de días existentes entre dos fechas cualesquiera"""

def fecha(dia:int, mes:int, anio:int)->tuple[bool,int]:
    """
    Verifica si una fecha es válida y si el año es bisiesto
    pre: dia, mes, anio como números enteros

    post:
    Devuelve una tupla (valida, bisiesto):
        valida (bool): True si la fecha es válida, False si no
        bisiesto (int): 1 si el año es bisiesto, 0 si no lo es
    """
    bisiesto=0
    if anio <= 0:
        return False,0

    if mes < 1 or mes > 12:
        return False,0

    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        dias_mes = 31
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        dias_mes = 30
    elif mes==2:
        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
            dias_mes = 29
            bisiesto=1
        else:
            dias_mes = 28
    if dia < 1 or dia > dias_mes:
        return False, bisiesto
    else:
        return True, bisiesto

def ingresar_valores()->tuple[int,int,int,int]:
    """
     Pide al usuario una fecha y devuelve la fecha validada junto con el indicador de bisiesto

     pre: El usuario debe ingresar día, mes y anio como números enteros

     Post:
     - Si la fecha es válida devuelve una tupla (dia, mes, anio, bisiesto)
     - Si la fecha es inválida, imprime un mensaje de error y vuelve a pedir los datos
     """
    dia = int(input("Ingrese el día: "))
    mes = int(input("Ingrese el mes: "))
    anio = int(input("Ingrese el año: "))

    validar,bisiesto=fecha(dia,mes,anio)
    if validar:
        return dia,mes,anio,bisiesto
    else:
        print("Error, la fecha es invalida")
        return ingresar_valores()

def diasiguiente(dia:int, mes:int, anio:int,bisiesto:int)->tuple[int,int,int]:
    """
    Calcula el día siguiente a una fecha dada

    pre:
    - dia, mes, anio como enteros que representan una fecha válida
    - bisiesto: 1 si el año es bisiesto, 0 si no

    post:
    - Devuelve una tupla (dia, mes, anio) correspondiente al día siguiente
    """
    if bisiesto==1:
        dias_mes = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dia += 1
    if dia > dias_mes[mes - 1]:
        dia = 1
        mes += 1
        if mes > 12:
            mes = 1
            anio += 1

    return dia, mes, anio


def sumar_dias(dia:int, mes:int, anio:int,bisiesto:int,n:int)->tuple[int,int,int]:
    """
    Devuelve la fecha resultante de sumar N días a una fecha dada

    pre:
    - dia, mes, anio como enteros que representan una fecha válida
    - bisiesto: 1 si el año es bisiesto, 0 si no
    - N: número de días a sumar

    Post:
    - Devuelve una tupla (dia, mes, anio) correspondiente a la fecha resultante después de sumar N días
    """
    for suma in range(n):
        dia, mes, anio = diasiguiente(dia, mes, anio,bisiesto)
    return dia, mes, anio

def verificar_mayor(d:int,m:int,a:int,d1:int,m2:int,a2:int)-> int:
    """
    Verifica entre dos fechas cual es mayor
    pre: Dos fechas con dia, mes y año como numeros enteros
    post: Devuelve 1 en caso de que la primer fecha sea mayor, 2 en caso de que la segunda sea mayor o 0 en caso de que sean iguales
    """

    if a > a2:
        return 1
    elif a < a2:
        return 2
    else:
        if m > m2:
            return 1
        elif m < m2:
            return 2
        else:
            if d > d1:
                return 1
            elif d < d1:
                return 2
            else:
                return 0

def dias_entre(fecha1: tuple[int, int, int, int], fecha2: tuple[int, int, int, int]) -> int:
    """
    Calcula la cantidad de días entre dos fechas.

    pre:
    - fecha1 y fecha2: tuplas (dia, mes, anio, bisiesto) que representan fechas válidas

    post:
    - Determina cual fecha es mayor
    - Devuelve un entero que representa la cantidad de días que hay desde la primer fecha hasta la segunda
    """
    dia1, mes1, anio1, bisiesto1 = fecha1
    dia2, mes2, anio2, bisiesto2 = fecha2

    mayor=verificar_mayor(dia1,mes1,anio1,dia2,mes2,anio2)
    if mayor==1:
        dia1, mes1, anio1, bisiesto1 = fecha2
        dia2, mes2, anio2, bisiesto2 = fecha1



    contador = 0

    while (dia1, mes1, anio1) != (dia2, mes2, anio2):
        if (anio1 % 4 == 0 and anio1 % 100 != 0) or (anio1 % 400 == 0):
            bisiesto1 = 1
        else:
            bisiesto1=0
        dia1, mes1, anio1 = diasiguiente(dia1, mes1, anio1,bisiesto1)
        contador += 1

    return contador



def opciones()->None:
    """
    Muestra una lista de opciones

    pre: No recibe nada

    Post: Imprime las opciones disponibles en pantalla

    """
    print("1: Día siguiente a la fecha ingresada")
    print("2: Sumar días a una fecha")
    print("3: Cantidad de días entre 2 fechas")
    print("4: Salir")

def menu()->None:
    """
    Muestra un menú con opciones ejecutables

    Pre: El usuario ingresa una opción como string

    Post:
    - Si la opción ingresada coincide con una opción la ejecuta, si no, muestra un mensaje de error
    - Imprime los resultados de cada función
    """
    opciones()
    op=input("Elija una opción: ")
    while op!="4":
        if op=="1":
            dia,mes,anio,bisiesto = ingresar_valores()
            dia,mes,anio = diasiguiente(dia, mes, anio, bisiesto)
            print(f"El día siguiente a la fecha ingresada es {dia}/{mes}/{anio}")

        elif op=="2":
            dia, mes, anio, bisiesto = ingresar_valores()
            dias_a_sumar = int(input("Cuantos días quieres sumar: "))
            dia,mes,anio = sumar_dias(dia,mes,anio,bisiesto,dias_a_sumar)
            print(f"Fecha después de sumar {dias_a_sumar} días: {dia}/{mes}/{anio}")

        elif op=="3":
            print("Fecha 1")
            dia, mes, anio, bisiesto = ingresar_valores()
            fecha1=dia,mes,anio,bisiesto

            print("Fecha 2")
            dia, mes, anio, bisiesto = ingresar_valores()
            fecha2=dia,mes,anio,bisiesto

            dias = dias_entre(fecha1,fecha2)
            print(f"Hay {dias} días entre las fechas")
        else:
            print("Opción incorrecta")
        print()
        op = input("Elija una opción: ")
    return "Adiós"

print(menu())

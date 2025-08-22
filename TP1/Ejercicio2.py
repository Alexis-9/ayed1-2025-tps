"""Desarrollar una función que reciba tres números enteros positivos correspondientes
al día, mes, año de una fecha y verifique si corresponden a una fecha válida. Debe
tenerse en cuenta la cantidad de días de cada mes, incluyendo los años bisiestos.
Devolver True o False según la fecha sea correcta o no. Realizar también un
programa para verificar el comportamiento de la función.
"""

def fecha(dia, mes, anio):
    if anio <= 0:
        return False

    if mes < 1 or mes > 12:
        return False

    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        dias_mes = 31
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        dias_mes = 30
    elif mes==2:
        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
            dias_mes = 29
        else:
            dias_mes = 28
    if dia < 1 or dia > dias_mes:
        return False
    else:
        return True

def ingresar_valores():
    dia = int(input("Ingrese el día: "))
    mes = int(input("Ingrese el mes: "))
    anio = int(input("Ingrese el año: "))

    if fecha(dia, mes, anio)==True:
        print("La fecha es válida")
    else:
        print("La fecha NO es válida")

ingresar_valores()
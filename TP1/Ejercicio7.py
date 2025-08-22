"""Escribir una función diasiguiente(dia, mes año) que reciba como parámetro una
fecha cualquiera expresada por tres enteros y calcule y devuelva otros tres enteros
correspondientes el día siguiente al dado. Utilizando esta función sin modificaciones
ni agregados, desarrollar programas que permitan:
a. Sumar N días a una fecha.
b. Calcular la cantidad de días existentes entre dos fechas cualesquiera"""

def fecha(dia, mes, anio):
    bisiesto=0
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
            bisiesto=1
        else:
            dias_mes = 28
    if dia < 1 or dia > dias_mes:
        return False, bisiesto
    else:
        return True, bisiesto

def ingresar_valores():
    dia = int(input("Ingrese el día: "))
    mes = int(input("Ingrese el mes: "))
    anio = int(input("Ingrese el año: "))

    validar,bisiesto=fecha(dia,mes,anio)
    if validar==True:
        return dia,mes,anio,bisiesto
    else:
        print("Error, la fecha es invalida")
        return ingresar_valores()

def diasiguiente(dia, mes, anio,bisiesto):
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


def sumar_dias(dia, mes, anio,bisiesto,N):
    for suma in range(N):
        dia, mes, anio = diasiguiente(dia, mes, anio,bisiesto)
    return dia, mes, anio

def dias_entre(fecha1, fecha2):
    dia1, mes1, anio1,bisiesto1 = fecha1
    dia2, mes2, anio2,bisiesto2= fecha2
    contador = 0

    while (dia1, mes1, anio1) != (dia2, mes2, anio2):
        if (anio1 % 4 == 0 and anio1 % 100 != 0) or (anio1 % 400 == 0):
            bisiesto1 = 1
        else:
            bisiesto1=0
        dia1, mes1, anio1 = diasiguiente(dia1, mes1, anio1,bisiesto1)
        contador += 1

    return contador



def opciones():
    print("1: Día siguiente a la fecha ingresada")
    print("2: Sumar días a una fecha")
    print("3: Cantidad de días entre 2 fechas")
    print("4: Salir")

def menu():
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
        print()
        op = input("Elija una opción: ")
    return "Adiós"

print(menu())

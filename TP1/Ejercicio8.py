"""La siguiente función permite averiguar el día de la semana para una fecha determinada.
La fecha se suministra en forma de tres parámetros enteros y la función devuelve 0 para domingo, 1 para lunes, 2 para martes, etc.
Escribir un programa para imprimir por pantalla el calendario de un mes completo, correspondiente a un mes
y año cualquiera basándose en la función suministrada.
Considerar que la semana comienza en domingo"""

def diadelasemana(dia,mes,anio):
    if mes<3:
        mes=mes+10
        anio=anio-1
    else:
        mes=mes-2
    siglo=anio//100
    anio2=anio%100
    diasem=(((26*mes-2)//10)+dia+anio2+(anio2//4)+(+siglo//4)-(2*siglo))%7
    if diasem<0:
        diasem = diasem+7
    return diasem

def fecha(dia, mes, anio):
    if anio <= 0:
        return False,0

    if mes < 1 or mes > 12:
        return False,0

    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        dias_mes = 31
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        dias_mes = 30
    else:
        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
            dias_mes = 29
        else:
            dias_mes = 28

    if dia < 1 or dia > dias_mes:
        return False,dias_mes
    else:
        return True,dias_mes


def calendario(dia_ingresado,mes_ingresado,anio_ingresado):
    dias_semana = ["Domingo", "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"]

    valido, dias_mes = fecha(1, mes_ingresado, anio_ingresado)

    inicio=diadelasemana(dia_ingresado,mes_ingresado,anio_ingresado)
    print(f"Estas en {dias_semana[inicio]}")

    for dia in range(1,dias_mes+1):
        nombre_dia = dias_semana[diadelasemana(dia, mes_ingresado, anio_ingresado)]
        print(f"{nombre_dia} {dia}")
        if diadelasemana(dia, mes_ingresado, anio_ingresado)==6:
            print()


def ingesar_valores():
    dia=int(input("Ingrese un día: "))
    mes=int(input("Ingrese un mes: "))
    anio=int(input("Ingrese un año: "))
    valido, dias_mes = fecha(dia, mes, anio)
    if not valido:
        print("Fecha inválida")
        return
    calendario(dia,mes,anio)
ingesar_valores()
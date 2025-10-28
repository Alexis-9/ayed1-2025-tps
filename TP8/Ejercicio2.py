"""Escribir una función que reciba como parámetro una tupla conteniendo una fecha
(día,mes,año) y devuelva una cadena de caracteres con la misma fecha expresada
en formato extendido. La función debe contemplarse que el año se ingrese en dos
dígitos, los que serán interpretados según un año de corte definido dentro del
programa. Cualquier año mayor que éste se considerará del siglo pasado. Por
ejemplo, si el año de corte fuera 30, la función devuelve "12 de Octubre de 2030"
para (12,10,30). Pero si la tupla fuera (25, 12, 31) devolverá "25 de Diciembre de
1931". Si el año se ingresa en cuatro dígitos el año de corte no será tenido en
cuenta. Escribir también un programa para ingresar los datos, invocar a la función y
mostrar el resultado.
"""


def fecha(tupla,corte)->str:
    """
    Verifica si una fecha es válida y si el año es bisiesto
    pre: dia, mes, anio como números enteros

    post:
    Devuelve una tupla (valida, bisiesto):
        valida (bool): True si la fecha es válida, False si no
        bisiesto (int): 1 si el año es bisiesto, 0 si no lo es
    """
    meses=["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio","Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

    dia,mes,anio=tupla

    bisiesto=0
    if anio <= 0:
        return "Fecha inválida"

    if anio < 100:
        if anio <= corte:
            anio += 2000
        else:
            anio += 1900

    if mes < 1 or mes > 12:
        return "Fecha inválida"

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
        return "Fecha inválida"
    else:
        return f"La fecha es {dia} de {meses[mes-1]} del {anio}"


def main():
    dia = int(input("Ingrese el día: "))
    mes = int(input("Ingrese el mes: "))
    anio = int(input("Ingrese el año: "))

    anio_de_corte=30
    tupla = (dia, mes, anio)

    print(fecha(tupla,anio_de_corte))


if __name__ == "__main__":
    main()
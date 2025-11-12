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


def fecha(tupla: tuple[int, int, int], corte: int) -> str:
    """
    Convierte una tupla de fecha (día, mes, año) en un string legible y valida la fecha,
    considerando años de dos dígitos según un corte

    Pre:
    - tupla contiene tres enteros: (día, mes, año)
    - corte es un entero que define el límite para interpretar años de dos dígitos
    - El día debe ser positivo, el mes entre 1 y 12, y el año entero

    Post:
    - Devuelve un string con la fecha en formato 'día de Mes del año' si es válida
    - Si la fecha es inválida, devuelve 'Fecha inválida'
    - Considera años bisiestos para febrero
    """


    meses=["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio","Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

    dia,mes,anio=tupla

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


def main() -> None:
    """
    Solicita al usuario ingresar una fecha y la muestra en formato legible

    Pre:
    - No recibe parámetros
    - El usuario debe ingresar números enteros para día, mes y año

    Post:
    - Llama a la función fecha para validar y formatear la fecha ingresada
    - Imprime por pantalla la fecha en formato 'día de Mes del año' o un mensaje de error si es inválida
    - No devuelve ningún valor
    """

    dia = int(input("Ingrese el día: "))
    mes = int(input("Ingrese el mes: "))
    anio = int(input("Ingrese el año: "))

    anio_de_corte=30
    tupla = (dia, mes, anio)

    print(fecha(tupla,anio_de_corte))


if __name__ == "__main__":
    main()
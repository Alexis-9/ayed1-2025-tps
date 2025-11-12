"""Desarrollar las siguientes funciones utilizando tuplas para representar fechas y horarios, y luego escribir un programa que las vincule:
a. Ingresar una fecha desde el teclado, verificando que corresponda a una fecha
válida.
b. Sumar N días a una fecha.
c. Ingresar un horario desde teclado, verificando que sea correcto.
d. Calcular la diferencia entre dos horarios. Si el primer horario fuera mayor al
segundo se considerará que el primero corresponde al día anterior. En ningún
caso la diferencia en horas puede superar las 24 horas.
"""

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





def ingresar_horario() -> tuple[int, int]:
    """
    Solicita al usuario ingresar una hora y un minuto, validando que estén en rangos correctos

    Pre:
    - No recibe parámetros
    - El usuario debe ingresar números enteros: hora (0-23) y minuto (0-59)

    Post:
    - Devuelve una tupla (hora, minuto) con los valores válidos ingresados
    - Si el usuario ingresa valores fuera de rango, solicita nuevamente el ingreso
    """

    hora = int(input("Ingrese la hora de 0 a 23: "))
    minuto = int(input("Ingrese los minutos: "))

    if 0<=hora and hora<=24 and 0<=minuto and minuto<=60:
        return hora, minuto
    else:
        print("Error, horario inválido")
        return ingresar_horario()


def diferencia_horarios(h1: int, m1: int, h2: int, m2: int) -> tuple[int, int]:
    """
    Calcula la diferencia entre dos horarios expresados en horas y minutos

    Pre:
    - h1, h2 son horas válidas (0-23)
    - m1, m2 son minutos válidos (0-59)

    Post:
    - Devuelve una tupla (horas, minutos) con la diferencia entre el segundo y el primer horario
    """

    minutos1 = h1 * 60 + m1
    minutos2 = h2 * 60 + m2

    if minutos1 > minutos2:
        minutos2 += 24 * 60

    diferencia = minutos2 - minutos1

    horas = diferencia // 60
    minutos = diferencia % 60
    return horas, minutos


def main() -> None:
    """
    Realiza operaciones con fechas y horarios

    Pre:
    - No recibe parámetros
    - El usuario debe ingresar valores válidos para fecha y horarios

    Post:
    - Solicita al usuario una fecha y un número de días para sumar, mostrando la nueva fecha
    - Solicita dos horarios y calcula la diferencia entre ellos
    - Imprime por pantalla la nueva fecha y la diferencia horaria
    - No devuelve ningún valor
    """

    dia, mes, anio, bisiesto = ingresar_valores()
    n = int(input("Cuántos días desea sumar: "))
    dia, mes, anio = sumar_dias(dia, mes, anio, bisiesto, n)
    print(f"La nueva fecha es {dia}/{mes}/{anio}")


    print("Ingrese el primer horario:")
    hora1, min1 = ingresar_horario()
    print("Ingrese el segundo horario:")
    hora2, min2 = ingresar_horario()

    horas, minutos = diferencia_horarios(hora1, min1, hora2, min2)
    print(f"Diferencia: {horas} horas y {minutos} minutos.")


if __name__ == "__main__":
    main()

"""Resolver el siguiente problema, utilizando funciones:
Se desea llevar un registro de los socios que visitan un club cada día. Para ello, se
ingresa el número de socio de cinco dígitos hasta ingresar un cero como fin de carga.

Se solicita:
a. Informar para cada socio, cuántas veces ingresó al club. Cada socio debe
aparecer una sola vez en el informe.

b. Solicitar un número de socio que se dio de baja del club y eliminar todos sus
ingresos. Mostrar los registros de entrada al club antes y después de
eliminarlo. Informar cuántos ingresos se eliminaron."""


def cargar_ingresos() -> list[int]:
    """
    Permite registrar los ingresos de socios de un club

    Pre: El usuario ingresa números de socio de 5 dígitos o 0 para terminar

    Post: Devuelve una lista de números de socio válidos ingresados
    """
    ingresos = []
    socio = int(input("Ingrese número de socio (0 para terminar): "))
    while socio != 0:
        if socio>=10000 and socio<= 99999:
            ingresos.append(socio)
        else:
            print("Número inválido. Debe ser de 5 dígitos.")
        socio = int(input("Ingrese número de socio (0 para terminar): "))
    return ingresos

def contar_ingresos(ingresos: list[int]) -> tuple[list[int], list[int]]:
    """
    Cuenta cuántas veces ingresó cada socio a un club

    Pre:
    - ingresos: lista de números de socio

    Post:
    - Devuelve una tupla de listas:
        socios: lista de socios únicos
        cantidades: lista de la cantidad de ingresos correspondiente a cada socio
    """
    socios = []
    for s in ingresos:
        if s not in socios:
            socios.append(s)

    cantidades = []
    for i in socios:
        cantidad=ingresos.count(i)
        cantidades.append(cantidad)
    return socios,cantidades

def mostrar_registros(socios: list[int], cantidades: list[int]) -> None:
    """
    Muestra en pantalla los socios y la cantidad de veces que ingresaron al club

    Pre:
    - socios: lista de números de socio únicos
    - cantidades: lista de cantidad de ingresos correspondiente a cada socio

    Post: Imprime en pantalla cada socio junto a su cantidad de ingresos
    """

    for i in range(len(socios)):
        print(f"Socio:{socios[i]} | Ingresos: {cantidades[i]}")


def eliminar_socio(ingresos: list[int], eliminar: int) -> tuple[list[int], int]:
    """
    Elimina todas las apariciones de un socio de la lista de ingresos

    Pre:
    - ingresos: lista de números de socio
    - eliminar: número de socio a eliminar

    Post:
    - Devuelve una tupla:
        nueva_lista: lista de ingresos sin el socio eliminado
        cantidad: número de veces que el socio eliminado estaba en la lista
    """
    cantidad = ingresos.count(eliminar)
    nueva_lista = [s for s in ingresos if s != eliminar]
    return nueva_lista, cantidad



def main() -> None:
    """
    Programa para registrar ingresos de socios, mostrar registros y eliminar ingresos de un socio

    Pre: Se ingresan números de socio de 5 dígitos hasta ingresar 0 para finalizar

    Post:
    - Muestra la cantidad de ingresos de cada socio
    - Permite eliminar ingresos de un socio y muestra los registros actualizados
    """
    ingresos = cargar_ingresos()

    socio,cantidad=contar_ingresos(ingresos)
    mostrar_registros(socio,cantidad)

    socio_a_eliminar = int(input("Ingrese el número de socio dado de baja: "))
    ingresos_nuevos, cant_eliminado = eliminar_socio(ingresos,socio_a_eliminar)
    print(f"Se eliminaron {cant_eliminado} ingresos del socio {socio_a_eliminar}.")
    socio,cantidad = contar_ingresos(ingresos_nuevos)
    mostrar_registros(socio,cantidad)

main()

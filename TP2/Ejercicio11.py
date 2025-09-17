"""Resolver el siguiente problema, diseñando las funciones a utilizar:
Una clínica necesita un programa para atender a sus pacientes. Cada paciente que
ingresa se anuncia en la recepción indicando su número de afiliado (número entero
de 4 dígitos) y además indica si viene por una urgencia (ingresando un 0) o con
turno (ingresando un 1). Para finalizar se ingresa -1 como número de socio. Luego
se solicita:

a. Mostrar un listado de los pacientes atendidos por urgencia y un listado de
los pacientes atendidos por turno en el orden que llegaron a la clínica.

b. Realizar la búsqueda de un número de afiliado e informar cuántas veces fue
atendido por turno y cuántas por urgencia. Repetir esta búsqueda hasta
que se ingrese -1 como número de afiliado. """

def ingresar_pacientes() -> tuple[list[int], list[int]]:
    """
    Permite ingresar pacientes con número de afiliado y tipo de atención

    Pre:
    - El usuario ingresa números de afiliado de 4 dígitos o -1 para terminar
    - El usuario ingresa 0 para urgencia o 1 para turno

    Post:
    - Devuelve una tupla de dos listas:
        afiliados: lista de números de afiliados ingresados
        turno: lista de situaciones correspondientes (0: urgencia, 1: turno).
    """
    afiliados=[]
    turno=[]

    afiliado = int(input("Ingrese número de afiliado (-1 para terminar) : "))
    while afiliado < 1000 or afiliado > 9999:
        print("Número de afiliado inválido. Debe ser de 4 dígitos.")
    while afiliado!=-1:
        situacion = int(input("Ingrese 0 si es urgencia o 1 si tiene turno: "))
        while situacion!=1 and situacion!=0:
            situacion = int(input("Ingrese 0 si es urgencia o 1 si tiene turno: "))

        afiliados.append(afiliado)
        turno.append(situacion)
        afiliado = int(input("Ingrese número de afiliado (-1 para terminar) : "))
    return afiliados, turno

def mostrar_listado(afiliados: list[int], turno: list[int]) -> None:
    """
    Muestra los pacientes atendidos por urgencia y por turno

    Pre:
    - afiliados: lista de números de afiliado
    - turno: lista de enteros indicando 0 para urgencia y 1 para turno

    Post: Imprime en pantalla los pacientes que fueron atendidos por urgencia y por turno
    """
    urgencia=[afiliados[i] for i, x in enumerate(turno) if x == 0]
    turnos=[afiliados[i] for i, x in enumerate(turno) if x == 1]


    print("Pacientes atendidos por urgencia: ")
    for paciente in urgencia:
        print(paciente, end="-")

    print()
    print("Pacientes atendidos por turno: ")
    for paciente in turnos:
        print(paciente, end="-")
    print()


def buscar_afiliado(afiliados: list[int], turno: list[int]) -> None:
    """
    Permite consultar cuántas veces un afiliado fue atendido por urgencia y por turno

    Pre:
    - afiliados: lista de números de afiliado
    - turno: lista de enteros indicando 0 para urgencia y 1 para turno

    Post:
    - Solicita al usuario el número de afiliado a buscar
    - Imprime cuántas veces fue atendido por urgencia y por turno
    - Repite la búsqueda hasta que el usuario ingrese -1
    """
    n_afiliado = int(input("Ingrese número de afiliado a buscar (-1 para terminar): "))
    veces_urgencia=0
    veces_turno=0
    while n_afiliado!=-1:
        for i,x in enumerate(afiliados):
            if x==n_afiliado:
                if turno[i]==0:
                    veces_urgencia+=1
                else:
                    veces_turno+=1
        print(f"El afiliado {n_afiliado} fue atendido {veces_urgencia} veces por urgencia y {veces_turno} veces por turno.")
        n_afiliado = int(input("Ingrese número de afiliado a buscar (-1 para terminar): "))


def main() -> None:
    """
    Menú de opciones ejecutables

    Pre: El usuario ingresa una opción como string

    Post:
    - Si la opción ingresada coincide con una opción la ejecuta, si no, muestra un mensaje de error
    - Imprime los resultados de cada función
    """
    afiliados = []
    turnos = []
    print("1: Ingresar pacientes")
    print("2: Mostrar listados")
    print("3: Buscar afiliado")
    print("4: Limpiar lista de pacientes")
    print("5: Salir")
    op=input("Seleccione una opción: ")

    while op!="5":
        if op=="1":
            mas_afiliados, mas_turnos = ingresar_pacientes()
            afiliados.extend(mas_afiliados)
            mas_turnos.extend(mas_turnos)
        elif op=="2":
            if len(afiliados)!=0:
                mostrar_listado(afiliados, turnos)
            else:
                print("No hay pacientes cargados.")
        elif op=="3":
            if len(afiliados)!=0:
                buscar_afiliado(afiliados, turnos)
            else:
                print("No hay pacientes cargados.")
        elif op=="4":
            afiliados = []
            turnos = []
            print("Lista vacía")
        else:
            print("Opción inválida. Intente de nuevo.")

        print("1: Ingresar pacientes")
        print("2: Mostrar listados")
        print("3: Buscar afiliado")
        print("4: Limpiar lista de pacientes")
        print("5: Salir")
        op = input("Seleccione una opción: ")

main()
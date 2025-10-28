def crear_matriz():
    matriz=[]
    for fila in range(1):
        for columna in range(3):
            matriz.append([])
    return matriz


def cargar_datos(alumnos):
    cargar_legajo=int(input("Legajo: "))
    edad_alumno=int(input("Edad: "))
    curso=int(input("Año: "))
    while verificar(cargar_legajo,edad_alumno,curso,alumnos)==False:
        cargar_legajo = int(input("Legajo: "))
        edad_alumno = int(input("Edad: "))
        curso = int(input("Año: "))

    alumnos[0].append(cargar_legajo)
    alumnos[1].append(edad_alumno)
    alumnos[2].append(curso)


def verificar(legajo,alumno,curso,alumnos):
    if legajo<10001 or legajo>99999:
        print("Legajo fuera de rangos")
        return False

    for i in range(len(alumnos[0])):
        if alumnos[0][i]==legajo:
            print("Legajo repetido")
            return False

    if alumno<18 or alumno>100:
        print("Edad invalida")
        return False
    if curso<1 or curso>4:
        print("Año de curso invalido")
        return False
    return True

def buscar_menor(matriz):
    if len(matriz[0])!=0:
        legajo = matriz[0][0]
        menor=matriz[1][0]
        curso=matriz[2][0]
        for i in range(len(matriz[1])):
            if menor > matriz[1][i]:
                menor = matriz[1][i]
                legajo = matriz[0][i]
                curso = matriz[2][i]
        print("Alumno más joven:")
        print("Legajo:", legajo)
        print("Edad:", menor)
        print("Curso:", curso)
    else:
        print("No se ingresaron alumnos")


def buscar_mayor(matriz):
    if len(matriz[0]) != 0:
        mayor=matriz[1][0]
        legajo=matriz[0][0]
        curso=matriz[2][0]
        for i in range(len(matriz[1])):
            if mayor<matriz[1][i]:
                mayor=matriz[1][i]
                legajo=matriz[0][i]
                curso=matriz[2][i]
        print("Alumno más adulto:")
        print("Legajo:", legajo)
        print("Edad:", mayor)
        print("Curso:", curso)
    else:
        print("No se ingresaron alumnos")

def alumnos_curso(alumnos):
    for curso in range(1,5):
        cantidad = 0
        for i in range(len(alumnos[2])):
            if alumnos[2][i]==curso:
                cantidad+=1
        print(f"Para el curso {curso} hay {cantidad} alumnos")

def promedio_edad(alumnos):
    cantidad=0
    edades=0
    for edad in range(len(alumnos[2])):
        if alumnos[1][edad]<=30:
            cantidad+=1
            edades+=alumnos[1][edad]
    if cantidad==0:
        print("No hay alumnos menores a 30 años")
    else:
        promedio=edades/cantidad
        print(f"Hay {cantidad} alumnos menores a 30 y el promedio de edad es de {promedio}")


def opciones():
    print("1:Carga de alumnos")
    print("2:Buscar alumno de menor edad")
    print("3:Buscar alumno de mayor edad")
    print("4:Mostrar cantidad de alumnos por año")
    print("5:Promedio de edad de alumnos menores a 30 ")
    print("6:Salir")

def menu():
    opciones()
    op = input("Ingrese una opción: ")
    print()
    alumnos = crear_matriz()
    while op != "6":
        if op == "1":
            cargar_datos(alumnos)
        elif op == "2":
            buscar_menor(alumnos)
        elif op == "3":
            buscar_mayor(alumnos)
        elif op == "4":
            alumnos_curso(alumnos)
        elif op == "5":
            promedio_edad(alumnos)
        else:
            print("error")
        print()
        opciones()
        op = input("Ingrese una opción: ")
        print()

menu()
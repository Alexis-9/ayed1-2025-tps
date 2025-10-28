def crear_matriz():
    matriz=[]
    for filas in range(3):
        fila=[]
        for columna in range(3):
            fila.append([])
        matriz.append(fila)
    return matriz

def buscar_codigo():
    carrera = int(input("Ingrese una carrera: 1-Mat 2-Lit 3-Hist: "))
    while carrera < 1 or carrera > 3:
        print("Error en codigo de curso")
        carrera = int(input("Elija un curso 1-Matematica 2-Literatura 3-Historia: "))
    return carrera

def validar_ingreso():
    comision = int(input("Ingrese una comision 1-A 2-B 3-C: "))
    while comision < 1 or comision > 3:
        print("Error")
        comision = int(input("Elija una comision de 1 a 3: "))
    return comision

def validar_cantidad(cantidad):
    while cantidad == 0 or cantidad < -1 or cantidad > 20:
        print("Error, ingrese una cantidad válida")
        cantidad = int(input("Ingrese la cantidad de alumnos que desea ingresar(-1 para terminar): "))
    return cantidad

def legajo_repetido(legajo,carreras):
    if legajo <= 0:
        return True
    for i in range(len(carreras)):
        for j in range(len(carreras[i])):
            for k in range(len(carreras[i][j])):
                if legajo==carreras[i][j][k]:
                    return True
    return False

def validar_total(carrera,comision,carreras):
    if len(carreras[carrera-1][comision-1])>19:
        return False
    else:
        return True


def cargar_comisiones(carrera,comision,carreras):
    cantidad=int(input("Ingrese la cantidad de alumnos que desea ingresar(-1 para terminar): "))
    cantidad = validar_cantidad(cantidad)
    while cantidad != -1:
        for alu in range(cantidad):
            if validar_total(carrera,comision,carreras)==False:
                print("Ya hay el máximo de estudiantes en esta comisión")
                return carreras
            else:
                legajo=int(input(f"Legajo del alumno {alu+1}: "))
                while legajo_repetido(legajo,carreras)==True:
                    print("Ese legajo ya fue ingresado o es un valor incorrecto")
                    legajo=int(input(f"Legajo del alumno {alu+1}: "))
                carreras[carrera-1][comision-1].append(legajo)

        cantidad=int(input("Ingrese la cantidad de alumnos que desea ingresar(-1 para terminar): "))
        cantidad = validar_cantidad(cantidad)
    return carreras

def cargar_codigos(carreras):
    carrera=buscar_codigo()
    comision=validar_ingreso()
    carreras=cargar_comisiones(carrera, comision, carreras)
    return carreras

def sin_inscriptos(carreras):
    lista=[]
    for i in range(len(carreras)):
        cursos_vacios=0
        for j in range(len(carreras[i])):
            if len(carreras[i][j])==0:
                cursos_vacios+=1
            if cursos_vacios==3:
                if i==0:
                    lista.append("Matematica")
                elif i==1:
                    lista.append("Literatura")
                elif i==2:
                    lista.append("Historia")
    return f"Los cursos vacios son: {lista}"

def mas_inscriptos(carreras):
    cantidades=[]
    cursos=["Matematica","Literatura","Historia"]
    for i in range(len(carreras)):
        cantidad=0
        for j in range(len(carreras[i])):
            cantidad+=len(carreras[i][j])
        cantidades.append(cantidad)

    mayor=cantidades[0]

    for x in range(len(cantidades)):
        if mayor<cantidades[x]:
            mayor=cantidades[x]

    cursos_mayores=[]
    if mayor==0:
        return f"No se ingresaron alumnos"
    else:
        for may in range(len(cantidades)):
            if mayor==cantidades[may]:
                cursos_mayores.append(cursos[may])
    if len(cursos_mayores)==1:
        return f"El curso con más alumnos es {cursos_mayores}"
    else:
        return f"Los cursos con más alumnos son: {cursos_mayores}"

def menos_de_diez(carreras):
    comisiones=[]
    for i in range(len(carreras)):
        for j in range(len(carreras[i])):
            if len(carreras[i][j])<10:
                comisiones.append(f"({i+1},{j+1})")
    return f"Las comisiones con menos de 10 inscriptos son: {comisiones}"

def opciones():
    print("1:Cargar alumnos")
    print("2:Mostrar cursos sin inscriptos ")
    print("3:Mostrar curso con más inscriptos ")
    print("4:Mostrar comisiones con menos de 10 alumnos ")
    print("5:Salir ")
    print("6:Mostrar Listas de alumnos")

def menu():
    carreras=crear_matriz()
    opciones()
    print()
    op = input("Ingrese una opción: ")
    print()
    while op!="5":
        if op=="1":
            carreras=cargar_codigos(carreras)
        elif op=="2":
            print(sin_inscriptos(carreras))
        elif op=="3":
            print(mas_inscriptos(carreras))
        elif op=="4":
            print(menos_de_diez(carreras))
        elif op=="6":
            print(carreras)
        else:
            print("Opción incorrecta")
        print()
        opciones()
        op = input("Ingrese una opción: ")
        print()
    print("Adiós")

menu()



def GrabarRangoAlturas() -> None:
    """
    Pide deportes y alturas de atletas y los guarda en un archivo de texto con un formato ordenado

    Pre:
    - No recibe parámetros
    - El usuario debe ingresar nombres de deportes y alturas válidas
    - Se crea o sobrescribe el archivo alturas.txt

    Post:
    - Genera un archivo alturas.txt con los deportes ingresados y las alturas de sus atletas
    - Finaliza cuando el usuario ingresa 0 en deporte o 0 como altura de atleta
    - No devuelve ningún valor
    """

    with open("alturas.txt", "w", encoding="utf-8") as archivo:
        indice_deporte=0
        while True:

            deporte = input("Ingrese deporte (0 Para salir): ").strip().title()
            while not deporte:
                print("El deporte no puede estar vacío")
                deporte = input("Ingrese deporte (0 Para salir): ").strip().title()

            if deporte =="0":
                archivo.write("\n")
                break

            indice_deporte+=1
            archivo.write(f"Deporte {indice_deporte} : {deporte}\n")
            atleta = 0

            while True:

                while True:
                    try:
                        altura = int(input("Ingrese altura del atleta en centimetros (-1 Para cambiar de deporte | 0 Para terminar): "))
                        if altura>280 or altura<100 and altura not in (-1,0):
                            print("Ingrese una altura válida")
                        else:
                            break
                    except ValueError:
                        print("Debe ingresar un número entero")

                atleta+=1
                if altura == -1:
                    archivo.write("\n")
                    break
                elif altura == 0:
                    break
                archivo.write(f"Altura del atleta {atleta} : {altura}\n")
            if altura == 0:
                archivo.write("\n")
                break


def GrabarPromedio() -> None:
    """
    Lee las alturas registradas en alturas.txt, calcula el promedio por deporte y los guarda en un archivo

    Pre:
    - Debe existir un archivo alturas.txt con el formato generado por la función GrabarRangoAlturas()
    - El archivo debe contener al menos un deporte con atletas para que haya promedios
    - No recibe parámetros


    Post:
    - Calcula el promedio de alturas de cada deporte encontrado
    - Muestra los promedios por pantalla
    - Genera un archivo promedios.txt con los promedios calculados
    - Si no hay datos válidos, crea un archivo vacío y avisa
    - No devuelve ningún valor
    """

    with open("alturas.txt", "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()


    altura = 0
    cantidad_atletas=0
    deporte=""
    nombre_deporte = ""
    promedios=[]


    for linea in lineas:
        linea = linea.strip()

        if linea == "":
            if cantidad_atletas>0:
                promedio = altura//cantidad_atletas
                promedios.append(f"{deporte}\nPromedio de alturas {nombre_deporte} : {promedio}")
                altura = 0
                cantidad_atletas = 0


        if linea.startswith("Deporte"):
            deporte = linea
            nombre_deporte= deporte.split(":")[1].strip()


        if linea.startswith("Altura"):
            cantidad_atletas+=1
            altura += int(linea.split(":")[1].strip())

    if not promedios:
        print("No hay datos cargados")
        with open("promedios.txt", "w", encoding="utf-8") as salida:
            salida.write("")
        return

    print("Promedios calculados:\n")
    for p in promedios:
        print(f"{p} cm")

    with open("promedios.txt", "w", encoding="utf-8") as salida:
        for p in promedios:
            salida.write(f"{p}\n\n")


def MostrarMasAltos() -> None:
    """
    Lee los promedios por deporte desde promedios.txt y muestra cuáles superan el promedio general

    Pre:
    - Debe existir un archivo promedios.txt con el formato generado por la función GrabarPromedio()
    - El archivo debe contener al menos un deporte con su promedio de altura
    - No recibe parámetros


    Post:
    - Calcula el promedio general de alturas entre todos los deportes
    - Muestra por pantalla qué deportes superan ese promedio y por cuánto
    - Si no hay promedios cargados, lo informa
    - No devuelve ningún valor
    """

    with open("promedios.txt", "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()


    promedio_suma = 0
    promedios=[]
    nombres = []
    superior_promedio=[]

    for linea in lineas:
        linea = linea.strip()

        if linea.startswith("Deporte"):
            nombres.append(linea.split(":")[1].strip())

        elif linea.startswith("Promedio"):
            promedio = int(linea.split(":")[1].strip())
            promedios.append(promedio)
            promedio_suma += promedio


    if not promedios:
        print("No hay datos cargados")
        return

    promedio_total=promedio_suma//len(promedios)

    print(f"Promedio general de alturas: {promedio_total} cm\n")

    for i,prom in enumerate(promedios):
        if prom>promedio_total:
            superior_promedio.append(f"{nombres[i]} Supera el promedio general por : {prom - promedio_total} cm")

    if not superior_promedio:
        print("Ningun deporte supera el promedio de altura")
    else:
        for deportes in superior_promedio:
            print(deportes)


def main() -> None:
    """
    Carga alturas, calcula promedios y muestra los deportes que superan el promedio general

    Pre:
    - Depende de que las funciones GrabarRangoAlturas, GrabarPromedio y MostrarMasAltos estén definidas correctamente
    - No recibe parámetros


    Post:
    - Llama a las tres funciones principales del programa
    - Imprime separadores despúes de cada función
    - No devuelve ningún valor
    """

    GrabarRangoAlturas()
    print("====================================================")
    GrabarPromedio()
    print("====================================================")
    MostrarMasAltos()

if __name__ == '__main__':
    main()
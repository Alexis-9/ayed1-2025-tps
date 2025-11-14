"""Escribir un programa que permita dividir un archivo de texto cualquiera en partes
que se puedan enviar por correo electrónico. El tamaño máximo de las partes se
ingresa por teclado. Los nombres de los archivos generados deben respetar el
nombre original con el agregado de un sufijo que indique de qué parte se trata.
Tener en cuenta que ningún registro puede ser dividido; la partición debe efectuarse después del delimitador del mismo. Mostrar un mensaje de error si el proceso no
pudiera llevarse a cabo. Recordar que no se permite cargar el archivo completo en memoria.
"""

def dividir_archivo():
    while True:
        try:
            max_caracteres=30#int(input("Ingrese la cantidad máxima de carácteres que puede tener una parte: "))
            break
        except ValueError:
            print("Debe ingresar un número entero")


    nombre_archivo="prueba.txt"#input("Ingrese el nombre del archivo: ").strip()

    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            if not lineas:
                print("El archivo esta vacío")
                return

        nombre = nombre_archivo.rsplit(".", 1)[0]
        largo=0
        parte=1
        parte_nueva = open(f"{nombre}_parte{parte}.txt", "w", encoding="utf-8")

        for linea in lineas:
            caracteres=len(linea.strip())

            if caracteres + largo<= max_caracteres:
                parte_nueva.write(linea)
                largo+=caracteres
            else:
                parte_nueva.close()
                parte+=1
                parte_nueva = open(f"{nombre}_parte{parte}.txt", "w", encoding="utf-8")
                parte_nueva.write(linea)
                largo=caracteres

        print("Archivo dividido correctamente")

    except Exception as e:
        print(f"Error al dividir archivo: {e}")

dividir_archivo()
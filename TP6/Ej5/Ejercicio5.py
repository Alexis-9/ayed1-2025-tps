"""Se dispone de dos formatos diferentes de archivos de texto en los que se almacenan datos de empleados, detallados más abajo.
Desarrollar un programa para convertir cada uno de los formatos suministrados, grabando los datos obtenidos en
otro archivo con formato CSV. Los archivos de entrada pueden generarse con Block
de Notas o cualquier otro editor, copiando y pegando los ejemplos proporcionados.
Ambos archivos tienen tres campos por registro: Apellido y Nombre, Fecha de alta
y Domicilio."""


def formato1(linea: str) -> list[str]:
    """
    Separa una línea de texto en nombre, fecha y dirección usando la posición del primer dígito como referencia

    Pre:
    - Recibe una cadena con un nombre seguido de una fecha de 8 dígitos y luego una dirección
    - La línea debe contener al menos un dígito para detectar el inicio de la fecha

    Post:
    - Devuelve una lista con los campos: nombre, fecha y dirección
    - Los campos se devuelven sin espacios sobrantes
    - La fecha se toma como los 8 caracteres consecutivos desde el primer dígito encontrado
    """

    indice = 0
    while indice < len(linea) and not linea[indice].isdigit():
        indice += 1

    nombre = linea[:indice].strip()
    fecha = linea[indice:indice+8].strip()
    direccion = linea[indice+8:].strip()

    return [nombre, fecha, direccion]


def formato2(linea: str) -> list[str]:
    """
    Extrae campos de una línea donde cada campo empieza con dos dígitos que indican su longitud

    Pre:
    - Recibe una cadena donde cada campo está formado por: dos dígitos de longitud y el texto del campo
    - La línea debe respetar ese formato para poder separarse bien

    Post:
    - Devuelve una lista con todos los campos extraídos en el orden en que aparecen
    - Avanza por la línea leyendo primero el largo y después el contenido del campo
    -Funciona incluso si se agregan más campos
    """

    campos=[]
    posicion=0
    while posicion +2 <= len(linea):
        largo=int(linea[posicion:posicion+2])
        posicion+=2

        campos.append(linea[posicion:posicion+largo])

        posicion+=largo

    return campos


def main() -> None:
    """
    Lee un archivo, separa sus líneas según dos formatos distintos y genera un CSV con el resultado

    Pre:
    - No recibe parámetros
    - Debe existir un archivo con el nombre ingresado (#Yo use Ejemplos.txt, deje comentado el input) y debe tener contenido
    - Cada línea del archivo debe pertenecer al formato 1 o al formato 2
    - formato1() y formato2() deben estar definidas

    Post:
    - Clasifica las líneas del archivo según si empiezan con dos dígitos o no
    - Genera un archivo resultado.csv con dos secciones: Formato 1 y Formato 2
    - Escribe cada línea procesada separada por comas
    - Muestra un mensaje indicando que el CSV fue creado
    - No devuelve ningún valor
    """

    archivo="Ejemplos.txt" #input("Ingrese el nombre del archivo: ")
    try:
        with open(archivo, "r", encoding="utf-8") as arch:
            lineas=arch.readlines()
            if not lineas:
                print("El archivo esta vacío")
                return
    except Exception:
        print("No se encontró el archivo")
        return

    lista_formato1=[]
    lista_formato2=[]

    for linea in lineas:
        linea=linea.strip()

        if not linea:
            continue
        elif len(linea)>=2 and linea[0].isdigit() and linea[1].isdigit():
            lista_formato2.append(formato2(linea))
        else:
            lista_formato1.append(formato1(linea))

    try:
        with open("resultado.csv", "w", encoding="utf-8") as resultado:

            resultado.write("Formato 1\n")
            for linea in lista_formato1:
                resultado.write(f"{",".join(linea)}\n") #Cambiando esta línea se cambía el formato en el csv

            resultado.write("\nFormato 2\n")
            for linea in lista_formato2:
                resultado.write(f"{",".join(linea)}\n")  #Cambiando esta línea se cambía el formato en el csv

            print("Archivo creado como resultado.csv")

    except Exception:
        print("No se pudo crear el archivo")





if __name__ == '__main__':
    main()



"""Escribir un programa que lea un archivo de texto conteniendo un conjunto de apellidos y nombres en formato "Apellido, Nombre" y guarde en el archivo
ARMENIA.TXT los registros de aquellas personas cuyo apellido termina con la cadena "IAN", en el archivo ITALIA.TXT los terminados en "INI" y en ESPAÑA.TXT los
terminados en "EZ". Descartar el resto."""


"""Arslanian, Gustavo –> ARMENIA.TXT
Rossini, Giuseppe –> ITALIA.TXT
Pérez, Juan –> ESPAÑA.TXT
Smith, John –> descartar"""


try:
    arch = open('Nombres.txt', 'rt', encoding='utf-8')
    armenia = open("ARMENIA.TXT", "wt", encoding="utf-8")
    espania = open("ESPAÑA.TXT", "wt", encoding="utf-8")
    italia = open("ITALIA.TXT", "wt", encoding="utf-8")

    while True:
        linea = arch.readline()

        if not linea:
            break
        else:
            apellido, nombre = linea.strip().split(',')
            apellido = apellido.strip().lower()
            nombre = nombre.strip()

            if not apellido:
                print("Error")
            elif apellido.endswith("ian"):
                armenia.write(f"{apellido.title()}, {nombre.title()}\n")
            elif apellido.endswith("ez"):
                espania.write(f"{apellido.title()}, {nombre.title()}\n")
            elif apellido.endswith("ini"):
                italia.write(f"{apellido.title()}, {nombre.title()}\n")



except FileNotFoundError as msg:
    print(f'No se encuentra el archivo: {msg}')
except OSError as msg:
    print(f'No se puede leer el archivo: {msg}')
else:
    print(f'Archivo leído correctamente\n')
finally:
    try:
        arch.close()
        armenia.close()
        italia.close()
        espania.close()
    except NameError:
        pass

with open("ARMENIA.TXT", "rt", encoding="utf-8") as arm:
    print("Los apellidos que terminan en ian: ")
    print(arm.read())

with open("ESPAÑA.TXT", "rt", encoding="utf-8") as es:
    print("Los apellidos que terminan en ez: ")
    print(es.read())
with open("ITALIA.TXT", "rt", encoding="utf-8") as it:
    print("Los apellidos que terminan en ini: ")
    print(it.read())


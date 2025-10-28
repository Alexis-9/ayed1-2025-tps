"""Se solicita crear un programa para leer direcciones de correo electrónico y verificar si representan una dirección válida. Por ejemplo usuario@dominio.com.ar.
Para que una dirección sea considerada válida el nombre de usuario debe poseer solamente
caracteres alfanuméricos, la dirección contener un solo carácter @, el dominio debe
tener al menos un carácter y tiene que finalizar con .com o .com.ar.

Repetir el proceso de validación hasta ingresar una cadena vacía. Al finalizar mostrar un listado de todos los dominios, sin repetirlos y ordenados alfabéticamente,
recordando que las direcciones de mail no distinguen mayúsculas ni minúsculas"""

def es_correo_valido(correo: str) -> str:
    """
    """
    correo = correo.lower()

    if correo.count('@') != 1:
        return ""

    usuario,dominio = correo.split('@')

    if not usuario.isalnum():
        return ""

    dominios = dominio.split(".")
    for dom in dominios:
        if not dom:
            return ""

    if dominio[-4:] != ".com" and dominio[-7:] != ".com.ar":
        return ""

    return dominio

def main():
    dominios = set()

    while True:
        correo = input("Ingrese una dirección de correo (Enter para salir): ")
        if correo == "":
            break

        if es_correo_valido(correo):
            dominio = es_correo_valido(correo)
            dominios.add(dominio)
            print("Correo válido")
        else:
            print("Correo inválido")

    if dominios:
        for i,dom in enumerate(sorted(dominios)):
            print(f"{i+1}- {dom}")
    else:
        print("No se ingresaron correos válidos")


if __name__ == "__main__":
    main()

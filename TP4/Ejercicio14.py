"""Se solicita crear un programa para leer direcciones de correo electrónico y verificar si representan una dirección válida. Por ejemplo usuario@dominio.com.ar.
Para que una dirección sea considerada válida el nombre de usuario debe poseer solamente
caracteres alfanuméricos, la dirección contener un solo carácter @, el dominio debe
tener al menos un carácter y tiene que finalizar con .com o .com.ar.

Repetir el proceso de validación hasta ingresar una cadena vacía. Al finalizar mostrar un listado de todos los dominios, sin repetirlos y ordenados alfabéticamente,
recordando que las direcciones de mail no distinguen mayúsculas ni minúsculas"""

def es_correo_valido(correo: str) -> str:
    """
    Verifica si un correo electrónico tiene un formato válido según reglas básicas

    Pre:
    - correo es una cadena de caracteres que representa una dirección de correo electrónico

    Post:
    - Devuelve la parte del dominio si el correo es válido
    - Devuelve una cadena vacía "" si el correo no cumple las condiciones de validez:
        - Contiene exactamente un '@'
        - La parte del usuario es alfanumérica
        - No hay dominios vacíos entre puntos
        - El dominio termina en '.com' o '.com.ar'
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

def main() -> None:
    """
    Solicita direcciones de correo al usuario,
    valida cada correo y muestra los dominios únicos ingresados

    Pre:
    - No recibe parámetros
    - El usuario puede ingresar múltiples correos o presionar Enter para finalizar

    Post:
    - Llama a la función es_correo_valido para verificar cada correo ingresado
    - Almacena los dominios válidos en un conjunto para evitar duplicados
    - Imprime por pantalla la lista de dominios válidos ordenados alfabéticamente
    - Indica si no se ingresaron correos válidos
    - No devuelve ningún valor
    """

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

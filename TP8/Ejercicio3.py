"""Desarrollar un programa que utilice una función que reciba como parámetro una
cadena de caracteres conteniendo una dirección de correo electrónico y devuelva
una tupla con las distintas partes que componen dicha dirección. Ejemplo:
alguien@uade.edu.ar -> (alguien, uade, edu, ar). La función debe detectar
formatos de fecha inválidos y devolver una tupla vacía."""


def partes_correo(correo: str) -> tuple:
    """
    Analiza una dirección de correo electrónico y devuelve sus partes si es válida

    Pre:
    - Recibe una cadena con el formato de correo electrónico a evaluar.
    - El correo debe contener un único '@' y hasta dos puntos ('.') en el dominio

    Post:
    - Devuelve una tupla con las partes del correo: (usuario, dominio, extensión [, subextensión]) si es válido
    - Si el correo no cumple el formato esperado, devuelve una tupla vacía
    """

    if correo.count("@")!=1:
        return ()

    usuario,dominio=correo.split("@")
    if not usuario or not dominio:
        return ()

    if dominio.count(".")>2:
        return ()

    lista = []
    lista.append(usuario)

    dominios=dominio.split(".")
    for dom in dominios:
        if not dom:
            return ()
        else:
            lista.append(dom)

    return tuple(lista)


def main() -> None:
    """
    Función principal que solicita al usuario ingresar una dirección de correo electrónico
    y muestra sus partes si el formato es válido

    Pre:
    - No recibe parámetros.
    - El usuario debe ingresar una cadena con formato de correo electrónico

    Post:
    - Llama a la función partes_correo para analizar el correo ingresado
    - Imprime las partes del correo si es válido, o un mensaje de error si no lo es
    - No devuelve ningún valor
    """

    correo = input("Ingrese una dirección de correo electrónico: ")
    partes = partes_correo(correo)

    if partes:
        print(f"Partes del correo: {partes}")
    else:
        print("Correo inválido")


if __name__ == "__main__":
    main()

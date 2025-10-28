"""Desarrollar un programa que utilice una función que reciba como parámetro una
cadena de caracteres conteniendo una dirección de correo electrónico y devuelva
una tupla con las distintas partes que componen dicha dirección. Ejemplo:
alguien@uade.edu.ar -> (alguien, uade, edu, ar). La función debe detectar
formatos de fecha inválidos y devolver una tupla vacía."""


def partes_correo(correo: str) -> tuple:
    """
    """
    if correo.count("@")!=1:
        return ()

    usuario,dominio=correo.split("@")
    if not usuario or not usuario:
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


def main():
    correo = input("Ingrese una dirección de correo electrónico: ")
    partes = partes_correo(correo)

    if partes:
        print(f"Partes del correo: {partes}")
    else:
        print("Correo inválido")


if __name__ == "__main__":
    main()

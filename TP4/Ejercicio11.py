""" Escribir un programa que cuente cuántas veces se encuentra una subcadena dentro
de otra cadena, sin diferenciar mayúsculas y minúsculas. Tener en cuenta que los
caracteres de la subcadena no necesariamente deben estar en forma consecutiva
dentro de la cadena, pero sí respetando el orden de los mismos. Ejemplo:
Cadena:
Platero es pequeño, peludo, suave; tan blando por fuera, que se diría todo de algodón, que no lleva
huesos. Sólo los espejos de azabache de sus ojos son duros cual dos escarabajos de cristal negro.
Sub-cadena: UADE
Cantidad encontrada: 4 (Las coincidencias están resaltadas en la cadena siguiente)
Platero es pequeño, peludo, suave; tan blando por fuera, que se diría todo de algodón, que no lleva
huesos. Sólo los espejos de azabache de sus ojos son duros cual dos escarabajos de cristal negro.
"""

def contar_subcadenas(cadena: str, subcadena: str) -> None:
    """
    Cuenta cuántas veces aparece una subcadena dentro de una cadena ignorando mayúsculas y minúsculas

    Pre:
    - cadena es una cadena de caracteres
    - subcadena es la secuencia que se desea contar dentro de la cadena

    Post:
    - Imprime por pantalla la cantidad de veces que la subcadena aparece en la cadena
    - No devuelve ningún valor
    """

    cadena = cadena.lower()
    subcadena = subcadena.lower()

    veces = 0
    posicion = 0

    for i in range(len(cadena)):
        if cadena[i] == subcadena[posicion]:
            posicion += 1
            if posicion == len(subcadena):
                posicion = 0
                veces += 1

    print(f"La subcadena está {veces} veces en la cadena")


def main() -> None:
    """
    Llama a la función contar_subcadenas() con los variables de cadena y subcadena ya definidos

    Pre:
    - No recibe parámetros
    - La cadena y la subcadena están definidas dentro de la función

    Post:
    - Llama a la función contar_subcadenas para mostrar cuántas veces aparece la subcadena
    - Imprime el resultado por pantalla
    - No devuelve ningún valor
    """

    cadena = "Platero es pequeño, peludo, suave; tan blando por fuera, que se diría todo de algodón, que no lleva huesos. Sólo los espejos de azabache de sus ojos son duros cual dos escarabajos de cristal negro."
    subcadena = "UADE"
    contar_subcadenas(cadena,subcadena)

if __name__ == '__main__':
    main()

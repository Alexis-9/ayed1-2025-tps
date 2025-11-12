"""Todo programa Python es susceptible de ser interrumpido mediante la pulsación de
las teclas Ctrl-C, lo que genera una excepción del tipo KeyboardInterrupt. Realizar
un programa para imprimir los números enteros entre 1 y 100_000, y que solicite
confirmación al usuario antes de detenerse cuando se presione Ctrl-C.
"""

def main() -> None:
    """
    Imprime números consecutivos desde 1 hasta 1_000_000,
    permitiendo al usuario interrumpir la ejecución con Ctrl+C y decidir si detenerla o continuar

    Pre:
    - No recibe parámetros
    - El usuario puede presionar Ctrl+C para activar la interrupción

    Post:
    - Imprime por pantalla los números consecutivos
    - Si el usuario confirma detener el programa, finaliza la ejecución
    - Si el usuario decide continuar, el programa sigue imprimiendo números
    - No devuelve ningún valor
    """

    for i in range(1, 1_000_000):
        try:
            print(i)
        except KeyboardInterrupt:
            while True:
                respuesta = input("¿Desea detener el programa? Si: 1 | No: 2: ")
                if respuesta == "1":
                    return
                elif respuesta == "2":
                    break
                else:
                    print("Opción incorrecta")

if __name__ == "__main__":
    main()

#Lo hice hasta un millón asi llegaba a pararlo
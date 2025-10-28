"""Todo programa Python es susceptible de ser interrumpido mediante la pulsación de
las teclas Ctrl-C, lo que genera una excepción del tipo KeyboardInterrupt. Realizar
un programa para imprimir los números enteros entre 1 y 100000, y que solicite
confirmación al usuario antes de detenerse cuando se presione Ctrl-C.
"""

def main():
    for i in range(1, 1000000):
        try:
            print(i)
        except KeyboardInterrupt:
            while True:
                respuesta = input("¿Desea detener el programa? si/no: ")
                if respuesta == 'si':
                    print("Deteniendo programa...")
                    return
                elif respuesta == 'no':
                    print("Continuando la ejecución...")
                    break
                else:
                    print("Opción incorrecta")

if __name__ == "__main__":
    main()
"""Escribir una función que reciba como parámetro un número entero entre 0 y 3999 y
lo convierta en un número romano, devolviéndolo en una cadena de caracteres. ¿En
qué cambiaría la función si el rango de valores fuese diferente?"""

def romano(n: int) -> None:
    """
    Convierte un número entero positivo a su representación en números romanos y lo muestra por pantalla

    Pre: recibe un número entero positivo n
    Post: imprime la representación en números romanos correspondiente al número n
    """
    valores=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
    letras=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]

    texto=""
    for i in range(len(valores)):
        while n>=valores[i]:
            texto+=letras[i]
            n-=valores[i]
    print(texto)

def main() -> None:
    """
    Solicita al usuario un número entero y muestra su representación en números romanos

    Pre: no recibe parámetros, el usuario debe ingresar un número entero entre 1 y 3999
    Post: llama a la función romano para mostrar el número ingresado en notación romana
    """
    while True:
        try:
            n = int(input("Ingrese un número entre 1 y 3999: "))
            if n>0 and n<4000:
                break
            else:
                print("Debe estar entre 1 y 3999")
        except ValueError:
            print("Debe ingresar un entero")
    romano(n)

if __name__ == '__main__':
    main()
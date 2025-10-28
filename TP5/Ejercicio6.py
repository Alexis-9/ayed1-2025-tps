"""El método index permite buscar un elemento dentro de una lista, devolviendo la
posición que éste ocupa. Sin embargo, si el elemento no pertenece a la lista se
produce una excepción de tipo ValueError. Desarrollar un programa que cargue
una lista con números enteros ingresados a través del teclado (terminando con -1)
y permita que el usuario ingrese el valor de algunos elementos para visualizar la
posición que ocupan, utilizando el método index. Si el número no pertenece a la
lista se imprimirá un mensaje de error y se solicitará otro para buscar. Abortar el
proceso al tercer error detectado. No utilizar el operador in durante la búsqueda.
"""
lista=[]
while True:
    try:
        n = int(input("Número a agregar: "))
        if n==-1:
            break
        lista.append(n)
    except ValueError:
        print("Debe ingresar un número entero")

print(f"Lista cargada: {lista}")

errores=0
while errores<3:
    try:
        buscar=int(input("Número a buscar: "))
        posicion=lista.index(buscar)
        print(f"El número {buscar} está en la posición {posicion+1}")
    except ValueError:
        errores+=1
        print("No se encontró ese número")
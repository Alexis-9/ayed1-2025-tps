""" Escribir funciones lambda para:
a. Informar si un número es oblongo. Se dice que un número es oblongo cuando se puede obtener multiplicando dos números naturales consecutivos.
Por ejemplo 6 es oblongo porque resulta de multiplicar 2 * 3.

b. Informar si un número es triangular.
Un número se define como triangular si puede expresarse como la suma de un grupo de números naturales consecutivos comenzando desde 1.
Por ejemplo 10 es un número triangular porque se obtiene sumando 1+2+3+4.
Ambas funciones lambda reciben como único parámetro el número a evaluar y devuelven True o False. No se permite utilizar ayudas externas a las mismas."""

def es_oblongo(n):
    for a in range(n):
        if n == a * (a + 1):
            return True
    return False


def es_triangular(n):
    for i in range(n):
        suma = 0
        for j in range(i + 1):
            suma += j
        if n == suma:
            return True
    return False


n = int(input("Qué número desea comprobar si es oblongo y triangular: "))
print(f"Oblongo: {es_oblongo(n)}")
print(f"Triangular: {es_triangular(n)}")

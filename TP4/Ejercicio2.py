"""Leer una cadena de caracteres e imprimirla centrada en pantalla. Suponer que la
misma tiene 80 columnas."""

def centrar_texto() -> None:
    """
    Solicita un texto al usuario y lo muestra centrado en una pantalla de 80 caracteres

    Pre: no recibe parámetros, el usuario ingresa un texto por teclado
    Post: imprime el texto centrado con espacios a la izquierda según el largo del texto
    """
    texto=input("Texto: ")
    pantalla= 80 - len(texto)
    largo= pantalla//2
    print(" "*largo + texto)

centrar_texto()
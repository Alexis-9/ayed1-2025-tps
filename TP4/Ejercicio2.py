"""Leer una cadena de caracteres e imprimirla centrada en pantalla. Suponer que la
misma tiene 80 columnas."""

def centrar_texto():
    texto=input("Texto: ")
    pantalla= 80 - len(texto)
    largo= pantalla//2
    print(" "*largo + texto)

centrar_texto()
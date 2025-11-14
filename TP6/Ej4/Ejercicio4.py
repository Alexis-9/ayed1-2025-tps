"""Desarrollar un programa para eliminar todos los comentarios de un programa escrito en lenguaje Python. Tener en cuenta que los comentarios comienzan con el
signo # (siempre que éste no se encuentre encerrado entre comillas simples o dobles) y que también se considera comentario a las cadenas de documentación
(docstrings).
"""
def eliminar_comentarios():
    programa="prueba.txt"#input("Ingrese el nombre del programa de python: ")
    try:
        with open(programa, "r", encoding="utf-8") as archivo:
            lineas=archivo.readlines()
    except Exception:
        print("No se encontro el archivo o esta vacío")


    comentario=False
    entre_comillas=False

    nuevas_lineas=[]
    linea_nueva=""

    sucesion=0


    for linea in lineas:
        for caracter in linea:

            if caracter=='"' or caracter== "'":
                entre_comillas = True

            if caracter=="#" and not entre_comillas :
                comentario=True

            if caracter=='"':
                sucesion+=1
                if sucesion==3:
                    comentario=True
            else:
                sucesion=0

            if not comentario and not sucesion:
                linea_nueva+=caracter


        comentario=False
        entre_comillas=False
        sucesion=0
        if linea_nueva.strip():
            nuevas_lineas.append("".join(linea_nueva).strip())
        linea_nueva=""

    print("Comentarios eliminados")

    #Lo hice en otro archivo asi se ve la diferencía pero se podría hacer en el mismo archivo para que lo sobreescriba
    with open(f"{programa}_1", "w", encoding="utf-8") as archivo:
        for linea in nuevas_lineas:
            archivo.write(f"{linea}\n")

eliminar_comentarios()

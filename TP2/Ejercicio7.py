"""Intercalar los elementos de una lista entre los elementos de otra. La intercalación
deberá realizarse exclusivamente mediante la técnica de rebanadas y no se creará
una lista nueva sino que se modificará la primera. Por ejemplo, si lista1 = [8, 1, 3]
y lista2 = [5, 9, 7], lista1 deberá quedar como [8, 5, 1, 9, 3, 7]. Las listas pueden
tener distintas longitudes."""

def intercalar_listas(lista1: list[int], lista2: list[int]) -> list[int]:
    """
    Intercala los elementos de lista2 dentro de lista1 uno por uno

    Pre: Dos listas de números enteros

    Post: Devuelve una nueva lista donde los elementos de lista2 se intercalan en lista1 manteniendo el orden de ambas listas
    """
    contador=1
    for i,x in enumerate(lista2):
        lista1[i+contador:i+contador] = [x]
        contador+=1
    return lista1

def main() -> None:
    """
    Intercala dos listas de ejemplo

    Pre: No recibe nada

    Post: Imprime lista1, lista2 y el resultado de intercalarlas usando intercalar_listas
    """
    lista1 = [8, 1, 3]
    lista2 = [5, 9, 7, "a", "b"]
    print(f"La lista 1 es {lista1}")
    print(f"La lista 2 es {lista2}")
    print(f"Las listas intercaladas quedan: {intercalar_listas(lista1,lista2)}")

main()

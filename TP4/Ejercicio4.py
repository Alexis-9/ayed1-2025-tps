"""Escribir una función que reciba como parámetro un número entero entre 0 y 3999 y
lo convierta en un número romano, devolviéndolo en una cadena de caracteres. ¿En
qué cambiaría la función si el rango de valores fuese diferente?"""


n=int(input("N: "))

valores=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
letras=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]

texto=""
for i in range(len(valores)):
    while n>=valores[i]:
        texto+=letras[i]
        n-=valores[i]
print(texto)
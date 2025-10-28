import random as rn

n=3

matriz=[]
dias=["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]
for i in range(n):
    fila=[]
    for j in range(7):
        fila.append(rn.randint(0,150))
    matriz.append(fila)


for i,fila in enumerate(matriz):
    print(f"Fabrica {i+1} {fila}")


fabricas=[]
total=0
for i in range(len(matriz)):
    for j in range(7):
       total+=matriz[i][j]
    fabricas.append(total)
    total=0

print()
for i,x in enumerate(fabricas):
    print(f"La fábrica {i+1} produjo {x} bicicletas")

mayor=0
fabrica=0
dia=0
for i in range(len(matriz)):
    for j in range(7):
        if matriz[i][j]>mayor:
            mayor=matriz[i][j]
            fabrica=i
            dia=j

print()
print(f"La fabrica {fabrica+1} fue la que más produjo en el día {dias[dia]}")

mayor=0
total=0
dia=0
for i in range(7):
    for j in range(len(matriz)):
        total+=matriz[j][i]
    if total>mayor:
        mayor=total
        dia=i
    total=0


print()
print(f"El dìa más productivo fue el {dias[dia]} con {mayor} bicicletas")

print()
menor=[min(fabrica) for fabrica in matriz]
print(menor)

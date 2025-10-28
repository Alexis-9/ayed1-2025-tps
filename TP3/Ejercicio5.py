import random as rn



n=3
m=5
matriz=[]
for i in range(n):
    fila=[]
    for j in range(m):
        fila.append(0)
    matriz.append(fila)

for fila in matriz:
    print(fila)

asd=3-1
nfila=0
if asd>len(matriz):
    asd-=len(matriz)
    nfila+=1

if not matriz[nfila][asd]:
    print("Butaca reservada")
    matriz[nfila][asd]=1
    for fila in matriz:
        print(fila)

else:
    print("No")

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz[i][j]=rn.randint(0,1)

print()
for fila in matriz:
    print(fila)

print()
desocupadas=0
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if not matriz[i][j]:
            desocupadas+=1
print(f"Hay {desocupadas} butacas desocupadas")

mayor=0
secuencia=0
fila=0
posicion=0
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
       if not matriz[i][j]:
           secuencia+=1
           if secuencia>mayor:
               mayor=secuencia
               fila=i
               posicion=j-secuencia
       else:
           secuencia=0

print(f"La secuencia más larga de butacas libres es de {mayor}, esta en la fila {fila+1} y empieza en la butaca {posicion+2}")
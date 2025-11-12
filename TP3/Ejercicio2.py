n=4

#Punto a
def punto_a():
    matriz=[]
    num=1
    for i in range(n):
        fila=[]
        for j in range(n):
            if i==j:
                fila.append(num)
                num+=2
            else:
                fila.append(0)
        matriz.append(fila)

    for fila in matriz:
        print(fila)

#Punto b
def punto_b():
    matriz=[]
    num=3**(n-1)
    for i in range(n):
        fila=[]
        for j in range(n):
            if j==n-1-i:
                fila.append(num)
                num//=3
            else:
                fila.append(0)
        matriz.append(fila)

    for fila in matriz:
        print(fila)

#Punto c
def punto_c():
    matriz = []
    num=n
    for i in range(n):
        fila = []
        for j in range(n):
            if i >= j:
                fila.append(num)
            else:
                fila.append(0)
        num -= 1
        matriz.append(fila)

    for fila in matriz:
        print(fila)

#Punto d
def punto_d():
    matriz = []
    num = 2**(n-1)
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(num)
        matriz.append(fila)
        num //= 2

    for fila in matriz:
        print(fila)

#Punto e
def punto_e():
    matriz = []
    num = 1
    for i in range(n):
        fila = []
        for j in range(n):
            if (i+j) % 2 != 0:
                fila.append(num)
                num += 1
            else:
                fila.append(0)
        matriz.append(fila)

    for fila in matriz:
        print(fila)



#Punto f
def punto_f():
    matriz = []
    num = 1

    for i in range(n):
        fila = []
        for j in range(n):
            if j<=i:
                fila.append(num)
                num += 1
            else:
                fila.append(0)
        fila.reverse()
        matriz.append(fila)

    for fila in matriz:
        print(fila)

#Punto g
def punto_g():
    matriz=[]
    for i in range(n):
        fila=[]
        for j in range(n):
            fila.append(0)
        matriz.append(fila)

    num=1
    inicio=0
    fin=n-1

    while inicio<=fin:
        for arriba in range(inicio,n-inicio):
            matriz[inicio][arriba]=num
            num+=1

        for derecha in range(inicio+1, fin+1):
            matriz[derecha][fin]=num
            num+=1

        for abajo in range(inicio+1, fin):
            fin2=n-1-abajo
            matriz[fin][fin2]=num
            num+=1

        for izquierda in range(inicio+1, fin+1):
            fin2=n-izquierda
            matriz[fin2][inicio]=num
            num+=1

        inicio+=1
        fin-=1

    for fila in matriz:
        print(fila)

#Punto h
def punto_h():
    pass


    for fila in matriz:
        print(fila)

#Punto i
def punto_i():
    pass

punto_h()
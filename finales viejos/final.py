stock = [[],[],[],[]]

def cargar_producto():
    print(f"Los productos ahora son: {stock[0]}")
    cargar_nombre=input("Ingrese el nombre del nuevo producto: ")
    verificar=False
    while verificar==False:
        for i in range(len(stock[0])):
            if cargar_nombre==stock[0][i]:
                print("Ese producto ya esta ingresado, intelo de nuevo")
                cargar_nombre = input("Ingrese el nombre del producto: ")
            else:
                verificar=True
    stock[0].append(cargar_nombre)

    cargar_categoria=int(input("Ingrese el número de la categoria de ese producto (1:Limpieza 2:Alimentos 3:Bazar): "))
    while cargar_categoria>3 or cargar_categoria<1:
        print("Error, intentelo de nuevo")
        cargar_categoria = int(input("Ingrese el número de la categoria de ese producto (1:Limpieza 2:Alimentos 3:Bazar): "))
    stock[1].append(cargar_categoria)

    cargar_precio=int(input("Ingrese el precio de ese producto: $"))
    stock[2].append(cargar_precio)
    while cargar_precio<=0:
        print("Error, ingrese un valor válido")
        cargar_precio = int(input("Ingrese el precio de ese producto: $"))

    cargar_cantidad=int(input("Ingrese la cantidad de stock de ese producto: "))
    while cargar_cantidad<=0:
        print("Error, ingrese un valor válido")
        cargar_cantidad = int(input("Ingrese la cantidad de stock de ese producto: $"))
    stock[3].append(cargar_cantidad)

def mostrar_bazar():
    contador=0
    for i in range(len(stock[1])):
        if stock[1][i]==3:
            contador+=1
    return f"Hay {contador} productos en la categoría bazar"

def cambiar_precio():
    if len(stock[0])>0:
        print(f"Los productos son: {stock[0]}")
        print(f"Sus precios son: {stock[2]}")
        nombre = input("Ingrese el nombre del producto a cambiar: ")
        encontrado=False
        for i in range(len(stock[0])):
            if nombre == stock[0][i]:
                encontrado=True
                indice=i
        if encontrado==True:
            precio = int(input("Ingrese el nuevo precio: $"))
            while precio <= 0:
                print("Error, ingrese un valor válido")
                precio = int(input("Ingrese el nuevo precio: $"))
            stock[2][indice] = precio
            return f"Precio actualizado: {stock[2]}"
        else:
            return f"No se encontro el producto"
    else:
        return f"No hay productos todavía"

def promedio_categoria():
    print("Categorías: 1-Limpieza 2-Alimentos 3-Bazar")
    categoria=int(input("Ingrese un número de una categoría: "))
    total=0
    contador=0
    if (categoria==1 or categoria==2 or categoria==3) and len(stock[1])>0:
        for i in range(len(stock[1])):
            if stock[1][i]==categoria:
                total+=stock[2][i]
                contador+=1
        promedio=total/contador
        return f"El promedio de precio de los productos de la categoría {categoria} es ${promedio}"
    else:
        return f"No hay productos de esa categoría"

def menor_stock():
    menor=0
    nombre=0
    for i in range(len(stock[1])):
        if stock[1][i]==2:
            if menor==0 or menor>stock[3][i]:
                menor=stock[3][i]
                nombre = stock[0][i]
    if nombre!=0:
        return f"El producto con menor stock en alimentos es ({nombre}) y tiene ({menor}) de stock"
    else:
        return f"No hay productos en alimentos"

def mas_caro():
    mayor = 0
    mayor1 = 0
    mayor2 = 0
    limpieza=0
    alimentos=0
    bazar=0
    for i in range(len(stock[1])):
        if stock[1][i] == 1:
            if mayor == 0 or mayor < stock[2][i]:
                mayor = stock[2][i]
                limpieza = stock[0][i]
        if stock[1][i] == 2:
            if mayor1 == 0 or mayor1 < stock[2][i]:
                mayor1 = stock[2][i]
                alimentos = stock[0][i]
        if stock[1][i] == 3:
            if mayor2 == 0 or mayor2 < stock[2][i]:
                mayor2 = stock[2][i]
                bazar = stock[0][i]
    if bazar!=0:
        print(f"El producto más caro en la categoría de Bazar es ({bazar}) y tiene un valor de ${mayor2}")
    else:
        print(f"No hay productos en bazar")
    if limpieza!=0:
        print (f"El producto más caro en la categoría de Limpieza es ({limpieza}) y tiene un valor de ${mayor}")
    else:
        print(f"No hay productos en limpieza")
    if alimentos!=0:
        print(f"El producto más caro en la categoría de Alimentos es ({alimentos}) y tiene un valor de ${mayor1}")
    else:
        print(f"No hay productos en alimentos")





def opciones():
    print("1: Cargar productos al inventario")
    print("2: Mostrar la cantidad de productos de bazar")
    print("3: Cambiar precio de producto")
    print("4: Promedio de precio de una categoría")
    print("5: Producto con menor stock en alimentos")
    print("6: Producto más caro por categoría")
    print("7: Salir")

def menu():
    opciones()
    print()
    op = input("Ingrese su opción (0: Para mostrar las opciones): ")
    print()
    while op!="7":
        if op=="0":
            opciones()
        elif op=="1":
            cargar_producto()
        elif op=="2":
            print(mostrar_bazar())
        elif op=="3":
            print(cambiar_precio())
        elif op=="4":
            print(promedio_categoria())
        elif op=="5":
            print(menor_stock())
        elif op=="6":
            mas_caro()
        else:
            print("Opción incorrecta")
        print()
        op=input("Ingrese su opción (0: Para mostrar las opciones): ")
        print()
    print("Adiós")

menu()

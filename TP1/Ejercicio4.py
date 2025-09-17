"""Un comercio de electrodomésticos necesita para su línea de cajas un programa que le indique al cajero el cambio que debe entregarle al cliente.
Para eso se ingresan dos números enteros, correspondientes al total de la compra y al dinero recibido.
Informar cuántos billetes de cada denominación deben ser entregados como vuelto, de tal forma que se minimice la cantidad de billetes.
Considerar que existen billetes de $5000, $1000, $500, $200, $100, $50 y $10.
Emitir un mensaje de error si el dinero recibido fuera insuficiente o si el cambio no pudiera entregarse debido a falta
de billetes con denominaciones adecuadas.
Ejemplo: Si la compra es de $3170 y se abona con $5000, el vuelto debe contener 1 billete de $1000, 1 billete de $500,
1 billete de $200, 1 billete de $100 y 3 billetes de $10.
"""

def dar_vuelto(total:int, recibido:int)->None:
    """
    Calcula y muestra el vuelto a dar en cada billete
    pre: total de la compra como número entero
         dinero recibido del cliente como número entero
    post:
    -Si recibido < total  imprime un mensaje de "dinero insuficiente"
    - Si recibido == total  imprime un mensaje de "No hay vuelto".
    - Si recibido > total  imprime cuanto cambio debe devolver usando los billetes de la lista
    - Si queda un resto menor a 10 imprime "Y te debo $(resto)"
    """
    cambio = recibido - total
    if cambio < 0:
        print("Error: dinero insuficiente.")
    elif cambio == 0:
        print("No hay vuelto.")
    else:
        billetes = [5000, 1000, 500, 200, 100, 50, 10]
        for i in billetes:
            cantidad=cambio//i
            if cantidad>0:
                print(f"{cantidad} billetes de ${i}")
            cambio=cambio%i
        if cambio>0:
            print(f"Y te debo ${cambio}")

def ingresar_valores()->None:
    """
    Solicita al usuario el total de la compra y el dinero recibido
    Calcula el vuelto a devolver con la función dar_vuelto

    pre: El usuario ingresa total_compra y dinero_recibido como dos números enteros positivos

    post:
    - Si alguno de los valores es menor o igual a 0 imprime un mensaje de error
    - En caso contrario llama a la función dar_vuelto(total_compra, dinero_recibido)

    """
    total_compra = int(input("Ingrese el total de la compra: "))
    dinero_recibido = int(input("Ingrese el dinero recibido: "))
    if total_compra<=0 or dinero_recibido<=0:
        print("Debe ingresar valores positivos")
    else:
        dar_vuelto(total_compra, dinero_recibido)

ingresar_valores()
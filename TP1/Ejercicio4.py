"""Un comercio de electrodomésticos necesita para su línea de cajas un programa que le indique al cajero el cambio que debe entregarle al cliente.
Para eso se ingresan dos números enteros, correspondientes al total de la compra y al dinero recibido.
Informar cuántos billetes de cada denominación deben ser entregados como vuelto, de tal forma que se minimice la cantidad de billetes.
Considerar que existen billetes de $5000, $1000, $500, $200, $100, $50 y $10.
Emitir un mensaje de error si el dinero recibido fuera insuficiente o si el cambio no pudiera entregarse debido a falta
de billetes con denominaciones adecuadas.
Ejemplo: Si la compra es de $3170 y se abona con $5000, el vuelto debe contener 1 billete de $1000, 1 billete de $500,
1 billete de $200, 1 billete de $100 y 3 billetes de $10.
"""

def dar_vuelto(total, recibido):
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

def ingresar_valores():
    total_compra = int(input("Ingrese el total de la compra: "))
    dinero_recibido = int(input("Ingrese el dinero recibido: "))
    if total_compra<=0 or dinero_recibido<=0:
        print("Debe ingresar valores positivos")
    else:
        dar_vuelto(total_compra, dinero_recibido)

ingresar_valores()
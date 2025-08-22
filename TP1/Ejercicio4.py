"""Un comercio de electrodomésticos necesita para su línea de cajas un programa que le indique al cajero el cambio que debe entregarle al cliente.
Para eso se ingresan dos números enteros, correspondientes al total de la compra y al dinero recibido.
Informar cuántos billetes de cada denominación deben ser entregados como vuelto, de tal forma que se minimice la cantidad de billetes.
Considerar que existen billetes de $5000, $1000, $500, $200, $100, $50 y $10.
Emitir un mensaje de error si el dinero recibido fuera insuficiente o si el cambio no pudiera entregarse debido a falta
de billetes con denominaciones adecuadas.
Ejemplo: Si la compra es de $3170 y se abona con $5000, el vuelto debe contener 1 billete de $1000, 1 billete de $500,
1 billete de $200, 1 billete de $100 y 3 billetes de $10.
"""
def dar_vuelto():
    total_compra = int(input("Ingrese el total de la compra: "))
    dinero_recibido = int(input("Ingrese el dinero recibido: "))

    cambio = dinero_recibido - total_compra
    billetes=[]

    if cambio < 0:
        print("Error: dinero insuficiente.")
    elif cambio == 0:
        print("No hay vuelto.")
    else:
        print(f"El vuelto es de ${cambio}")

        billetes5000 = cambio // 5000
        cambio = cambio % 5000

        billetes1000 = cambio // 1000
        cambio = cambio % 1000

        billetes500 = cambio // 500
        cambio = cambio % 500

        billetes200 = cambio // 200
        cambio = cambio % 200

        billetes100 = cambio // 100
        cambio = cambio % 100

        billetes50 = cambio // 50
        cambio = cambio % 50

        billetes10 = cambio // 10
        cambio = cambio % 10

        if cambio != 0:
            print("Error: no se puede entregar vuelto exacto.")
        else:
            if billetes5000 > 0:
                print(billetes5000, "billete(s) de $5000")
            if billetes1000 > 0:
                print(billetes1000, "billete(s) de $1000")
            if billetes500 > 0:
                print(billetes500, "billete(s) de $500")
            if billetes200 > 0:
                print(billetes200, "billete(s) de $200")
            if billetes100 > 0:
                print(billetes100, "billete(s) de $100")
            if billetes50 > 0:
                print(billetes50, "billete(s) de $50")
            if billetes10 > 0:
                print(billetes10, "billete(s) de $10")
dar_vuelto()
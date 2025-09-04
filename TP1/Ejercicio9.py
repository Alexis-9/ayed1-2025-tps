"""Resolver el siguiente problema utilizando funciones:
Un productor frutihortícola desea contabilizar sus cajones de naranjas según el peso
para poder cargar los camiones de reparto. La empresa cuenta con N camiones, y
cada uno puede transportar hasta media tonelada (500 kilogramos). En un cajón
caben 100 naranjas con un peso de entre 200 y 300 gramos cada una. Si el peso
de alguna naranja se encuentra fuera del rango indicado se la clasifica para
procesar como jugo.
Desarrollar un programa para ingresar la cantidad de naranjas
cosechadas e informar cuántos cajones se pueden llenar, cuántas naranjas son para
jugo y si hay algún sobrante de naranjas que deba considerarse para el siguiente
reparto.
Simular el peso de cada unidad generando un número entero al azar entre 150 y 350.
Además, se desea saber cuántos camiones se necesitan para transportar la cosecha, considerando que la ocupación del camión no debe ser inferior al 80%; en
caso contrario el camión no serán despachado por su alto costo."""

import random as rn

def separar_naranjas(naranjas):
    cantidad_jugo = 0
    cantidad_naranjas = 0
    for i in range(naranjas):
        peso=rn.randint(150,350)
        if peso<200 or peso>300:
            cantidad_jugo+=1
        else:
            cantidad_naranjas+=1
    return cantidad_naranjas,cantidad_jugo

def llenar_cajones(cantidad_naranjas):
    cajones=0
    while cantidad_naranjas>=100:
        cajones+=1
        cantidad_naranjas-=100
    return cajones,cantidad_naranjas

def llenar_camiones(cajones):
    camiones=0
    peso_maximo_camion=500
    peso_cajon=25
    cajones_por_camion=peso_maximo_camion//peso_cajon
    ocupacion=int(cajones_por_camion*0.8)

    while cajones>=ocupacion:
        camiones+=1
        cajones-=ocupacion

    return cajones,camiones

def verificar(naranjas):
    return naranjas>0

def ingresar_valores():
    naranjas = int(input("Ingrese la cantidad de naranjas cosechadas: "))
    if verificar(naranjas):
        cantidad_naranjas, cantidad_jugo = separar_naranjas(naranjas)
        cajones, sobrante = llenar_cajones(cantidad_naranjas)
        cajones_sobrantes,camiones = llenar_camiones(cajones)

        print(f"Hay {cantidad_naranjas} naranjas válidas para cajones ")
        print(f"{cantidad_jugo} naranjas son para jugo ")
        print(f"Se llenaron {cajones} cajones")
        print(f"Y sobraron {sobrante} naranjas")
        if camiones>1:
            print(f"Para transportar los cajones se necesitan {camiones} camiones con un 80% de ocupación mínima: ")
            if cajones_sobrantes > 0:
                print(f"Y sobraron {cajones_sobrantes} cajones")
        elif camiones==1:
            print(f"Para transportar los cajones se necesita un camión")
            if cajones_sobrantes>0:
                print(f"Y sobraron {cajones_sobrantes} cajones")
        else:
            print(f"Hay {cajones_sobrantes} cajones, por lo tanto no son suficientes para llenar un camión")
    else:
        print("Error, ingrese una cantidad válida de naranjas")

ingresar_valores()
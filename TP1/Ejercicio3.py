"""Una persona desea llevar el control de los gastos realizados al viajar en el subterráneo dentro de un mes.
Sabiendo que dicho medio de transporte utiliza un esquema de tarifas decrecientes (detalladas en la tabla de abajo) se solicita desarrollar una función
que reciba como parámetro la cantidad de viajes realizados en un determinado mes y devuelva el total gastado en viajes.
Realizar también un programa para verificar el comportamiento de la función.
"""

def gasto_subte(viajes:int, tarifa_max:int)->float:
    """
    Calcula el gasto total en pasajes según la cantidad de viajes y sus descuentos
    pre: viajes como número entero
         tarifa_max como número entero

    post: Devuelve el total como float
    """
    if viajes <= 0:
        total=0
    elif viajes <= 20:
        total = viajes * tarifa_max
    elif viajes <= 30:
        total = 20 * tarifa_max + (viajes - 20) * tarifa_max * 0.8
    elif viajes <= 40:
        total = 20 * tarifa_max + 10 * tarifa_max * 0.8 + (viajes - 30) * tarifa_max * 0.7
    else:
        total = 20 * tarifa_max + 10 * tarifa_max * 0.8 + 10 * tarifa_max * 0.7 + (viajes - 40) * tarifa_max * 0.6
    return total

tarifa = 1031
cantidad_viajes = int(input("Ingrese la cantidad de viajes del mes: "))

total = gasto_subte(cantidad_viajes, tarifa)

print(f"El total gastado en el mes es: ${total}")

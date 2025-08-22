"""Una persona desea llevar el control de los gastos realizados al viajar en el subterráneo dentro de un mes.
Sabiendo que dicho medio de transporte utiliza un esquema de tarifas decrecientes (detalladas en la tabla de abajo) se solicita desarrollar una función
que reciba como parámetro la cantidad de viajes realizados en un determinado mes y devuelva el total gastado en viajes.
Realizar también un programa para verificar el comportamiento de la función.
"""

def gasto_subte(viajes, tarifa_max):
    if viajes <= 0:
        return 0
    if viajes <= 20:
        costo_viaje = tarifa_max
    elif viajes <= 30:
        costo_viaje = tarifa_max * 0.8
    elif viajes <= 40:
        costo_viaje = tarifa_max * 0.7
    else:
        costo_viaje = tarifa_max * 0.6
    total_gasto= viajes*costo_viaje
    return total_gasto

tarifa = 963
cantidad_viajes = int(input("Ingrese la cantidad de viajes del mes: "))

total = gasto_subte(cantidad_viajes, tarifa)

print(f"El total gastado en el mes es: ${total}")

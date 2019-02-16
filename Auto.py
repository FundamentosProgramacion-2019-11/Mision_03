# Autor: Alan Giovanni Rodriguez Camacho A01748185
# Descripcion: Calcula el redimiento de un automovil de km/l y en millas/galone imprime los litros necesario de gasolina para hacer un viaje.


def CalcularKmLitros(km,lt):#Calcula los km/litro de cirto numero de kilometros y litros
    kmLt=km/lt

    return kmLt
def CalcularMiGalon(km,lt):#Calcula las mi/gal de cirto numero de kilometros y litros
    mi=km/1.6093
    ga=lt*0.264
    miGa=mi/ga

    return miGa

def CalcularLitrosGasolina(km,lt,kmPorRecorrer):#Calcula los litros de gasolina necesarios para recorrer x numero de kilometros.
    ltGas=(kmPorRecorrer*lt)/km

    return ltGas

def main():
    km=int(input("Teclea el numero de km recorridos: "))
    lt=int(input("Teclea el numero de litros de gasolina usados: "))
    kmlt=CalcularKmLitros(km,lt)
    miga=CalcularMiGalon(km,lt)

    print("Si recorres {0}km con {1} litros de gasolina, el rendimiento es: ".format(km,lt))
    print("%.2f km/l"% kmlt)
    print("%.2f mi/gal"% miga)

    kmPorRecorrer=int(input("¿Cuantos km vas a recorrer? "))
    total=CalcularLitrosGasolina(km,lt,kmPorRecorrer)

    print("Para recorrer %.0f km necesitas %.02f litros de gasolina"% (kmPorRecorrer,total))

main()
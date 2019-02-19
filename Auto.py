# Autor: Itzel Yanabany Castro Becerril
# Calcular km/l, mi/gal y lo litros necesarios de gasolina que necesitara un coche


def calcularKml(km, litros, recorrer):
    kml = km / litros
    return kml


def calcularMilgalimprimirKml(km, litros, recorrer):
    milGal = (calcularKml(km, litros, recorrer) / 1.6093) / 0.264
    return milGal


def imprimirKml(km, litros, recorrer):
    kml = calcularKml(km, litros, recorrer)
    milGal = calcularMilgalimprimirKml(km, litros, recorrer)
    print("Si recorrer """, km, "kms con", litros, " litros de gasolina, el rendimiento es:")
    print("Km/l= %.2f" % (kml))
    print("Mil/gal= %.2f" % (milGal))


def calcularRecorrido(km, litros, recorrer):
    recorrido = (recorrer * litros) / km
    return recorrido


def imprimirRecorrido(km, litros, recorrer):
    recorrido = calcularRecorrido(km, litros, recorrer)
    print("Para recorrer", recorrer, "Km necesitas %.2f" % (recorrido), "litros de gasolina.")


def main():
    km = int(input("Teclea el numero de km recorridos: "))
    litros = int(input("Teclea el numero de litros de gasolina usados: "))
    recorrer = int(input("¿Cuantos kilometros vas a recorrer?: "))
    imprimirKml(km, litros, recorrer)
    imprimirRecorrido(km, litros, recorrer)


main()



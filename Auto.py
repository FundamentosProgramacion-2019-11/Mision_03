#Autor: Yasmín Landaverde Nava
#Descripción: este programa calcula el rendimiento de un auto

MILLAS = 1.6093
GALONES = 0.264

def calcularKilometrosLitros(kilometros, litros):
    totalkml = kilometros / litros
    return totalkml

def imprimirKilometrosLitros(kilometros, litros):
    totalkml = calcularKilometrosLitros(kilometros, litros)
    print("Si recorres", kilometros, "kms con", litros, "litros de gasolina, el rendimiento es:")
    print("%.2f" % totalkml, "km/l")

def calcularMillasGalones(kilometros, litros):
    millas = kilometros / MILLAS
    galones = litros * GALONES
    totalmig = millas / galones
    return totalmig

def imprimirMillasGalones(kilometros, litros):
    totalmig = calcularMillasGalones(kilometros, litros)
    print ("%.2f" % totalmig, "mi/gal")

def calcularLitros(kilometros, litros, futuro):
    totalLitros = futuro / calcularKilometrosLitros(kilometros, litros)
    return totalLitros

def imprimirLitros(kilometros, litros, futuro):
    totalLitros = calcularLitros(kilometros, litros,futuro)
    print("Para recorrer", futuro, "necesitas "  "%.2f" % totalLitros, "de gasolina")


def main():
    kilometros = int(input("Teclea el número de kms recorridos: "))
    litros = int(input("Teclea el número de litros de gasolina usados:  "))
    calcularKilometrosLitros(kilometros, litros)
    imprimirKilometrosLitros(kilometros, litros)
    calcularMillasGalones(kilometros, litros)
    imprimirMillasGalones(kilometros, litros)
    futuro = int(input("¿Cuántos kilómetros vas a recorrer?: "))
    calcularLitros(kilometros, litros,futuro)
    imprimirLitros(kilometros, litros,futuro)

main()
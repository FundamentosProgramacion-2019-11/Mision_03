#Maria Angelica Hernandez Parada
#Rendimiento de un automovil

def calcularRendimiento(kilometrosRecorridos, litrosUsados):
    rendimiento=kilometrosRecorridos/litrosUsados
    return rendimiento

def imprimirRendimiento(kilometrosRecorridos, litrosUsados):
    imprendimiento = calcularRendimiento(kilometrosRecorridos, litrosUsados)
    print("Si recorres", kilometrosRecorridos, "km con", litrosUsados, "litros de gasolina, el rendimiento es:  ")
    print("%.2f" % (imprendimiento), "km/l")

def calcularMillas(kilometrosRecorridos):
    millas= kilometrosRecorridos/1.6093
    return millas

def calcularGalones(litrosUsados):
    galones= litrosUsados * 0.264
    return galones

def calcularRendimientoEnMillasGalones(kilometrosRecorridos,litrosUsados):
    millas1=calcularMillas(kilometrosRecorridos)
    galones1=calcularGalones(litrosUsados)
    rendimiento= millas1/galones1
    return rendimiento

def imprimirRendimientoEnMillasGalones(kilometrosRecorridos,litrosUsados):
    rendimientoGalonesMillas= calcularRendimientoEnMillasGalones(kilometrosRecorridos,litrosUsados)
    print("%.2f" % (rendimientoGalonesMillas), "mi/gal")

def calcularLitros(kilometrosPorRecorrer):
    litros= kilometrosPorRecorrer/27.93
    return litros

def imprimirLitros(kilometrosPorRecorrer):
    implitros=calcularLitros(kilometrosPorRecorrer)
    print("Para recorrer",kilometrosPorRecorrer, "km. necesitas", "%.2f" %(implitros),"litros de gasolina")

def main():
    kilometrosRecorridos = int(input("Teclea el número de km recorridos: "))
    litrosUsados = int(input("Teclea el número de litros de gasolina usados: "))
    calcularRendimiento(kilometrosRecorridos, litrosUsados)
    imprimirRendimiento(kilometrosRecorridos, litrosUsados)
    calcularMillas(kilometrosRecorridos)
    #1milla=1.6093
    calcularGalones(litrosUsados)
    calcularRendimientoEnMillasGalones(kilometrosRecorridos,litrosUsados)
    imprimirRendimientoEnMillasGalones(kilometrosRecorridos,litrosUsados)
    kilometrosPorRecorrer = int(input("¿Cuántos Kilómetros vas a recorrer? "))
    calcularLitros(kilometrosPorRecorrer)
    #1lt= 27.93
    imprimirLitros(kilometrosPorRecorrer)

main()

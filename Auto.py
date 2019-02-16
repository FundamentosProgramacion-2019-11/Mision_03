#Autor: María Fernanda García Gastélum A01376181
#Calcular rendimiento de gasolina en km/l y mi/gal

def calcularRendimientoKilometros(kilometrosRecorridos,gasolinaUtilizadaLitros):
    rendimientoKilometros= kilometrosRecorridos/gasolinaUtilizadaLitros
    return rendimientoKilometros

def calcularRendimientoMillas(kilometrosRecorridos,gasolinaUtilizadaLitros):
    rendimientoMillas= (kilometrosRecorridos/ 1.6093 )/(gasolinaUtilizadaLitros / 0.264)
    return rendimientoMillas

def calcularGasolinaPorKm(kilometrosPorRecorrer,kilometrosRecorridos,gasolinaUtilizadaLitros):
    gasolinaPorKm= kilometrosPorRecorrer/calcularRendimientoKilometros(kilometrosRecorridos,gasolinaUtilizadaLitros)
    return gasolinaPorKm

def main():
    kilometrosRecorridos= int(input("Teclea el número de km recorridos:"))
    gasolinaUtilizadaLitros= int(input("Teclea el número de litros de gasolina usados: "))
    calcularRendimientoKilometros(kilometrosRecorridos,gasolinaUtilizadaLitros)
    calcularRendimientoMillas(kilometrosRecorridos,gasolinaUtilizadaLitros)
    print("\n")
    print("Si recorres", kilometrosRecorridos, "kms con", gasolinaUtilizadaLitros, "litros de gasolina, el rendimiento es: ")
    print("%.2f" % calcularRendimientoKilometros(kilometrosRecorridos,gasolinaUtilizadaLitros), "km/l")
    print("%.2f" % calcularRendimientoMillas(kilometrosRecorridos,gasolinaUtilizadaLitros), "mi/gal")
    print("\n")
    kilometrosPorRecorrer= int(input("¿Cuántos kilómetros vas a recorrer? "))
    calcularGasolinaPorKm(kilometrosPorRecorrer,kilometrosRecorridos,gasolinaUtilizadaLitros)
    print("\n")
    print("Para recorrer", kilometrosPorRecorrer, "km. necesitas %.2f"% calcularGasolinaPorKm(kilometrosPorRecorrer,kilometrosRecorridos,gasolinaUtilizadaLitros), "litros de gasolina")

main()
#Autor: Diego Raul Elizalde Uriarte
#





def calcularRendimientoMi(kilometrosRecorridos,litrosGasolina):
    millaPorgalon = (kilometrosRecorridos/1.6093) / (litrosGasolina*0.264)
    return millaPorgalon



def calcularRendimientoKm(kilometrosRecorridos,litrosGasolina):
    kmPorLitro = kilometrosRecorridos/litrosGasolina
    return kmPorLitro

def calcularKmQueRecorrera(kilometrosRecorridos,litrosGasolina,kmQueRecorrera):
    kmQueRecorrera = (litrosGasolina/kilometrosRecorridos)* kmQueRecorrera
    return kmQueRecorrera



def main():
    kilometrosRecorridos = int(input("Teclea el número de km recorridos: "))
    litrosGasolina = int(input("Teclea el número de litros de gasolina usados: "))
    calcularRendimientoKm(kilometrosRecorridos,litrosGasolina)
    calcularRendimientoMi(kilometrosRecorridos,litrosGasolina)
    print("Si recorres", kilometrosRecorridos, "kms con 17 litros de gasolina, el rendimiento es: ")
    print(" %.2f" % (calcularRendimientoKm(kilometrosRecorridos,litrosGasolina)), "km/l")
    print(" %.2f" % (calcularRendimientoMi(kilometrosRecorridos,litrosGasolina)), "mi/gal")
    kmQueRecorrera = int(input("¿Cuántos kilómetros vas a recorrer? "))
    print("Para recorrer", kmQueRecorrera, "km. necesitas %.2f" % (calcularKmQueRecorrera(kilometrosRecorridos,litrosGasolina,kmQueRecorrera)), "litros de gasolina")






main()
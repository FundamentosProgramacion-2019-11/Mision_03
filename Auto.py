#Autor: Michel Antoine Dionne Gutierrez A0174863, Grupo: 03
#Este programa calculara el rendimiento de un coche y cuantos litros de gasolina necesitara para viajar una cierta cantidad


#Esta funcion calcula el rendimiento en km/litros
def calcularRendimientoKm(kmRecoridos,litrosGasolina):
    rendimientoEnKm = kmRecoridos/litrosGasolina
    return rendimientoEnKm

#Esta funcion calcula el rendimiento en millas/galones
def calcularRendimientoMillas(kmRecoridos,litrosGasolina):
    rendimientoEnMillas = ((kmRecoridos / 1.609) / (litrosGasolina * .264))
    return rendimientoEnMillas

#Esta funcion calcula cunatos litros necesita para viajar una cierta distancia dependiendo del rendimiento
def calcularLitrosGasolina(kmParaRecorrer,rendimientoKm):
    gasolinaRequerida = kmParaRecorrer/rendimientoKm
    return gasolinaRequerida



def main():
    kmRecoridos = int(input("Teclea el numero de km recorridos"))
    litrosGasolina = int(input("Teclea el numero de litros de gasolina usados"))
    rendimientoKm=calcularRendimientoKm(kmRecoridos,litrosGasolina)
    rendimientoMillas=calcularRendimientoMillas(kmRecoridos, litrosGasolina)
    print("Si recorres ",kmRecoridos," con ",litrosGasolina,"tu rendimiento es de")
    print("El rendimiento del coche es de %.2f"%rendimientoKm,"km/L")
    print("El rendimietno del coche es de %.2f"%rendimientoMillas,"millas/Galon")
    kmParaRecorrer = int(input("Cuantos kilometros vas a recorrer ? "))
    gasolinasReq=calcularLitrosGasolina(kmParaRecorrer,rendimientoKm)
    print("La gasolina necesaria para recorrer ",kmParaRecorrer,"es de %.2f"%gasolinasReq,"litros")

main()
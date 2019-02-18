#Autor: Ivana Olvera Mérida A01746744
#Escribir un programa que lea el número de kilómetros recorridos y la cantidad de gasolina utilizada

def calcularMillas (kilometros):
    millas = kilometros * 1.6093
    return  millas

def calcularGalones(litros):
    galones = litros / 0.264
    return galones

def calcularRendimientoKm (kilometros, litros):
    rendimientoKm = kilometros/litros
    return rendimientoKm

def calcularRendimientoMi(millasC, galonesC):
    rendimientoMi = millasC / galonesC
    return rendimientoMi

def calcularLitros (kilometros, litros, kmPorRecorrer):
    litrosTotales = kmPorRecorrer/litros
    return litrosTotales

def calcularKmaRecorrer(recorrer, rendimientoKmC):
    litrospararecorrer = rendimientoKmC/recorrer
    return litrospararecorrer

def main ():
    kilometros = int(input("Teclea el número de kilómetros recorridos:"))
    litros = int(input("Teclea el número de litros de gasolina usados:"))
    recorrer = int(input("¿Cuántos km vas a recorrer?"))
    millasC = calcularMillas(kilometros)
    galonesC = calcularGalones(litros)
    rendimientoKmC = calcularRendimientoKm(kilometros, litros)
    rendimientoMiC = calcularRendimientoMi(millasC, galonesC)
    litrosPara = calcularKmaRecorrer(rendimientoKmC, recorrer)

    print ("Si recorres " + str(kilometros) + " kms con " + str(litros) + " de gasolina, el redimiento es:" )
    print("%.2f"% (rendimientoKmC)+ " km/l")
    print("%.2f"% (rendimientoMiC) + " mi/gal")
    print("Para recorrer " + str(recorrer) + "km. necesitas " + "%.2f"% (litrosPara) + " litros de gasolina")

main ()
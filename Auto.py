#Bruno Omaer Jiménez Mancilla
#Programa que analiza la eficiencia de un auto
def convertirKmAMi(kilometros):
    Mi = kilometros/1.609
    return Mi
def convertirLirosAGalones(litros):
    Gal = litros / 3.785
    return Gal
def rendimientoEnKmXHr(kilometro,litros):
    R = kilometro/litros
    return R
def rendimientoenMiXGal(millas,galones):
    R2 = millas/galones
    return R2
def calcularGasolina(kilometros,litros,kilometros2):
    liNecesarios = (litros*kilometros2)/kilometros
    return liNecesarios

def main ():
    km = float(input("Teclea el número de km recorridos: "))
    li = float(input("Teclea el número de litros de gasolina usados: "))
    mi = convertirKmAMi(km)
    gal = convertirLirosAGalones(li)
    R1 = rendimientoEnKmXHr(km,li)
    R2 = rendimientoenMiXGal(mi,gal)
    print("Si recorres ",km," kms con ",li,"litros de gasolina, el rendimiento es: ")
    print(round(R1,2)," km/l")
    print(round(R2, 2), " mi/gal")
    km2 = float(input("¿Cuántos kilometros vas a recorrer? "))
    gasolinaN = calcularGasolina(km,li,km2)
    print("Para recorrer ",km2, "necesitas ",round(gasolinaN,2), " litros de gasolina.")



main()
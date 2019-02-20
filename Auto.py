#Autor: Katia Hernández Barrera
#Descripción: programa que calcula el rendimiento de un automovil

def main():
    km = int(input("Teclea el número de km recorridos: "))
    l = int(input("Teclea el número de litros de gasolina usados: "))
    rend = calcularRendimientoKM(km,l)
    rendimiento = calcularRendimientoMi(km,l)
    print("                                                   ")
    print("Si recorres",km,"kms con",l,"litros de gasolina, el rendimiento es:")
    print("%.2f"% rend,"km/l")
    print("%.2f" % rendimiento,"mi/gal")
    print("                                                   ")
    kmPorRecorrer = int(input("¿Cuántos kilómetros vas a recorrer?"))
    gasolina = calcularGasolina(km,l,kmPorRecorrer)
    print("                                                   ")
    print("Para recorrer",kmPorRecorrer,"km","necesitas","%.2f"%gasolina,"litros de gasolina")



def calcularRendimientoKM(km,l):
    rend = km/l
    return rend

def calcularRendimientoMi(km,l):
    rendimiento = (km*0.62138)/ (l*0.264)
    return rendimiento

def calcularGasolina(km,l,kmPorRecorrer):
    gasolina = kmPorRecorrer/(km/l)
    return gasolina



main()
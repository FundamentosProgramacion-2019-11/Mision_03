# Autor: YadiraFuentesCalderón, A01745235
# Descripcion: Calcular el rendimiento de un coche en km/l, mi/gal y cuantos litros son necesarios si se quiere seguir con el rendimiento en x km

def calcularRendimientoKmL(kmRecorridos, litrosGasolina):
    rendimientoKmL= kmRecorridos/litrosGasolina
    return rendimientoKmL

def calcularRendimientoMiGal(kmRecorridos, litrosGasolina):
    rendimientoMiGal= (kmRecorridos/1.6093)/(litrosGasolina*.264)
    return rendimientoMiGal

def calcularGasolinaNecesaria(rendimientoKmL, KmQueSeRecorreran):
    litrosNecesarios= KmQueSeRecorreran/rendimientoKmL
    return litrosNecesarios

def main():
    kmRecorridos= int(input("Teclea el número de km recorridos: "))
    litrosGasolina= int(input("Teclea el número de litros de gasolina usados: "))

    rendimientoKmL= calcularRendimientoKmL(kmRecorridos, litrosGasolina)
    rendimientoMiGal= calcularRendimientoMiGal(kmRecorridos, litrosGasolina)

    print ("Si recorres",kmRecorridos,"kms con",litrosGasolina,"litros de gasolina, el rendimiento es: ")
    print ("%.2f"%rendimientoKmL,"km/l")
    print ("%.2f"%rendimientoMiGal,"mi/gal")

    KmQueSeRecorreran= int(input("¿Cuántos kilómetros vas a recorrer? "))

    litrosNecesarios= calcularGasolinaNecesaria(rendimientoKmL, KmQueSeRecorreran)

    print ("Para recorrer",KmQueSeRecorreran,"km. necesitas %.2f"%litrosNecesarios,"litros de gasolina")

main()
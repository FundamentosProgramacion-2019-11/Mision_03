# Autor: Juan Carlos Flores García A01376511. Grupo 02.
# Programa que calcula el rendimiento de un automóvil.

# Función que calcula el rendimiento del automóvil de kilómetros entre litros de gasolina.
def calcularRendimientoKmL(kmRecorridos, litrosGasolina):
    rendimientoKmL = kmRecorridos / litrosGasolina
    return rendimientoKmL

# Función que calcula el rendimiento del automóvil de millas entre galones de gasolina.
def calcularRendimientoMiG(kmRecorridos, litrosGasolina):
    millas = kmRecorridos * (1 / 1.6093)
    galones = litrosGasolina * (0.264 / 1)
    rendimientoMiG = millas / galones
    return rendimientoMiG

# Función que calcula los litros de gasolina necesarios para recorrer cierta cantidad de kilómetros.
def calcularGasolinaNecesaria(kmARecorrer, rendimientoKmL):
    litrosNecesarios = kmARecorrer / rendimientoKmL
    return litrosNecesarios

# Función principal.
def main():
    kmRecorridos = int(input("Teclea el número de km recorridos: "))
    litrosGasolina = int(input("Teclea el número de litros de gasolina usados: "))
    rendimientoKmL = calcularRendimientoKmL(kmRecorridos, litrosGasolina)
    rendimientoMiG = calcularRendimientoMiG(kmRecorridos, litrosGasolina)
    print("")
    print("Si recorres", (kmRecorridos), "kms con", (litrosGasolina), "litros de gasolina, el rendimiento es: ")
    print("%.2f" % (rendimientoKmL), "km/l")
    print("%.2f" % (rendimientoMiG), "mi/gal")
    print("")
    kmARecorrer = int(input("¿Cuántos kilómetros vas a recorrer? "))
    gasolinaNecesaria = calcularGasolinaNecesaria(kmARecorrer, rendimientoKmL)
    print("")
    print("Para recorrer", (kmARecorrer), "km. necesitas", "%.2f" %  (gasolinaNecesaria), "litros de gasolina")

# Llamada a la función principal.
main()

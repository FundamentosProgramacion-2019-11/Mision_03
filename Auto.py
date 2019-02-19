# Roberto Castro Barrios A01748559
# Descripción: Programa que calcula el rendimiento de tu auto.
# Millas = 1.6093
# Galones = 0.264

#Esta funcion calula los litros para recorrer ciertos kilometros
def calcularLitros(kmRecorridos, litrosGas, litrosNecesarios) :
    total = (litrosNecesarios*litrosGas)/kmRecorridos
    return total

#Esta funcion convierte los kilometros y litros a millas y galones. Posteriormente, calcula el rendimiento
def rendimientoMiGal(kmRecorridos, litrosGas) :
    millas = kmRecorridos/1.6093
    galones = litrosGas*0.264
    total = millas/galones
    return total

#Esta funcion calcula el rendimiento en Kilometros/litros
def rendimientoKml(kmRecorridos, litrosGas) :
    total = kmRecorridos/litrosGas
    return total

#Esta es la funcion principal; encargada de leer, imprimir y recibir las funciones.
def main() :
    kmRecorridos = int(input("Teclea el numero de kilometros recorridos: "))
    litrosGas = int(input("Teclea el numero de litros de gasolina usados: "))
    rendimientoKml(kmRecorridos, litrosGas)
    rendimientoMiGal(kmRecorridos, litrosGas)
    rendimiento1 = rendimientoKml(kmRecorridos, litrosGas)
    rendimiento2 = rendimientoMiGal(kmRecorridos, litrosGas)
    print("Si recorres %d Kms con %d litros de gasolina, el rendimiento es: "%(kmRecorridos, litrosGas))
    print("%.2f Km/l"%(rendimiento1))
    print("%.2f mi/gal"%(rendimiento2))
    litrosNecesarios = int(input("¿Cuantos kilometros vas a recorrer? "))
    calcularLitros(kmRecorridos, litrosGas, litrosNecesarios)
    totalLitros = calcularLitros(kmRecorridos, litrosGas, litrosNecesarios)
    print("Para recorrer %d Km. Necesitas %.2f litros de gasolina"%(litrosNecesarios, totalLitros))

#Llama a la función -main-
main()


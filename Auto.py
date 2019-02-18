# Autor: Roberto Emmanuel González Muñoz A01376803
# Escribe un programa que lea el número de kilómetros recorridos
# y la cantidad de gasolina utilizada, y que imprima el rendimiento del automovil
# en kilometros/Litro y millas/galón.
# Después, el programa pregunta cuántos kilómetros
# va a viajar e imprime los litros de gasolina que necesitará.


def calcularRendimientoKm(km, L):
    rendimientoKmL = km/L
    return rendimientoKmL


def calcularRendimientoMg(km, L):
    rendimientoMG = (km / 1.6093) / (L * 0.264)
    return rendimientoMG


def main():
    # Pregunta los datos al usuario.
    kmRecorridos = int(input("Teclea el número de km recorridos: "))
    litrosUtilizados = int(input("Teclea el número de km recorridos: "))

    # Calcula rendimiento de la gasolina en Kilómetros por Litro.
    rendimientoKmL = calcularRendimientoKm(kmRecorridos, litrosUtilizados)

    # Calcula rendimiento de la gasolina en Millas por Galón.
    rendimientoMg = calcularRendimientoMg(kmRecorridos, litrosUtilizados)

    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
    print("Si recorres %d kms con %d litros de gasolina, el rendimiento es: " % (kmRecorridos, litrosUtilizados))
    print("%.2f km/l" % rendimientoKmL)
    print("%.2f mi/gal" % rendimientoMg)
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")

    # Pregunta al usuario su proximo recorrido y hace una aproximación de la gasolina que se usará.
    kmporRecorrer = int(input("¿Cuántos kilómetros vas a recorrer?: "))
    litrosNecesarios = kmporRecorrer/ rendimientoKmL

    print("Para recorrer %d km. Necesitas %.2f litros de gasolina." % (kmporRecorrer, litrosNecesarios))
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")


main()
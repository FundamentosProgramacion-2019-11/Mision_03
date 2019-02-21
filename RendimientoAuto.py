#Debido al aumento de la gasolina, los automovilistas están preocupados por el rendimiento de su auto. Los datos que
#tienen es el número de kilómetros que recorrieron y la cantidad de litros de gasolina que utilizaron en su último viaje.
#Escribe un programa que lea el número de kilómetros recorridos y la cantidad de gasolina utilizada, y que imprima lo
#siguiente:
#1) El rendimiento del automóvil en:
#a. kilómetros/litro.
#b. millas/galón. (1 milla = 1.6093 kilómetros, 1 litro = 0.264 galones)
#2) Después, el programa pregunta cuántos kilómetros va a viajar e imprime los litros de gasolina que necesitará.
#Debes usar funciones. Utiliza tantas como sean necesarias de acuerdo con tu diseño Top-Down. Imprime dos decimales.

def calcularKm(kmrecorridos, gasusada):
    Resultado1 = kmrecorridos/gasusada
    return Resultado1
def calcularMiles(galones, millas):
    Resultado2 = millas/galones
    return Resultado2

def calcularGasU(GasolinaUtilizada, rendimiento):
    Resultado3 = GasolinaUtilizada/rendimiento
    return Resultado3

def main():
    kmrecorridos = int(input("Teclea número de Km recorridos:"))
    gasusada = int(input("Teclea la cantidad de litros utilizados en los Km recorridos:"))
    galones = gasusada*0.264
    millas = kmrecorridos/1.6093
    redimientoKm = calcularKm(kmrecorridos, gasusada)
    rendimientomiles = calcularMiles(galones, millas)
    print("Si recorres", kmrecorridos, "km, el redimiento es:")
    print(redimientoKm, "km/l")
    print(rendimientomiles, "mi/gal")
    GasolinaUtilizada = int(input("¿Cuántos Km vas a recorrer? :"))
    GasU = calcularGasU(GasolinaUtilizada, redimientoKm)
    print("La gasolina que vas a gastar en", GasolinaUtilizada, "km, son", GasU, "litros.")

main()
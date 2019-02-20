#José Isidro Sánchez Vázquez
#Calculador del rendimiento de un auto
#Debido al aumento de la gasolina, los automovilistas están preocupados por el rendimiento de su auto.
# Los datos que tienen es el número de kilómetros que recorrieron y la cantidad de litros de gasolina que utilizaron en su último viaje.
#   Escribe un programa que lea el número de kilómetros recorridos y la cantidad de gasolina utilizada, y que imprima lo siguiente:
# 1) El rendimiento del automóvil en: a. kilómetros/litro. b. millas/galón. (1 milla = 1.6093 kilómetros, 1 litro = 0.264 galones)
# 2) Después, el programa pregunta cuántos kilómetros va a viajar e imprime los litros de gasolina que necesitará.
def calculadorDelRendimientoEnKmSobreLitro(kmRecorridos,LdeGasolina):
    rendimiento = kmRecorridos/LdeGasolina
    return rendimiento
def calculadorDelRendimientoEnMillaSobreGalon(kmRecorridos,LdeGasolina):
    conversionLitrosAgalones = LdeGasolina*0.264
    conversionKilometrosAmillas = kmRecorridos*1.6093
    rendimiento = conversionKilometrosAmillas/conversionLitrosAgalones
    return rendimiento
def calculadorDeLaCantidadDeGasolinaNecesaria(kmRecorridos,LdeGasolina,kilometros):
    gasolina = (kilometros*LdeGasolina)/kmRecorridos
    return gasolina
def main():
    kmRecorridos = int(input("Teclea el numero de km recorridos: "))
    LdeGasolina = int(input("Teclea el numero de litros de gasolina usados: "))
    rendimientoKmEntrel = calculadorDelRendimientoEnKmSobreLitro(kmRecorridos,LdeGasolina)
    rendimientoMiEntregal = calculadorDelRendimientoEnMillaSobreGalon(kmRecorridos,LdeGasolina)
    print("Si recorres",kmRecorridos,"km con",LdeGasolina,"litros de gasolina, el rendimiento es:")
    print("%.2f"%(rendimientoKmEntrel),"km/l")
    print("%.2f"%(rendimientoMiEntregal),"mi/gal")
    kilometros = int(input("¿Cuantos kilometros vas a recorrer? "))
    cantidadDeGasolina = calculadorDeLaCantidadDeGasolinaNecesaria(kmRecorridos,LdeGasolina,kilometros)
    print("Para recorrer",kilometros,"km. necesitas%.2f" % (cantidadDeGasolina),"litros de gasolina")

main()
#Autor: Luis Alberto Zepeda Hernandez, A01328616.
#Descripcion: Escribe un programa que lea el número de kilómetros recorridos
# y la cantidad de gasolina utilizada, y que imprima, rendimiento en km/lts, mi/gal,
#el programa pregunta cuántos kilómetros va a viajar e imprime los litros de gasolina que necesitará.


#se encarga de calcular cuantos  litros se requieren para recorrer cierta cantidad de km. Regresa el valor.
def calculaLitrosParaRecorrer(kmPorRecorrer):
    litrosNecesarios = (17 * kmPorRecorrer) / 475
    return litrosNecesarios
#se encarga de hacer la conversión de litros a galones, y regresa el valor.
def calculaConversionGal(gasolinaUsada):
    conversionGalones = gasolinaUsada * 0.264
    return conversionGalones

#se encarga de hacer la conversión  de km a mi, y regresa el valor.
def calculaConversionMi(kmRecorridos):
    conversionMillas = kmRecorridos / 1.6093
    return conversionMillas

#se encarga de calcualr el rendimiento en mi/gal, llama a funciones que realizan la conversión de km a mi, lts a gal, y regresa el resultado
def calculaRendiminetoMi(kmRecorridos,gasolinaUsada):
    conversionMi = calculaConversionMi(kmRecorridos)
    conversionGal = calculaConversionGal(gasolinaUsada)
    rendimiento = conversionMi / conversionGal
    return rendimiento

#se encarga de calcualr el rendimiento en km/l con los datos recolectados por main, regresa los resultados.
def calculaRendimientoKm(kmRecorridos,gasolinaUsada):
    rendimiento = kmRecorridos / gasolinaUsada
    return rendimiento

#se encarga de pedir la información al usuario, llama a otras funciones para calcular los resultados e imprimirlos.
def main():
    kmRecorridos = int(input("Teclea el número de km recorridos: "))
    gasolinaUsada = int(input("Teclea el número de litros de gasolina usados: "))
    rendimientoKm = calculaRendimientoKm(kmRecorridos, gasolinaUsada)
    rendimientoMi = calculaRendiminetoMi(kmRecorridos, gasolinaUsada)
    print()
    print("Si recorres",kmRecorridos, "kms con",gasolinaUsada, "litros de gasolina, el rendimiento es:")
    print("{0:.2f}".format(rendimientoKm),"km/l")
    print("{0:.2f}".format(rendimientoMi),"mi/gal")
    print()

    kmPorRecorrer = int(input("¿Cuántos kilómetros vas a recorrer? "))
    litrosNecesarios = calculaLitrosParaRecorrer(kmPorRecorrer)
    print()
    print("Para recorrer",kmPorRecorrer,"km. necesitas","{0:.2f}".format(litrosNecesarios),"litros de gasolina")



main()
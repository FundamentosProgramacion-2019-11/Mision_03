#Marianela Contreras D.
# Programa para conocer el rendimiento de un carro en km/l y mi/gal.

#Función para calcular el rendimiento del carro en kilometros/litro
def calcularKilometrosLitros(kilometros,litros):
    kilometrosLitros= kilometros/litros
    return kilometrosLitros

#Función para calcular el rendimiento del carro en millas/galones
def calcularMillasGalones(kilometros,litros):
    millasGalones= (kilometros/1.6093)/(litros*.264)
    return millasGalones

#Función para calcular los litros necesarios para recorrer la distancia del usuario
def calcularLitrosNecesarios(kilometros,litros,kilometrosRecorrer):
    kilometrosLitros = calcularKilometrosLitros(kilometros,litros)
    litrosNecesarios = kilometrosRecorrer/kilometrosLitros
    return litrosNecesarios

#Función principal del programa y la que correrá. Las lecturas e impresiones se hacen en esta función.
def main():
    kilometros = float(input("Teclea el número de km recorridos:"))
    litros = float(input("Teclea el número de litros de gasolina usados:"))
    calcularKilometrosLitros(kilometros,litros)
    calcularMillasGalones(kilometros,litros)
    kilometrosLitros= calcularKilometrosLitros(kilometros,litros)
    millasGalones = calcularMillasGalones(kilometros,litros)
    print("\nSi recorres %d"% kilometros, "kms con %d" %litros, "litros de gasolina, el rendimiento es: \n %.2f"% kilometrosLitros,"km/l \n %.2f" %millasGalones,"mi/gal")
    kilometrosRecorrer = float(input("\n¿Cuántos kilómetros vas a recorrer?"))
    calcularLitrosNecesarios(kilometros,litros,kilometrosRecorrer)
    litrosNecesarios= calcularLitrosNecesarios(kilometros,litros,kilometrosRecorrer)
    print("\nPara recorrer %d"%kilometrosRecorrer, "km. Necesitas %.2f"%litrosNecesarios, "litros de gasolina")


main()
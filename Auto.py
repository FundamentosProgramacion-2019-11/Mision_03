#Autor: Mario Hernández Cárdenas
# Calcular el rendimiento de gasolina de un auto en kilometros y millas segun los litros

def calcularRendimientoKilometros(kilometros, litros):   #Divide los kilometros entre los litros para obtener rendimiento
    rendimientoKilometros = kilometros/litros
    return rendimientoKilometros

def calcularRendimientoMillas(kilometros, litros):   #Convierte kilometros y litros a millas y galones, divide y obtiene rendimiento
    millas = kilometros / 1.6093
    galones = litros * 0.264
    rendimientoMillas = millas/galones
    return rendimientoMillas

def calcularRendimiento(kilometrosPorRecorrer, rendimientoKilometros):   #Utiliza el rendimiento de kilometros para pronosticar los litros de combustible que se necesitan
    rendimientoFuturo = kilometrosPorRecorrer / rendimientoKilometros
    return rendimientoFuturo

def main():
    kilometros = int(input("Teclea el número de km recorridos: "))
    litros = int(input("Teclea el número de litros de gasolina usados: "))
    rendimientoKilometros = calcularRendimientoKilometros(kilometros, litros)
    rendimientoMillas = calcularRendimientoMillas(kilometros, litros)
    print("\nSi recorres", kilometros, "kms con", litros, "litros de gasolina, el rendimiento es: \n %.2f"
                                                        %rendimientoKilometros, "km/l\n %.2f"
                                                        %rendimientoMillas, "mi/gal\n")
    kilometrosPorRecorrer = int(input("¿Cuántos kilómetros vas a recorrer? "))
    rendimientoFuturo = calcularRendimiento(kilometrosPorRecorrer, rendimientoKilometros)
    print("Para recorrer", kilometrosPorRecorrer,"km. necesitas %.2f"%rendimientoFuturo, "litros de gasolina")

main()
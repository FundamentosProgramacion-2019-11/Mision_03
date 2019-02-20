#Autor: Elizabeth Citlalli Zapata Cortes
#Descripción: Aporta el rendimiento del automovil en kilometro/litro y millas/ galón,
#             pregunta cuantos va a recorrer y calcula la cantidad de gasolina necesaria.

def calcularLitros(kmRecorridos, litrosUsados,kmFuturos):
    litrosFuturos = (kmFuturos * litrosUsados) / kmRecorridos
    return litrosFuturos

def calcularMillasGalon(kmRecorridos,litrosUsados):
    milla = kmRecorridos / 1.6093
    galon = litrosUsados * 0.264
    miGal = milla / galon
    return miGal

def calcularKilometroLitro(kmRecorridos, litrosUsados):
    kmL = kmRecorridos / litrosUsados
    return kmL

def main():
    kmRecorridos = int(input("Teclea el número de km recorridos: "))
    litrosUsados = int(input("Teclea el número de litros de gasolina usados: "))
    print()
    print("Si recorres ", (kmRecorridos), "kms con", (litrosUsados), "litros de gasolina, el rendimiento es: ")
    print("%.2f" % (calcularKilometroLitro(kmRecorridos, litrosUsados)), "km/l")
    print("%.2f" % (calcularMillasGalon(kmRecorridos,litrosUsados)), "mi/gal")
    print()

    kmFuturos = int(input("¿Cuántos kilómetros vas a recorrer? "))
    print()
    print("Para recorrer", (kmFuturos), "km. necesitas %.2f" % (calcularLitros(kmRecorridos, litrosUsados,kmFuturos)), "litros de gasolina")

main()
# Autor: Rosalía Serrano Herrera
# Calcula el rendimiento del automóvil en función de los km recorridos y la gasolina utilizada, calcula la gasolina necesaria para recorrer cierta distancia

def calcularRendimientoKL(kilometros, gasolina):
    rendimientoKL = kilometros/gasolina
    return rendimientoKL

def calcularRendimientoMG(kilometros, gasolina):
    rendimientoMG = (kilometros/1.6093)/(gasolina*0.264)
    return rendimientoMG

def calcularGasolina(km, rendimientoKL):
    gas = km / rendimientoKL
    return gas

def main():
    kilometros = int(input("Teclea el número de km recorridos: "))
    gasolina = int(input("Teclea el número de litros de gasolina usados: "))
    rendimientoKL = calcularRendimientoKL(kilometros, gasolina)
    rendimientoMG = calcularRendimientoMG(kilometros, gasolina)
    print("\n" "Si recorres", kilometros, "kms con", gasolina, "litros de gasolina, el rendimiento es: ")
    print("%.2f" % (rendimientoKL), "km/l")
    print("%.2f" % (rendimientoMG), "mi/gal")
    km = int(input("\n" "¿Cuántos kilómetros vas a recorrer? "))
    gas = calcularGasolina(km, rendimientoKL)
    print("\n" "Para recorrer", km, "km. necesitas %.2f" % (gas), "litros de gasolina")

main()
#Luis Adrian Carmona Villalobos
#A01748395

def calcularRendimientoKmL(kmRecorridos, litrosGasolina):
    rendimientoKmL = kmRecorridos/litrosGasolina
    return rendimientoKmL
def calcularRendimientoMiGal(kmRecorridos, litrosGasolina):
    millas = kmRecorridos*0.621371
    galon = litrosGasolina*0.264172
    rendimientoMiG = millas*galon
    return rendimientoMiG

def main():
    kmRecorridos = float(input("Teclea el numero de km recorridos: "))
    litrosGasolina = float(input("Teclea el numero de litros de gasolina usados: "))

    print("Si recorres: ", kmRecorridos, "con", litrosGasolina, "el rendimiento es,:")
    print(calcularRendimientoKmL(kmRecorridos, litrosGasolina)
    print(calcularRendimientoMiGal(kmRecorridos, litrosGasolina))
main()

#Autor: Karla Ximena Rueda Ruiz
#Aplicar la técnica Top-Down para calcular precio total de boletos de acuerdo a una zona en específico.

def main():
    kilometros=int(input("Teclea el número de km recorridos:"))
    litros=int(input("Teclea el número de litros de gasolina usados:"))

    kml=calcularRendimientokm(kilometros,litros)
    print("El rendimiento en kilometros es=", format(kml, ".2f"))
    miG=calcularRendimientomiG(kilometros,litros)
    print("El rendimiento en litros es=", format(miG,".2f"))

    kmrecorridos=int(input("¿Cuántos km vas a recorrer?:"))

    litrosgasolina=calcularLitrosgasolina(kmrecorridos,kml)
    print("Litros de gasolina que necesitas=", format(litrosgasolina, ".2f"))

def calcularRendimientokm(kilometros,litros):
    kml=(kilometros/litros)
    return kml

def calcularRendimientomiG(kilometros,litros):
    miG=(kilometros*0.6213)/(litros*0.264)
    return miG

def calcularLitrosgasolina(kmrecorridos,kml):
    litrosgasolina=kmrecorridos/kml
    return litrosgasolina

main()


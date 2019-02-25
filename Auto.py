# AUTOR: Paulina Guerrero Ruiz
# Calcular rendimiento de auto


def calcularRendimientoA (kilometros, litros):
    rendimientoA = kilometros/litros
    return rendimientoA

def calcularRendimientoB (kilometros, litros):
    millas = (kilometros * 0.62137)
    galones = (litros * 0.264)
    rendimientoB = millas / galones
    return rendimientoB


def main():

    kilometros = int(input("Teclea el numero de kilometros recorridos: "))
    litros = int(input("Teclea el numero de litros usados: "))
    rendimientoA = calcularRendimientoA(kilometros, litros)
    rendimientoB = calcularRendimientoB(kilometros,litros)
    print ("Si recorres", kilometros, "km", "con", litros, "litros de gasolina, el rendimiento es: ")
    print (rendimientoA, "km/l")
    print (rendimientoB, "ml/gal")




main ()
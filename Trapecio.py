# Bruno Omar Jiméenz Mancilla
# Programa que calcula area y perimetro de un trapecio
import math
def AreaTrapecio(baseMenor,baseMayor,altura):
    areaTotal = ((baseMayor*baseMenor)/2)*altura
    return areaTotal

def PerimetroTrapecio(baseMenor,baseMayor,altura):
    x = baseMayor-baseMenor
    y = x/2
    z = math.sqrt((altura**2)+(y**2))
    pt = baseMayor+baseMenor+(2*z)
    return pt

def main():
    b = float(input("¿Cuál es la base menor del trapecio? "))
    B = float(input("¿Cuál es la base mayor del trapecio? "))
    a = float(input("¿Cuál es la altura del trapecio? "))
    at = AreaTrapecio(b,B,a)
    pt = PerimetroTrapecio(b,B,a)
    print("Área: ",round(at,2),)
    print("Perimetro: ",round(pt,2))
main()
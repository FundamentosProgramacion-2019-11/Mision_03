#Autor: César Guzmán Guadarrama
#Descripción: Este programa te dice el area y el perimetro de un trapecio

import math

def calcularArea(BA,f,h):   #esta función saca el área del trapecio
    A = ((BA +f) / 2) * h
    return A

def calcularPerimetro(BA,baseMenor,h):    #esta función saca el perimetro del trapecio
    lado4 = (BA - baseMenor) / 2
    ladoC = math.sqrt((lado4)**2 + (h)**2)
    P = 2*ladoC + BA + baseMenor
    return P


def main():             #funcion principal pide valores para resolver el problema
    baseMayor = float(input("Dame la longitud de la base mayor"))
    baseMenor = float(input("Dame la longitud de la base menor"))
    altura = float(input("Dame la longitud de la altura"))
    print("El area es de ",round(calcularArea(baseMayor,baseMenor,altura),2), "m2")
    print("El perimetro es de ",round(calcularPerimetro(baseMayor,baseMenor,altura),2), "m")

main()
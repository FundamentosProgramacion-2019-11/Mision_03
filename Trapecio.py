# Autor: Luis Renteria
# Calcular area y perimetro de trapecio con funciones

import math


def calcularArea(baseMayor, baseMenor, altura):
    Area=((baseMayor+baseMenor)*(altura))/2
    return Area

def calcularPerimetro(baseMayor, baseMenor, altura):
    lado=math.sqrt(((baseMayor-baseMenor)/2)**2)+((altura)**2)
    Perimetro=(lado*2)+baseMenor+baseMayor
    return Perimetro

def main():
    baseMayor=int(input("inserte la base mayor:"))
    baseMenor=int(input("inserte la base menor:"))
    altura=int(input("inserte la altura:"))
    calcularArea(baseMayor, baseMenor, altura)
    calcularPerimetro(baseMayor, baseMenor, altura)
    print ("El area del trapecio es:",calcularArea(baseMayor, baseMenor, altura))
    print ("El perimetro del trapecio es:",calcularPerimetro(baseMayor, baseMenor, altura))


main()
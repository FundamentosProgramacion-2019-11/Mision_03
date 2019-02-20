#Autor: Diego Raul Elizalde Uriarte
#Calcular Area y perimetro de un trapecio

import math as m

def calcularArea(baseMayor,baseMenor,altura):
    Area = ((baseMayor+baseMenor)/2)*(altura)
    return Area



def calcularPerimetro(baseMayor,baseMenor,altura):
    a = (baseMayor-baseMenor)/2
    c = m.sqrt(((a)**2)+(altura)**2)
    Perimetro = baseMenor+baseMayor+(c*2)
    return Perimetro




def main():
    baseMayor = int(input("Escribe la longitud de la base mayor: "))
    baseMenor = int(input("Escribe la longitud de la base menor: "))
    altura = int(input("Escribe la altura: "))
    calcularArea(baseMayor,baseMenor,altura)
    print("Area: %.2f" % (calcularArea(baseMayor,baseMenor,altura)))
    calcularPerimetro(baseMayor,baseMenor,altura)
    print("Perimetro: %.2f" % (calcularPerimetro(baseMayor,baseMenor,altura)))







main()
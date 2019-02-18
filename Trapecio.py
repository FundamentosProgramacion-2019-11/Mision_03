# Autor: Ronaldo Estefano Lira Buendia
# Calcular el area y el perimetro de un trapecio

import math

def calcularArea(baseMayor, baseMenor, altura):
    area = ((baseMayor + baseMenor)/2)*altura
    return area

def calcularPerimetro(baseMayor, baseMenor, altura):
    x = (baseMayor - baseMenor)/2
    c = math.sqrt((x**2)+(altura**2))
    perimetro = baseMayor + baseMenor + (2*c)
    return perimetro

def  main():
    baseMayor = int(input("Dame la longitud de la base mayor: "))
    baseMenor = int(input("Dame la longitud de la base menor: "))
    altura = int(input("Dame la altura: "))
    area = calcularArea(baseMayor, baseMenor, altura)
    print("Area: {0:.2f}".format(area))
    perimetro = calcularPerimetro(baseMayor, baseMenor, altura)
    print("Perimetro: {0:.2f}".format(perimetro))



main ()
# Roberto Castro Barrios A01748559
# Descripción: Programa que calcula el área y perímetro de un trapecio isósceles.

import math as m

##Esta funcion mediante el teorema de pitagoras, calcula el lado c y posteriormente, el perimetro
def calcularPerimetro(baseMenor, baseMayor, altura) :
    baseA= (baseMayor-baseMenor)/2
    ladoC= m.sqrt((baseA**2)+(altura**2))
    totalPerimetro = baseMayor+baseMenor+(2*ladoC)
    return totalPerimetro

#Esta funcion calcula el area total
def calcularArea(baseMenor, baseMayor, altura) :
    totalArea = ((baseMayor + baseMenor)/2)*altura
    return totalArea

#Esta es la funcion principal; encargada de leer, imprimir y recibir las funciones.
def main() :
    baseMayor = float(input("Ingresa la base Mayor de tu trapecio: "))
    baseMenor = float(input("Ingresa la base Menor de tu trapecio: "))
    altura = float(input("Ingresa la altura de tu trapecio: "))
    calcularArea(baseMenor, baseMayor, altura)
    calcularPerimetro(baseMenor, baseMayor, altura)
    totalArea = calcularArea(baseMenor, baseMayor, altura)
    totalPerimetro = calcularPerimetro(baseMenor, baseMayor, altura)
    print("Área: %.2f"%(totalArea))
    print("Perímetro: %.2f"%(totalPerimetro))

#Llama a la función -main-
main()

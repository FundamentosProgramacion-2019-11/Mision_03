#Autor: Katia Hernández Barrera
#Descripción: programa que calcula el área y perímetro de un trapecio isósceles.

import math
def calcularArea (baseMayor, baseMenor, altura):
   area = ((baseMayor + baseMenor) * altura) /2
   return area

def calcularPerimetro (baseMayor, baseMenor, altura):
    #lado = math.sqrt(((baseMayor - baseMenor/2)**2 + (altura**2)))
    lado = altura/math.sin(math.radians(60))
    perimetro = baseMayor + baseMenor + (lado * 2)
    return perimetro

def main():
    baseMayor = int(input("teclee la base mayor"))
    baseMenor = int(input("teclee la base menor"))
    altura = int(input("teclee la altura"))
    area = calcularArea(baseMayor, baseMenor, altura)
    print("Área: %.2f" % area)
    perimetro = calcularPerimetro(baseMayor, baseMenor, altura)
    print("Perímetro:%.2f"% perimetro)


main()
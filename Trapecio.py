#FRANCISCO JAVIER GONZALEZ MOLINA A01748636
#PROGRAMA QUE CALCULA AREA DE UN TRAPECIO

import math

#En esta funcion se calcula el area del trapecio utilizando su formula
#regresando el area del trapecio
def calcularArea (baseMayor,baseMenor,altura):
    area= ((baseMayor+baseMenor)/2)*altura
    return area

#En esta funcion se calcula el perimetro, en cual tambien en esta funcion se
#calculó el lado faltante del trapecio usando teorema de pitagoras, en el cual se
#realizo un trianngulo a partir de la altura. Al final, la funcion regresa el valor del perimetro.
def calculaPerimetro (baseMayor,baseMenor,altura):
    basedeltriangulo=(baseMayor-baseMenor)/2
    hipotenusatriangulo= math.sqrt((basedeltriangulo**2)+(altura**2))
    perimetro=baseMayor+baseMenor+(2*hipotenusatriangulo)
    return perimetro

#Esta funcion lee valores del usuario y realiza las operaciones para calcular el area y
#perimetro del trapecio
def main ():
    baseMayor=int(input("Escribe longitud de la base mayor: "))
    baseMenor=int(input("Escribe longitud de la base menor: "))
    altura=int(input("Escribe la altura: "))
    area=calcularArea(baseMayor,baseMenor,altura)
    perimetro=calculaPerimetro(baseMayor,baseMenor,altura)
    print ("""
    Area: %.2f
    Perimetro: %.2f"""%(area,perimetro))

#llama la funcion "main()"
main()
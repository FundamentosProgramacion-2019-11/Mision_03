#Autor: Marianela Contreras D.
#Programa para calcualr el área y perímetro de un trapecio.

#función para calcular el área del trapecio.
def calcularArea(baseMayor,baseMenor,h):
    area= ((baseMayor+baseMenor)/2)*h
    return area

#función para calcular el perímetro del trapecio.
def calcularPerimetro(baseMayor,baseMenor,h):
    lado = ((((baseMayor - baseMenor) / 2) ** 2) + (h ** 2)) ** .5
    perimetro = lado + lado + baseMenor + baseMayor
    return perimetro

#función principal del programa y la que se correrá. Las lecturas e impresiones se hacen en esta función.
def main():
    baseMayor= float(input("Escribe la longitud de la base mayor:"))
    baseMenor= float(input("Escribe la longitud de la base menor:"))
    h = float(input("Escribe la altura:"))
    calcularArea(baseMayor,baseMenor,h)
    area = calcularArea(baseMayor, baseMenor, h)
    perimetro = calcularPerimetro(baseMayor, baseMenor, h)
    print("Área: %.2f" % area)
    print("Perímetro: %.2f" % perimetro)


main()
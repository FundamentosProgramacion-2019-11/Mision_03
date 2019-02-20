#Autor: Karla Ximena Rueda Ruiz
#Aplicar la técnica Top-Down para calcular área y perímetro de un trapecio

def main():

    basemayor= int(input("Inserte valor de la base mayor : "))
    basemenor= int(input("Inserte valor de la base menor : "))
    altura= int(input("Inserte valor de la altura : "))

    area=calcularArea(basemenor,basemayor,altura)
    print("Área =", format(area, ".2f"))

    perimetro=calcularPerimetro(basemayor,basemenor,altura)
    print("Perímetro =", format(perimetro, ".2f"))

def calcularArea(basemenor, basemayor, altura):
    area=(basemayor+basemenor)*(altura)/2

    return area

def calcularPerimetro(basemayor, basemenor, altura):
    lado=Calcularlado (basemayor, basemenor, altura)
    perimetro= (basemayor+basemenor+lado+lado)

    return perimetro

def Calcularlado (basemayor, basemenor, altura):
    x=(basemayor-basemenor)/2
    lado=(x**2+altura**2)**0.5

    return lado



main ()
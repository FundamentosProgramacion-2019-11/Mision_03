# Autor: YadiraFuentesCalderón, A01745235
# Descripcion: Calcular el are y perimetro de un trapecio

def calcularArea(baseMayor, baseMenor, altura):
    area= ((baseMayor+baseMenor)/2)*altura
    return area

def calcularPerimetro(baseMayor, baseMenor, altura):
    hipotenusa= ((((baseMayor-baseMenor)/2)**2)+(altura**2))**.5
    perimetro= baseMayor+baseMenor+(hipotenusa*2)
    return perimetro

def main():
    baseMayor= int(input("Escribe la longitud de la base mayor: "))
    baseMenor = int(input("Escribe la longitud de la base menor: "))
    altura= int(input("Escribe la altura: "))

    area= calcularArea(baseMayor, baseMenor, altura)
    perimetro= calcularPerimetro(baseMayor, baseMenor, altura)

    print ("Área: %.2f"%area)
    print("Perímetro: %.2f" % perimetro)
main()

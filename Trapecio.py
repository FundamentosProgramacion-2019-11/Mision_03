#Autor: Aline Paulette Villegas Berdejo
#Calcula el perímetro y área de un trapecio isósceles

#Calcula área con de un trapecio isósceles
def calcularArea(baseMayor, baseMenor, altura):
    area= ((baseMayor+baseMenor)/2) *altura
    return area

#Calcula el perímetro de un trapecio isósceles
def calcularPerimetro(baseMayor, baseMenor, altura):
    baseTriangulo= (baseMayor-baseMenor)/2
    ladoTriangulo= ((baseTriangulo**2)+(altura**2))**.5
    perimetro= baseMenor+baseMayor+ladoTriangulo+ladoTriangulo
    return perimetro

#Indica las funciones que se van a correr al llamar a la funición "main()"  (Lee datos, imprime datos)
def main():
    baseMayor= int(input("Escribe la longitud de la base mayor: "))
    baseMenor= int(input("Escribe la longitud de la base menor: "))
    altura= int(input("Escribe la altura: "))
    calcularArea(baseMayor, baseMenor, altura)
    calcularPerimetro(baseMayor, baseMenor, altura)
    area= calcularArea(baseMayor, baseMenor, altura)
    print("Área: %.2f" % area)
    perimetro= calcularPerimetro(baseMayor, baseMenor, altura)
    print("Perímetro: %.2f" % perimetro)


main()

#Luis Fernando Duran Castillo
#Calcular el area y perimetro del trapecio

def calcularPerimetro(baseMayor, basemenor, altura):
    perimetro= baseMayor + basemenor + (2*altura)
    return perimetro

def calculararea(baseMayor, basemenor, altura):
    area= ((baseMayor + basemenor)/2)* altura
    return area

def imprimir(baseMayor, basemenor, altura):
    print("el perimetro del trapecio es de: ",calcularPerimetro(baseMayor, basemenor, altura))
    print("el area del trapecio es de",calculararea(baseMayor, basemenor, altura))

def main():
    baseMayor= int(input("cuanto mide la base mayor? "))
    basemenor= int(input("cuanto mide la base menor "))
    altura= int(input("cuanto mide la altura? "))
    calcularPerimetro(baseMayor, basemenor, altura)
    calculararea(baseMayor, basemenor, altura)
    imprimir(baseMayor, basemenor, altura)

main()
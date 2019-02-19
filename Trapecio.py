#Autor: Yasmín Landaverde Nava
#Descripción: este programa calcula el área y perímetro de un trapecio


def calcularArea(baseMayor, baseMenor, altura):
    area = ((baseMayor + baseMenor)/2) * altura
    return area

def imprimirArea(baseMayor, baseMenor, altura):
    area = calcularArea(baseMayor, baseMenor, altura)
    print("El area es: ", area)

def calcularPerimetro(baseMayor, baseMenor, altura):
    a = (baseMayor - baseMenor) / 2
    hipotenusa = ((a ** 2) + (altura ** 2)) ** .5
    return hipotenusa
    hipotenusa = calcularLado(baseMayor, baseMenor, altura)
    perimetro = baseMenor + baseMayor + hipotenusa + hipotenusa
    return perimetro

def imprimirPerimetro(baseMayor, baseMenor, altura):
    perimetro =  calcularPerimetro(baseMayor, baseMenor, altura)
    print ("El perímetro es de: ", "%.2f" % perimetro)


def main():
    baseMayor = int(input("Escribe la longitud de la base mayor: "))
    baseMenor = int(input("Escribe la longitud de la base menor: "))
    altura = int(input("Escribe la longitud de la altura: "))
    calcularArea(baseMayor, baseMenor, altura)
    imprimirArea(baseMayor, baseMenor, altura)
    calcularPerimetro(baseMayor, baseMenor, altura)
    imprimirPerimetro(baseMayor, baseMenor, altura)



main()
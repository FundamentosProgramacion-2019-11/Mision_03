# Autor: Rosalía Serrano Herrera
# Calcula el área y perímetro de un trapecio

def calcularArea(baseMayor, baseMenor, altura):
    area = altura * ((baseMayor+baseMenor)/2)
    return area

def calcularPerimetro(baseMayor, baseMenor, altura):
    base = (((baseMayor-baseMenor)/2))
    hipotenusa = (base**2 + altura**2)**0.5
    perimetro = baseMayor + baseMenor + hipotenusa*2
    return perimetro

def main():
    baseMayor = int(input("Escribe la longitud de la base mayor: "))
    baseMenor = int(input("Escribe la longitud de la base menor: "))
    altura = int(input("Escribe la altura: "))
    area = calcularArea(baseMayor, baseMenor, altura)
    perimetro = calcularPerimetro(baseMayor, baseMenor, altura)
    print("Área: %.2f" % (area))
    print("Perímetro: %.2f" % (perimetro))

main()
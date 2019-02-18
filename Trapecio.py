#Autor: Ivana Olvera Mérida A01746744
#Escribir un programa que lea la base mayor, la base menor, la altura del trapecio e imprima el área y el perímetro

def calcularPerimetro(baseMayor, baseMenor, altura):
    base = (baseMayor - baseMenor)/2
    lado = (base**2 + altura**2)**0.5
    perimetro = baseMayor + baseMenor + (2*lado)
    return perimetro

def calcularArea(baseMayor, baseMenor, altura):
    area = (baseMayor + baseMenor)*altura/2
    return area

def main ():
    baseMayor = int(input("Escribe la longitud de la base mayor:"))
    baseMenor = int(input("Escribe la longitud de la base menor:"))
    altura = int(input("Escribe la altura:"))
    area = calcularArea(baseMayor, baseMenor, altura)
    perimetro = calcularPerimetro(baseMayor, baseMenor, altura)
    print("Área: %.2f" % (area))
    print("Perímetro: %.2f" % (perimetro))

main ()
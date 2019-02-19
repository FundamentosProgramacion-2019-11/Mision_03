#Autor: Mario Hernández Cárdenas
# Calcular el área y perímetro de un trapecio

def calcularArea(baseMayor, baseMenor, altura):    #Calcula el area del trapecio
    area = ((baseMayor + baseMenor)/2) * altura
    return area

def calcularHipotenusa(baseMayor, baseMenor, altura):    #Obtiene la hipotenusa para calcular el perimetro
    base = (baseMayor - baseMenor)/2
    hipotenusa = (base**2 + altura**2)**0.5
    return hipotenusa

def calcularPerimetro(baseMayor, baseMenor, hipotenusa):     #Suma todos los lados
    perimetro = baseMayor + baseMenor + hipotenusa*2
    return perimetro

def main():
    baseMayor = int(input("Escribe la longitud de la base mayor: "))
    baseMenor = int(input("Escribe la longitud de la base menor: "))
    altura = int(input("Escribe la altura: "))
    area = calcularArea(baseMayor, baseMenor, altura )
    hipotenusa = calcularHipotenusa(baseMayor, baseMenor, altura)
    perimetro = calcularPerimetro(baseMayor, baseMenor, hipotenusa)
    print("Area: %.2f" %area)
    print("Perímetro: %.2f"%perimetro)

main()
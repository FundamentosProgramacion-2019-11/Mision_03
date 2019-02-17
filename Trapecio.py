#Autor: Daniela Estrella Tovar
# Dada la Base Mayor, la Base Menor y la altura, calcular el área y el perímetro de un trapecio isósceles.

def calcularArea(baseMenor, baseMayor, altura):
    area= (baseMayor+baseMenor)/2 * altura
    return area
def imprimirArea(baseMenor, baseMayor, altura):
    area= calcularArea(baseMenor, baseMayor, altura)
    print("Área:  %.2f" %(area))

def calcularPerimetro(baseMenor, baseMayor, altura):
    lado= (((baseMayor-baseMenor)**2)/4 + altura**2) ** 0.5
    perimetro= baseMenor + baseMayor + lado*2
    return perimetro
def imprimirPerimetro(baseMenor, baseMayor, altura):
    perimetro= calcularPerimetro(baseMenor, baseMayor, altura)
    print("Perímetro: %.2f"% (perimetro))

def main():
    baseMayor= int(input("Escribe la longitud de la Base Mayor:  "))
    baseMenor= int(input("Escribe la longitud de la Base Menor: "))
    altura= int(input("Escribe la Altura: "))
    imprimirArea(baseMenor, baseMayor, altura)
    imprimirPerimetro(baseMayor, baseMenor, altura)

main()
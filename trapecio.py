#Emiliano Tartarini
#Trapecio
def calcularArea(BaseMenor, BaseMayor, ALTURA):

    AREA= (BaseMayor+BaseMenor)/2 * ALTURA
    return AREA

def calcularPerimetro(BaseMenor, BaseMayor, ALTURA):

    lado= (((BaseMayor-BaseMenor)**2)/4 + ALTURA**2) ** 0.5
    perimetro= BaseMenor + BaseMayor + lado*2
    return perimetro

def main():

    BaseMayor= int(input("Escribe Base Mayor:"))
    BaseMenor= int(input("Escribe Base Menor:"))
    ALTURA= int(input("Escribe la Altura:"))

    AREA= calcularArea(BaseMenor, BaseMayor, ALTURA)
    print("AREA:%.2f" % (AREA))

    PERIMETRO= calcularPerimetro(BaseMayor, BaseMenor, ALTURA)
    print("Perímetro:%.2f" % (PERIMETRO))

main()
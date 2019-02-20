#Luis Adrian Carmona Villalobos
#A01748395

def calcularArea(baseMayor,baseMenor,h):
    area = ((baseMayor+baseMenor)/2)*h
    return area
def calcularPerimetro(baseMayor,baseMenor,h):
    lado = ((((baseMayor-baseMenor)/2)**2)+(h**2))**.5
    perimetro = baseMayor+baseMenor+(lado*2)
    return perimetro
def main():
    baseMayor = float(input("Cual es la base mayor? "))
    baseMenor = float(input("Cual es la base menor? "))
    h = float(input("Cual es su altura? "))
    area = calcularArea(baseMayor,baseMenor,h)
    perimetro = calcularPerimetro(baseMayor,baseMenor,h)
    print("Area: %.2f"%area)
    print("Perimetro: %.2f"%perimetro)
main()


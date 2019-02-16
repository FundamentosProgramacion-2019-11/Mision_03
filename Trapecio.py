#Maria Angelica Hernandez Parada
#Area y perimetro de un trapecio

def calcularArea(baseMayor,baseMenor,altura):
    areaTotal= ((baseMayor+baseMenor)/2)*altura
    return areaTotal

def calcularPerimetro(baseMayor,baseMenor,altura):
    baseL = (baseMayor - baseMenor) / 2
    lado = (baseL**2 + altura**2)**0.5
    perimetroTotal= baseMayor + baseMenor + (2*lado)
    return perimetroTotal

def imprimirArea(baseMayor,baseMenor,altura):
    areaTotal = calcularArea(baseMayor, baseMenor, altura)
    print("Área: %.2f" % (areaTotal))

def imprimirPerimetro(baseMayor,baseMenor,altura):
    perimetroTotal = calcularPerimetro(baseMayor, baseMenor, altura)
    print("Perímetro: %.2f" % (perimetroTotal))

def main():
    baseMayor = int(input("Escribe la longitud de la base mayor: "))
    baseMenor = int(input("Escribe la longitud de la base menor: "))
    altura = int(input("Escribe la altura: "))
    calcularArea(baseMayor,baseMenor,altura)
    calcularPerimetro(baseMayor,baseMenor,altura)
    imprimirArea(baseMayor,baseMenor,altura)
    imprimirPerimetro(baseMayor,baseMenor,altura)

main()
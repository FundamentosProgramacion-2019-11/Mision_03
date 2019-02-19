# Autor: Itzel Yanabany Castro Becerril
# Calcular el area y el Perimetro de la figura anterior

def calcularArea(baseMayor, baseMenor, altura):
    area = ((baseMayor + baseMenor) / 2) * altura
    return area


def imprimirArea(baseMayor, baseMenor, altura):
    area = calcularArea(baseMayor, baseMenor, altura)
    print("Area:  %.2f" % (area))


def calcularPerimetro(baseMayor, baseMenor, altura):
    base = (baseMayor - baseMenor) / 2
    hip = (base ** 2 + altura ** 2) ** 0.5
    perimetro = baseMayor + baseMenor + hip * 2
    return perimetro


def imprimirPerimetro(baseMayor, baseMenor, altura):
    perimetro = calcularPerimetro(baseMayor, baseMenor, altura)
    print("Perimetro: %.2f " % (perimetro))


def main():
    baseMayor = int(input("Escribe la longitud de la base mayor: "))
    baseMenor = int(input("Escribe la longitud de la base menor: "))
    altura = int(input("Escribe la altura: "))
    imprimirArea(baseMayor, baseMenor, altura)
    imprimirPerimetro(baseMayor, baseMenor, altura)


main()

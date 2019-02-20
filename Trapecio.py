# Autor: Elizabeth Citlalli Zapata Cortes
# Descripción: Programa que muestre al usuario el área y el perímetro de un trapecio isósceles recibiendo
#              base mayor, base menor y la altura.

def calcularPerimetro(baseMayor, baseMenor, altura):
    baseTriangulo = (baseMayor - baseMenor) / 2
    lado = (altura**2 + baseTriangulo**2) **0.5
    perimetro = baseMayor + baseMenor + (lado*2)
    return  perimetro

def calcularArea(baseMayor, baseMenor, altura):
    area = ((baseMayor + baseMenor) / 2) * altura
    return area

def main():
    baseMayor = int(input("Escribe la longitud de la base mayor: "))
    baseMenor = int(input("Escribe la longitud de la base menor: "))
    altura = int(input("Escribe la altura: "))
    print("Área: %.2f" % (calcularArea(baseMayor, baseMenor, altura)))
    print("Perímetro: %.2f" % (calcularPerimetro(baseMayor, baseMenor, altura)))

main()
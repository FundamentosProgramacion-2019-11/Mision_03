# Autor: Juan Carlos Flores García A01376511. Grupo 02.
# Programa que calcula el área y perímetro de un trapecio isósceles.

# Función que calcula el área del trapecio.
def calcularArea(baseMayor, baseMenor, altura):
    area = ((baseMayor + baseMenor) / 2) * altura
    return area

# Función que calcula el tamaño de los lados inclinados y luego obtiene el perímetro del trapecio.
def calcularPerimetro(baseMayor, baseMenor, altura):
    x = (baseMayor - baseMenor) / 2
    hipotenusa = ((x ** 2) + (altura ** 2)) ** 0.5
    perimetro = baseMayor + baseMenor + hipotenusa * 2
    return perimetro

# Función principal.
def main():
    baseMayor = int(input("Escribe la longitud de la base mayor: "))
    baseMenor = int(input("Escribe la longitud de la base menor: "))
    altura = int(input("Escribe la altura: "))
    totalArea = calcularArea(baseMayor, baseMenor, altura)
    totalPerimetro = calcularPerimetro(baseMayor, baseMenor, altura)
    print("Área: %.2f" % (totalArea))
    print("Pérímetro: %.2f" % (totalPerimetro))

# Llamada a la función principal.
main()





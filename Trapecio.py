#Autor: Cecilia Daniela Olivares Hernández, a01745727
#Descripción: Calcula el área y perímetro de un trapecio.

#Esta funcion calcula el area del trapecio
def calcularArea(baseMayor, baseMenor, altura):
    area = ((baseMayor + baseMenor)/2)*altura
    return area

#Esta funcion calcula el perimetro del trapecio
def calcularPerimetro(baseMayor, baseMenor, altura):
    baseLado = (baseMayor - baseMenor)/2
    lado = (baseLado**2 + altura**2) ** 0.5
    perimetro = baseMayor + baseMenor + (2 * lado)
    return perimetro

#Funcion principal que resuelve el problema
def main():
    baseMayor = int(input("Escribe la longitud de la base mayor: "))
    baseMenor = int(input("Escribe la longitud de la base menor: "))
    altura = int(input("Escribe la altura: "))
    area = calcularArea(baseMayor, baseMenor, altura)
    perimetro = calcularPerimetro(baseMayor, baseMenor, altura)
    print("Área: " + "\x1b[1;30m" + "%.2f" % (area))
    print("\x1b[0;mPerímetro: " + "\x1b[1;30m" + "%.2f" % (perimetro))


main()

#Autor: Mariana Teyssier Cervantes
# Calcular el area y perimetro de un trapecio.

#calcular el area del trapecio con su formula.
def calcularArea(baseMayor, baseMenor, altura):
    area = float(baseMayor + baseMenor)/2*altura
    return area

#imprimir el area con dos decimales.
def ImprimirArea(baseMayor, baseMenor, altura):
    area = calcularArea(baseMayor, baseMenor, altura)
    print("Area: %.2f" % (area))

#calcular los dos lados diagonales del trapecio con el teorema de pitagoras.
#calcular la base (cateto) del triangulo.
def calcularLado(baseMayor, baseMenor, altura):
    cateto = float(baseMayor - baseMenor)/2
    lado = float(cateto**2 + altura**2)**0.5
    return lado

#imprimir el perimetro con dos decimales.
def ImprimirPerimetro(baseMayor, baseMenor, altura):
    lado = calcularLado(baseMayor, baseMenor, altura)
    perimetro = baseMayor + baseMenor + (lado*2)
    print("Perimetro: %.2f" % (perimetro))


#Decirle al usuario que escriba las medidas del trapecio.
#Calcular e imprimir el area y perimetro.

def main():
    baseMayor = int(input("Escribe la longitud de la base mayor: "))
    baseMenor = int(input("Escribe la longitud de la base menor: "))
    altura = int(input("Escribe la altura: "))
    ImprimirArea(baseMayor, baseMenor, altura)
    ImprimirPerimetro(baseMayor, baseMenor, altura)

#Llamar a la funcion -main-
main()

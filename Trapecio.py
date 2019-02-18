# Roberto Emmanuel González Muñoz A01376803
# Escribe un programa que lea la base mayor, la base menor
# y la altura de un trapecio isósceles y que imprima Area y Perímetro.


def calcularArea(B, b, h):
    area = ((B + b) * h) / 2
    return area


def calcularPerímetro(B, b, h):
    perimetro =((((((B-b)/2)**2)+ h**2)**.5) * 2) + B + b
    return perimetro


def main():
    
    # Adquirir los datos relevantes para calcular el are y el perimetro de un Trapecio.
    baseMayor = int(input("Escribe la longitud de la base mayor: "))
    baseMenor = int(input("Escriba la longitud de la base menor: "))
    altura = int(input("Escriba la altura: "))
    
    # Uso de funciones para el calculo.
    Area = calcularArea(baseMayor,baseMenor, altura)
    Perímetro = calcularPerímetro(baseMayor,baseMenor, altura)
    
    # Resultados
    print("_______________________________")
    print("Area: %.2f" % Area)
    print("Perímetro: %.2f" % Perímetro)
    print("_______________________________")

main()
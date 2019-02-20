# Paulina Guerrero Ruiz
# Escribir un problema que lea la base mayor, la base menor y la altura de un trapecio




def calcularArea(B, b, h):
    Area = ((B + b) * h)/2
    return Area

def calcularPerimetro(B,b,h):
    Perimetro = (h*2) + B + b
    return Perimetro


def main():
    B = int(input("Escribe la longitud de la base mayor: "))
    b = int(input("Escribe la longitud de la base menor: "))
    h = int(input(" Escribe la altura: "))
    Area = calcularArea(B,b,h)
    Perimetro = calcularPerimetro(B,b,h)
    print ("Area: %2.f" % (Area), "Perimetro %2.f"% (Perimetro))

main ()